# Sample E-commerce Inventory Database
inventory = {
    "SKU_101": {"name": "Wireless Mouse", "price": 25.00, "stock_count": 50, "category": "Electronics"},
    "SKU_102": {"name": "Gaming Keyboard", "price": 80.00, "stock_count": 0, "category": "Electronics"},
    "SKU_103": {"name": "Yoga Mat", "price": 30.00, "stock_count": 15, "category": "Fitness"},
    "SKU_104": {"name": "Bluetooth Speaker", "price": 120.00, "stock_count": 5, "category": "Electronics"},
    "SKU_105": {"name": "Protein Shaker", "price": 15.00, "stock_count": 0, "category": "Fitness"},
}


def apply_discount(inventory: dict, category: str, percent: float) -> None:
    """Reduce the price of every item in a category by the given percent."""
    for sku, item in inventory.items():
        if item["category"] == category:
            item["price"] = round(item["price"] * (1 - percent / 100), 2)
    return None


def flag_restock(inventory: dict, threshold: int = 0) -> None:
    """Add restock_urgent=True to items whose stock_count equals the threshold."""
    for sku, item in inventory.items():
        if item["stock_count"] == threshold:
            item["restock_urgent"] = True
    return None


def ensure_last_sold(inventory: dict, default: str = "Never") -> None:
    """Make sure every item has a 'last_sold' key."""
    for sku, item in inventory.items():
        item.setdefault("last_sold", default)
    return None


def view_inventory(inventory: dict) -> None:
    """Print every item on its own line."""
    for sku, item in inventory.items():
        print(sku, item)
    return None


if __name__ == "__main__":
    apply_discount(inventory, "Electronics", 15)
    flag_restock(inventory)
    ensure_last_sold(inventory)
    view_inventory(inventory)