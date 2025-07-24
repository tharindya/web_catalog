from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.regex import Regex

app = Flask(__name__)
client = MongoClient("mongodb+srv://minhquan:qJPRYNm8ruSEqjWf@cluster0.jtvun9w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.catalog
collection = db.products

@app.route("/")
def home():
    return "Welcome to Web Catalog!"

@app.route("/products")
def view_products():
         products = collection.find()
         return render_template("index.html", products=products)

@app.route("/products/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        product = {
            "name": request.form["name"],
            "price": float(request.form["price"]),
            "category": request.form["category"],
            "description": request.form["description"],
            "stock": int(request.form["stock"])
        }
        collection.insert_one(product)
        return redirect(url_for("view_products"))
    return render_template("add_product.html")

@app.route("/search")
def search_products():
    query = request.args.get("query", "")
    if query:
        search_filter = {
            "$or": [
                {"name": {"$regex": Regex(query, "i")}},
                {"category": {"$regex": Regex(query, "i")}}
            ]
        }
        products = collection.find(search_filter)
    else:
        products = collection.find()
    return render_template("index.html", products=products)

@app.route("/products/delete/<product_id>", methods=["POST"])
def delete_product(product_id):
    collection.delete_one({"_id": ObjectId(product_id)})
    return redirect(url_for("view_products"))

@app.route("/products/update/<product_id>", methods=["GET", "POST"])
def update_product(product_id):
    product = collection.find_one({"_id": ObjectId(product_id)})

    if request.method == "POST":
        updated_data = {
            "name": request.form["name"],
            "price": float(request.form["price"]),
            "category": request.form["category"],
            "description": request.form["description"],
            "stock": int(request.form["stock"])
        }
        collection.update_one({"_id": ObjectId(product_id)}, {"$set": updated_data})
        return redirect(url_for("view_products"))

    return render_template("update_product.html", product=product)


if __name__ == "__main__":
         app.run(debug=True)

