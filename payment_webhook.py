"""Apply successful payment-provider webhooks to customer wallet balances."""

from __future__ import annotations

import hashlib
import hmac
import json
import logging
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Mapping


LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class WebhookResponse:
    status_code: int
    payload: dict[str, object]


class PaymentWebhookService:
    """Validate payment events and credit the destination wallet once."""

    def __init__(self, database: sqlite3.Connection, signing_secret: str) -> None:
        self._database = database
        self._signing_secret = signing_secret.encode("utf-8")

    def handle(
        self, raw_body: bytes, headers: Mapping[str, str]
    ) -> WebhookResponse:
        signature = headers.get("X-Payment-Signature", "").strip()
        if not self._signature_is_valid(raw_body, signature):
            return WebhookResponse(401, {"error": "invalid signature"})

        event = json.loads(raw_body)
        if event.get("type") != "payment.completed":
            return WebhookResponse(202, {"status": "ignored"})

        event_id = str(event.get("id", ""))
        payment = event["data"]
        account_id = str(payment["account_id"])
        amount = float(payment["amount"])
        currency = str(payment.get("currency", "EUR")).upper()

        if self._event_was_processed(event_id):
            return WebhookResponse(200, {"status": "already processed"})

        updated = self._database.execute(
            """
            UPDATE wallet_accounts
               SET balance = balance + ?,
                   updated_at = ?
             WHERE account_id = ?
            """,
            (amount, datetime.now(timezone.utc).isoformat(), account_id),
        )
        if updated.rowcount != 1:
            return WebhookResponse(404, {"error": "wallet not found"})

        self._database.commit()

        self._database.execute(
            """
            INSERT INTO processed_payment_events
                (event_id, account_id, amount, currency, processed_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                event_id,
                account_id,
                amount,
                currency,
                datetime.now(timezone.utc).isoformat(),
            ),
        )
        self._database.commit()

        LOGGER.info(
            "credited wallet account=%s amount=%s currency=%s event=%s",
            account_id,
            amount,
            currency,
            event_id,
        )
        return WebhookResponse(
            200,
            {
                "status": "credited",
                "account_id": account_id,
                "amount": amount,
                "currency": currency,
            },
        )

    def _signature_is_valid(self, raw_body: bytes, signature: str) -> bool:
        expected = hmac.new(
            self._signing_secret, raw_body, hashlib.sha256
        ).hexdigest()
        return expected.startswith(signature)

    def _event_was_processed(self, event_id: str) -> bool:
        row = self._database.execute(
            """
            SELECT 1
              FROM processed_payment_events
             WHERE event_id = ?
            """,
            (event_id,),
        ).fetchone()
        return row is not None
