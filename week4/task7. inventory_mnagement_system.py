import json
from datetime import datetime
FILE_NAME = "products.json"
class Product:
    def __init__(self, name, product_id, price, quantity, category):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.quantity = quantity
        self.category = category

    def display_product(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.name)
        print("Category:", self.category)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        if self.quantity == 0:
            print("Stock Status: Out of Stock")
        elif self.quantity <= 5:
            print("Stock Status: Low Stock")
        else:
            print("Stock Status: Available")

    def to_dictionary(self):
        return {"name": self.name,
            "product_id": self.product_id,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category}

products = []
transactions = []

def save_products():
    data = []
    for product in products:
        data.append(product.to_dictionary())
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def load_products():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
        for item in data:
            product = Product(item["name"],
                item["product_id"],
                item["price"],
                item["quantity"],
                item["category"])
            products.append(product)
    except FileNotFoundError:
        print("No existing product file found.")
        print("Starting with an empty inventory.")
    except json.JSONDecodeError:

        print("Product file is empty or corrupted.")
        print("Starting with an empty inventory.")

def find_product(product_id):
    for product in products:
        if product.product_id.lower() == product_id.lower():
            return product
    return None

def add_product():
    name = input("Enter product name: ")
    product_id = input("Enter product ID: ")
    if find_product(product_id) is not None:
        print("A product with this ID already exists.")
        return
    category = input("Enter product category: ")
    while True:
        try:
            price = float(input("Enter product price: "))
            if price >= 0:
                break
            else:
                print("Price cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            quantity = int(input("Enter product quantity: "))
            if quantity >= 0:
                break
            else:
                print("Quantity cannot be negative.")
        except ValueError:
            print("Please enter a whole number.")
    product = Product(name,
        product_id,
        price,
        quantity,
        category)
    products.append(product)
    save_products()
    print("Product added successfully!")

def view_products():
    if len(products) == 0:
        print("No products available.")
        return
    for product in products:
        product.display_product()

def search_product():
    search = input("Enter Product ID or Product Name: ").lower()
    found = False
    for product in products:
        if (product.product_id.lower() == search or product.name.lower() == search):
            product.display_product()
            found = True
    if not found:
        print("Product not found.")

def update_product():
    product_id = input("Enter Product ID: ")
    product = find_product(product_id)
    if product is None:
        print("Product not found.")
        return
    print("\nCurrent Product Information:")
    product.display_product()
    print("\nEnter New Information")
    new_name = input("Enter new product name: ")
    new_category = input("Enter new category: ")
    while True:
        try:
            new_price = float(input("Enter new price: "))
            if new_price >= 0:
                break
            else:
                print("Price cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            new_quantity = int(input("Enter new quantity: "))
            if new_quantity >= 0:
                break
            else:
                print("Quantity cannot be negative.")
        except ValueError:
            print("Please enter a whole number.")
    product.name = new_name
    product.category = new_category
    product.price = new_price
    product.quantity = new_quantity
    save_products()
    print("Product updated successfully!")

def delete_product():
    product_id = input("Enter Product ID: ")
    product = find_product(product_id)
    if product is None:
        print("Product not found.")
        return
    product.display_product()
    confirmation = input("Are you sure you want to delete this product? (yes/no): ").lower()
    if confirmation == "yes":
        products.remove(product)
        save_products()
        print("Product deleted successfully!")
    else:
        print("Delete operation cancelled.")

def check_stock():
    if len(products) == 0:
        print("No products available.")
        return
    for product in products:
        print(product.name,"-> Quantity:",product.quantity)
        if product.quantity == 0:
            print("Status: Out of Stock")
        elif product.quantity <= 5:
            print("Status: Low Stock")
        else:
            print("Status: Available")

def low_stock_products():
    found = False
    for product in products:
        if product.quantity <= 5:
            product.display_product()
            found = True
    if not found:
        print("No low-stock products.")

def total_inventory_value():
    total = 0
    for product in products:
        value = product.price * product.quantity
        total += value
    print("Total Inventory Value:",round(total, 2))

def sell_product():
    product_id = input("Enter Product ID: ")
    product = find_product(product_id)
    if product is None:
        print("Product not found.")
        return
    product.display_product()
    while True:
        try:
            quantity = int(input("Enter quantity to sell: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
            elif quantity > product.quantity:
                print("Not enough stock available.")
                print("Available stock:", product.quantity)
            else:
                break
        except ValueError:
            print("Please enter a whole number.")
    product.quantity -= quantity
    total_price = product.price * quantity
    transaction = {"type": "Sale",
        "product_id": product.product_id,
        "product_name": product.name,
        "quantity": quantity,
        "total_price": total_price,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    transactions.append(transaction)
    save_products()
    print("\nSale completed successfully!")
    print("Product:", product.name)
    print("Quantity Sold:", quantity)
    print("Total Sale:", round(total_price, 2))
    print("Remaining Stock:", product.quantity)

def purchase_product():
    product_id = input("Enter Product ID: ")
    product = find_product(product_id)
    if product is None:
        print("Product not found.")
        return
    product.display_product()
    while True:
        try:
            quantity = int(input("Enter quantity to add: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
            else:
                break
        except ValueError:
            print("Please enter a whole number.")
    product.quantity += quantity
    total_price = product.price * quantity
    transaction = {"type": "Purchase",
        "product_id": product.product_id,
        "product_name": product.name,
        "quantity": quantity,
        "total_price": total_price,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    transactions.append(transaction)
    save_products()
    print("\nStock updated successfully!")
    print("Product:", product.name)
    print("Quantity Added:", quantity)
    print("New Stock:", product.quantity)

def view_transactions():
    if len(transactions) == 0:
        print("No transactions recorded.")
        return
    for transaction in transactions:
        print("Type:", transaction["type"])
        print("Product:", transaction["product_name"])
        print("Product ID:", transaction["product_id"])
        print("Quantity:", transaction["quantity"])
        print("Total:", round(transaction["total_price"], 2))
        print("Date:", transaction["date"])

def category_search():
    category = input("Enter category: ").lower()
    found = False
    for product in products:
        if product.category.lower() == category:
            product.display_product()
            found = True
    if not found:
        print("No products found in this category.")

def main():
    load_products()
    while True:
        print("......INVENTORY MANAGEMENT SYSTEM......")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Check Stock")
        print("7. Low Stock Products")
        print("8. Total Inventory Value")
        print("9. Sell Product")
        print("10. Purchase / Restock")
        print("11. View Transaction History")
        print("12. Search by Category")
        print("13. Exit")
        choice = input("Enter your choice (1-13): ")
        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            check_stock()
        elif choice == "7":
            low_stock_products()
        elif choice == "8":
            total_inventory_value()
        elif choice == "9":
            sell_product()
        elif choice == "10":
            purchase_product()
        elif choice == "11":
            view_transactions()
        elif choice == "12":
            category_search()
        elif choice == "13":
            print("Thank you for using Inventory Management System!")
            break
        else:
            print("Invalid choice.Please select 1-13.")

main()