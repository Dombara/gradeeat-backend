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





@app.route('/category/<string:id>', methods=['GET'])
def get_category_by_id(id):
    try:
        category_id = int(id)

        # Fetch category
        category_info = db.categories.find_one({"id": category_id})
        if not category_info:
            return jsonify({"error": "Category not found"}), 404
        category_info["_id"] = str(category_info["_id"])  # Convert ObjectID to string

        # Fetch products
        products_cursor = db.products.find({"categoryId": category_id})
        products = list(products_cursor)
        for product in products:
            product["_id"] = str(product["_id"])  # Convert ObjectID to string

        # Combine into a single array
        response = [category_info] + products

        return jsonify(response)

    except ValueError:
        return jsonify({"error": "Invalid ID format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500



# Get reviews by product ID
@app.route('/get_reviews/<string:id>', methods=['GET'])
def get_reviews_by_product_id(id):
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
        complaints = db.complaints.find({"categoryId": int(id)})
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
        products_analytics_data=list(db.products.find({"category_id": category_id}))

        if not products_analytics_data:
            return jsonify({"status": "error", "message": "No products found for this category"}), 404
        
        for product in products_analytics_data:
            product["_id"] = str(product["_id"])
            # product["category_id"] = str(product["category_id"])

        top_rated = sorted(products_analytics_data, key=lambda x: x.get("rating", 0), reverse=True)[:5]
        
        top_rated_data = [
            {
                "name": p.get("name"),
                "rating": p.get("rating"),
                "brand": p.get("brand")
            } for p in top_rated
        ]



        # least_complaints = sorted(products_analytics_data, key=lambda x: len(x.get("complaints", [])))[:5]

        # least_complaints_data = [
        #     {
        #         "name": p.get("name"),
        #         "complaints_count": len(p.get("complaints", [])),
        #         "brand": p.get("brand")
        #     } for p in least_complaints
        # ]


        return jsonify({
            "status": "success",
            "category_id": category_id,
            "top_rated_products": top_rated_data
            # "least_complaints_products": least_complaints_data
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500













# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
