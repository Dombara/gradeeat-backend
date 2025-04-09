import os
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

MONGO_URI="mongodb+srv://yash:yash@cluster0.bcuflio.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)








@app.route('/')
def index():
    return "Welcome to the Flask MongoDB API!"
















@app.route('/categories', methods=['GET'])
def get_categories():
    category_data = [
        {
            "id": 1,
            "icon": "/images/icon/icon-01.svg",
            "title": "Crafted for SaaS",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In convallis tortor."
        },
        {
            "id": 2,
            "icon": "/images/icon/icon-02.svg",
            "title": "High-quality Design",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In convallis tortor."
        },
        {
            "id": 3,
            "icon": "/images/icon/icon-03.svg",
            "title": "Next.js 13 + TypeScript",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In convallis tortor."
        },
        {
            "id": 4,
            "icon": "/images/icon/icon-04.svg",
            "title": "Sanity Blog and Docs",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In convallis tortor."
        },
        {
            "id": 5,
            "icon": "/images/icon/icon-05.svg",
            "title": "DB, Auth and Stripe",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In convallis tortor."
        },
        {
            "id": 6,
            "icon": "/images/icon/icon-06.svg",
            "title": "Regular Free Updates",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In convallis tortor."
        }
    ]
    return jsonify(category_data)
















@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    mongo.db.test_collection.insert_one(data)
    return jsonify({"message": "Data inserted successfully!"})








if __name__ == '__main__':
    app.run(debug=True)