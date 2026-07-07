"""Domain models."""
from dataclasses import dataclass


@dataclass
class Order:
    order_id: str
    customer: str
    total_usd: float
    status: str = "pending"
