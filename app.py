from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

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
    # Temporary search stub, you can improve later
    return redirect(url_for('view_products'))


if __name__ == "__main__":
         app.run(debug=True)

