from flask import Flask, request

app = Flask(__name__)

items = [
    {
        "name": "Litchi",
        "eater": 40,
        "eating": "Bubu"
    },
    {
        "name": "Mango",
        "eater": 20,
        "eating": "Hero"
    }
]

@app.get("/get-items")
def get_items():
    return {"items": items}

@app.post("/add-items")
def add_items():
    request_data = request.get_json() # it returns a python dictionary from the body
    items.append(request_data)
    return {"items": items}

