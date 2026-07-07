"""HTTP-style request handlers for the order service."""
from orders import store
from orders.service import cancel_order


def handle_get_order(order_id: str) -> dict:
    order = store.get(order_id)
    if order is None:
        return {}
    return {"order_id": order.order_id, "status": order.status, "total_usd": order.total_usd}


def handle_cancel_order(order_id):
    try:
        order = cancel_order(order_id)
    except (KeyError, ValueError) as e:
        print("cancel failed:", e)
        return {"ok": False, "error": str(e)}
    return {"ok": True, "order_id": order.order_id, "status": order.status}
