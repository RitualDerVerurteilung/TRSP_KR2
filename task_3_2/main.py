from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
app = FastAPI() # Запуск: uvicorn task_3_2.main:app --reload

sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]

@app.get("/products/search")
def search_products(
        keyword: str = Query(),
        category: str = Query(default=None),
        limit: int = Query(10),
):
    results = []
    for product in sample_products:
        if len(results) == limit:
            break
        if keyword in product["name"]:
            results.append(product)
        elif category is not None and category == product["category"]:
            results.append(product)
    return results

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in sample_products:
        if product["product_id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Item not found")