

from dataclasses import dataclass
from uuid import uuid4


@dataclass(frozen=True)
class OrderLine:
    sku: str
    quantity: int


@dataclass(frozen=True)
class Order:
    order_id: str
    customer_id: str
    order_lines: list[OrderLine]


@dataclass(frozen=True)
class Batch:
    batch_id: str
    sku: str
    quantity: int


@dataclass(frozen=True)
class Allocation:
    allocation_id: str
    batch_id: str
    sku: str
    quantity: int
