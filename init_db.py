from pymongo import MongoClient

client = MongoClient("mongodb+srv://anja0007:r65IkY2ECPcTc8Ur@clustercst8276.37todo3.mongodb.net/")
db = client.catalog
collection = db.products

# Clear existing data to avoid duplicates
collection.delete_many({})

# Sample data
sample_products = [
    {"name": "Wireless Mouse", "price": 19.99, "category": "Electronics", "description": "Ergonomic wireless mouse", "stock": 50},
    {"name": "Graphic T-Shirt", "price": 15.00, "category": "Clothing", "description": "Cotton tee with logo", "stock": 100},
    {"name": "Notebook", "price": 9.99, "category": "Books", "description": "Hardcover notebook", "stock": 75},
    {"name": "Laptop", "price": 999.99, "category": "Electronics", "description": "16GB RAM, 512GB SSD", "stock": 10},
    {"name": "Headphones", "price": 49.99, "category": "Electronics", "description": "Wireless noise-canceling headphones", "stock": 30}
]
collection.insert_many(sample_products)
print(f"Inserted {len(sample_products)} products.")