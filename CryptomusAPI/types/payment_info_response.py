from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional


@dataclass
class PaymentInfoResponse:
    state: int
    uuid: str
    order_id: str
    amount: float
    payment_status: str
    url: str
    expired_at: int
    status: str
    is_final: bool
    created_at: datetime
    updated_at: datetime
    commission: float
    payment_amount: Optional[float] = None
    payment_amount_usd: Optional[float] = None
    payer_amount: Optional[float] = None
    additional_data: Optional[str] = None
    payer_amount_exchange_rate: Optional[float] = None
    discount_percent: Optional[float] = None
    discount: Optional[float] = None
    payer_currency: Optional[str] = None
    currency: Optional[str] = None
    comments: Optional[str] = None
    merchant_amount: Optional[float] = None
    network: Optional[str] = None
    address: Optional[str] = None
    from_: Optional[str] = None
    txid: Optional[str] = None
    address_qr_code: Optional[str] = None

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> PaymentInfoResponse:
        from_ = data["result"].pop("from", None)
        return cls(state=data["state"], from_=from_, **data["result"])
