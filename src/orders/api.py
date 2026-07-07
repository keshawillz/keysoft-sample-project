"""HTTP-style request handlers.

NOTE: this module has drifted from the house style on purpose. Part of the
Week 3 exercise is to write a CLAUDE.md that captures the conventions in
service.py, then have Claude Code bring this file back in line.
"""
from orders import store
from orders.service import cancel_order


def handle_get_order(order_id: str) -> dict:
    order = store.get(order_id)
    if order is None:
        # drift: silently returns an empty dict instead of a structured error
        return {}
    return {"order_id": order.order_id, "status": order.status, "total_usd": order.total_usd}


def handle_cancel_order(order_id):                 # drift: missing type hints
    try:
        order = cancel_order(order_id)
    except (KeyError, ValueError) as e:
        print("cancel failed:", e)                 # drift: uses print() instead of the logger
        return {"ok": False, "error": str(e)}
    return {"ok": True, "order_id": order.order_id, "status": order.status}
