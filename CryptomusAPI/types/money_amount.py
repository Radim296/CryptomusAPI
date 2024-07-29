from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Union

from ..enums import CryptoCurrency, FiatCurrency


@dataclass
class MoneyAmount:
    amount: Decimal
    payment_amount: Decimal
    payment_amount_usd: Decimal
    payer_amount: Decimal
    payer_amount_exchange_rate: Optional[Decimal]
    discount_percent: Decimal
    discount: Decimal
    payer_currency: Union[CryptoCurrency, FiatCurrency]
