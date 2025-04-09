from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)

# Use your full Mongo URI
MONGO_URI = "mongodb+srv://yash:yash@cluster0.bcuflio.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Configure the app to use the URI
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)

# Access the specific database manually since no default DB is defined in the URI
db = mongo.cx["mydb"]  # 👈 Replace 'yourdbname' with your actual database name





@app.route('/')
def index():
    # print(db)
    return "Welcome to the Flask MongoDB API!"
















@app.route('/categories', methods=['GET'])
def get_categories():
    category_data = [
        {
            "id": 1,
            "icon": "/images/icon/icon-01.svg",
            "title": "Crafted for SaaS",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In convallis tortor."
        }
        ,
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
        }
        # ,
        # {
        #     "id": 6,
        #     "icon": "/images/icon/icon-06.svg",
        #     "title": "Regular Free Updates",
        #     "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In convallis tortor."
        # }
    ]
    return jsonify(category_data)




@app.route('/category/<string:id>', methods=['GET'])
def get_category_by_id(id):
    try:
        category_data = db.Products.find({"categoryId": int(id)})
        products = list(category_data)

        if not products:
            return jsonify({"error": "Category not found"}), 404

        # Convert ObjectId to string for JSON serialization
        for product in products:
            product["_id"] = str(product["_id"])

        return jsonify(products)
    except ValueError:
        return jsonify({"error": "Invalid ID format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500







@app.route('/reviews/<string:id>', methods=['GET'])
def get_category_by_id(id):
    try:
        category_data = db.reviews.find({"categoryId": int(id)})
        products = list(category_data)

        if not products:
            return jsonify({"error": "Category not found"}), 404

        # Convert ObjectId to string for JSON serialization
        for product in products:
            product["_id"] = str(product["_id"])

        return jsonify(products)
    except ValueError:
        return jsonify({"error": "Invalid ID format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500











@app.route('/add', methods=['POST'])
def add_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        db.categories.insert_one(data)
        return jsonify({"message": "Data inserted successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500



















if __name__ == '__main__':
    app.run(debug=True)