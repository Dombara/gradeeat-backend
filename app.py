from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)

# MongoDB URI
MONGO_URI = "mongodb+srv://yash:yash@cluster0.bcuflio.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)

# Specify the database
db = mongo.cx["mydb"]

# Home route
@app.route('/')
def index():
    return "Welcome to the Flask MongoDB API!"

# Static category data
@app.route('/categories', methods=['GET'])
def get_categories():
    category_data = [
        {
            "id": 1,
            "icon": "/images/icon/icon-01.svg",
            "title": "Packaged Food",
            "description": "Explore snacks, ready meals, and all packaged products reviewed by real users for freshness and quality"
        },
        {
            "id": 2,
            "icon": "/images/icon/icon-02.svg",
            "title": "Dairy Products",
            "description": "Check ratings on milk, cheese, curd and more – freshness, quality, and hygiene verified by the community"
        },
        {
            "id": 3,
            "icon": "/images/icon/icon-03.svg",
            "title": "Beverages",
            "description": "From juices to soft drinks, see what’s refreshing and what’s not – based on authentic user reviews"
        },
        {
            "id": 4,
            "icon": "/images/icon/icon-04.svg",
            "title": "Ready-to-Eat",
            "description": "Microwave meals and instant mixes—find out which ones actually taste good and meet food safety norms."
        },
        {
            "id": 5,
            "icon": "/images/icon/icon-05.svg",
            "title": "Health & Nutrition",
            "description": "Whey proteins, vitamins, and more—get feedback from real users before you consume for your wellness."
        },
        {
        "id": 6,
        "icon": "/images/icon/icon-06.svg",
        "title": "Food Chains",
        "description": "Popular restaurants and food chains rated for cleanliness, taste, and service. Add your own experience!"
    }
    ]
    return jsonify(category_data)





# Get products by category ID
@app.route('/category/<string:id>', methods=['GET'])
def get_category_by_id(id):
    try:
        # Convert category ID to integer
        category_id = int(id)

        # Fetch products belonging to this category
        category_data = db.products.find({"categoryId": category_id})
        products = list(category_data)

        # Fetch category information
        category_info = db.categories.find_one({"id": category_id})

        if not category_info:
            return jsonify({"error": "Category not found"}), 404

        # Convert MongoDB ObjectIDs to strings
        for product in products:
            product["_id"] = str(product["_id"])

            category_info["_id"] = str(category_info["_id"])

        # Return both category and product data
        return jsonify([category_info] + products)

    except ValueError:
        return jsonify({"error": "Invalid ID format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500




# Get reviews by category ID
@app.route('/reviews/<string:id>', methods=['GET'])
def get_reviews_by_category_id(id):
    try:
        reviews = db.reviews.find({"productId": int(id)})
        reviews_list = list(reviews)

        if not reviews_list:
            return jsonify({"error": "Category not found"}), 404

        for review in reviews_list:
            review["_id"] = str(review["_id"])

        return jsonify(reviews_list)
    except ValueError:
        return jsonify({"error": "Invalid ID format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    






@app.route('/complaints/<string:id>', methods=['GET'])
def get_complaints_by_category_id(id):
    try:
        complaints = db.complaints.find({"productId": int(id)})
        complaints_list = list(complaints)

        if not complaints_list:
            return jsonify({"error": "Category not found"}), 404

        for review in complaints_list:
            review["_id"] = str(review["_id"])

        return jsonify(complaints_list)
    except ValueError:
        return jsonify({"error": "Invalid ID format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Add category data
# @app.route('/add', methods=['POST'])
# def add_category():
#     data = request.get_json()
#     if not data:
#         return jsonify({"error": "No data provided"}), 400

#     try:
#         db.categories.insert_one(data)
#         return jsonify({"message": "Data inserted successfully!"}), 201
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# Add review data
@app.route('/add-review', methods=['POST'])
def add_review():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        db.reviews.insert_one(data)
        return jsonify({"message": "Review inserted successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
















@app.route('/add-complaint', methods=['POST'])
def add_complaint():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        db.complaints.insert_one(data)
        return jsonify({"message": "Review inserted successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    




@app.route('/analytics/<int:category_id>', methods=['GET'])
def categories_analytics(category_id):
    try:
        # Use correct field name as per DB schema: 'categoryId' not 'category_id'
        products = list(db.products.find({"categoryId": category_id}))

        if not products:
            return jsonify({"status": "error", "message": "No products found for this category"}), 404

        for product in products:
            product["_id"] = str(product["_id"])

        top_rated = sorted(products, key=lambda x: x.get("averageReview", 0), reverse=True)[:5]

        top_rated_data = [
            {
                "name": p.get("productTitle"),
                "rating": p.get("averageReview"),
                "brand": p.get("brand")
            } for p in top_rated
        ]

        return jsonify({
            "status": "success",
            "category_id": category_id,
            "top_rated_products": top_rated_data
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500












# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
