import json
from abc import ABC, abstractmethod


class OutOfStockError(Exception):
    pass


class DuplicateProductError(Exception):
    pass


class InvalidProductDataError(Exception):
    pass


class Product(ABC):
    def __init__(self, product_id, name, price, quantity_in_stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity_in_stock = quantity_in_stock

    @abstractmethod
    def restock(self, amount):
        pass

    @abstractmethod
    def sell(self, quantity):
        pass

    @abstractmethod
    def to_dict(self):
        pass

    def get_total_value(self):
        return self._price * self._quantity_in_stock

    def __str__(self):
        return f"{self._name} (ID: {self._product_id}) - Rs.{self._price}, Stock: {self._quantity_in_stock}"


# Subclass: Electronics
class Electronics(Product):
    def __init__(
        self, product_id, name, price, quantity_in_stock, brand, warranty_years
    ):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._brand = brand
        self._warranty_years = warranty_years

    def restock(self, amount):
        self._quantity_in_stock += amount

    def sell(self, quantity):
        if quantity <= self._quantity_in_stock:
            self._quantity_in_stock -= quantity
        else:
            raise OutOfStockError("Not enough stock for Electronics.")

    def __str__(self):
        return (
            super().__str__()
            + f" | Brand: {self._brand}, Warranty: {self._warranty_years} years"
        )

    def to_dict(self):
        return {
            "type": "Electronics",
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "quantity_in_stock": self._quantity_in_stock,
            "brand": self._brand,
            "warranty_years": self._warranty_years,
        }


# Subclass: Groceries
class Groceries(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, expiry_date):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._expiry_date = expiry_date

    def restock(self, amount):
        self._quantity_in_stock += amount

    def sell(self, quantity):
        if quantity <= self._quantity_in_stock:
            self._quantity_in_stock -= quantity
        else:
            raise OutOfStockError("Not enough stock for Groceries.")

    def __str__(self):
        return super().__str__() + f" | Expiry Date: {self._expiry_date}"

    def to_dict(self):
        return {
            "type": "Groceries",
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "quantity_in_stock": self._quantity_in_stock,
            "expiry_date": self._expiry_date,
        }


# Subclass: Clothing
class Clothing(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, size, fabric):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._size = size
        self._fabric = fabric

    def restock(self, amount):
        self._quantity_in_stock += amount

    def sell(self, quantity):
        if quantity <= self._quantity_in_stock:
            self._quantity_in_stock -= quantity
        else:
            raise OutOfStockError("Not enough stock for Clothing.")

    def __str__(self):
        return super().__str__() + f" | Size: {self._size}, Fabric: {self._fabric}"

    def to_dict(self):
        return {
            "type": "Clothing",
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "quantity_in_stock": self._quantity_in_stock,
            "size": self._size,
            "fabric": self._fabric,
        }


# Helper Functions
def get_non_empty_input(prompt, cast_type=str):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Input cannot be empty. Please try again.")
            continue
        try:
            return cast_type(value)
        except ValueError:
            print(f"Invalid input. Please enter a valid {cast_type.__name__}.")


def save_to_file(filename, inventory):
    data = [item.to_dict() for item in inventory]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print("Inventory saved successfully.")


def load_from_file(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            inventory = []
            for item in data:
                product_type = item.pop("type", None)
                if product_type == "Electronics":
                    inventory.append(Electronics(**item))
                elif product_type == "Groceries":
                    inventory.append(Groceries(**item))
                elif product_type == "Clothing":
                    inventory.append(Clothing(**item))
                else:
                    raise InvalidProductDataError("Unknown product type.")
            print("Inventory loaded successfully.")
            return inventory
    except FileNotFoundError:
        print("File not found.")
        return []
    except Exception as e:
        print("Error loading data:", str(e))
        return []


def find_product_by_id(inventory, product_id):
    for item in inventory:
        if item._product_id == product_id:
            return item
    return None


# CLI Menu
def menu():
    inventory = []

    while True:
        print("\n--- Inventory Menu ---")
        print("1. Add Product")
        print("2. Sell Product")
        print("3. View/Search Product")
        print("4. Save Inventory")
        print("5. Load Inventory")
        print("6. Exit")

        choice = input("Choose an option: ").strip()
        if not choice:
            print("You must choose an option.")
            continue

        if choice == "1":
            pid = get_non_empty_input("Product ID: ", int)
            if find_product_by_id(inventory, pid):
                print("Product with this ID already exists.")
                continue
            name = get_non_empty_input("Name: ")
            price = get_non_empty_input("Price: ", float)
            qty = get_non_empty_input("Quantity: ", int)
            print("Product Type: 1) Electronics 2) Groceries 3) Clothing")
            t = get_non_empty_input("Choose type (1/2/3): ")

            if t == "1":
                brand = get_non_empty_input("Brand: ")
                warranty = get_non_empty_input("Warranty years: ", int)
                inventory.append(Electronics(pid, name, price, qty, brand, warranty))
            elif t == "2":
                expiry = get_non_empty_input("Expiry Date (YYYY-MM-DD): ")
                inventory.append(Groceries(pid, name, price, qty, expiry))
            elif t == "3":
                size = get_non_empty_input("Size: ")
                fabric = get_non_empty_input("Fabric: ")
                inventory.append(Clothing(pid, name, price, qty, size, fabric))
            else:
                print("Invalid type.")

        elif choice == "2":
            pid = get_non_empty_input("Enter Product ID to sell: ", int)
            product = find_product_by_id(inventory, pid)
            if product:
                qty = get_non_empty_input("Quantity to sell: ", int)
                try:
                    product.sell(qty)
                    print("Sold successfully.")
                except OutOfStockError as e:
                    print("[Error]", e)
            else:
                print("Product not found.")

        elif choice == "3":
            pid = get_non_empty_input("Enter Product ID to view: ", int)
            product = find_product_by_id(inventory, pid)
            if product:
                print(product)
                print(f"Total Value: Rs.{product.get_total_value()}")
            else:
                print("Product not found.")

        elif choice == "4":
            filename = get_non_empty_input("Enter filename to save: ")
            save_to_file(filename, inventory)

        elif choice == "5":
            filename = get_non_empty_input("Enter filename to load: ")
            inventory = load_from_file(filename)

        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()
