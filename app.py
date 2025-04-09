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
        category_data = db.categories.find_one({"id": int(id)})

        if not category_data:
            return jsonify({"error": "Category not found"}), 404

        # Convert ObjectId to string for JSON serialization
        category_data["_id"] = str(category_data["_id"])

        return jsonify(category_data)
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







products = [
    {
        "categoryId": 1,
        "productId": 101,
        "brand": "Sunfeast",
        "productTitle": "Good Day Butter Cookies",
        "productDescription": "Delicious and crunchy butter cookies perfect for tea-time cravings.",
        "averageReview": 4.3,
        "reviewCount": 285
    },
    {
        "categoryId": 1,
        "productId": 102,
        "brand": "Nestlé",
        "productTitle": "Maggi 2-Minute Noodles",
        "productDescription": "Classic instant noodles with a rich masala flavor, ready in 2 minutes.",
        "averageReview": 4.5,
        "reviewCount": 137
    },
    {
        "categoryId": 1,
        "productId": 103,
        "brand": "Haldiram's",
        "productTitle": "Aloo Bhujia",
        "productDescription": "Crispy potato-based namkeen with tangy and spicy notes.",
        "averageReview": 4.4,
        "reviewCount": 196
    },
    {
        "categoryId": 1,
        "productId": 104,
        "brand": "Kellogg's",
        "productTitle": "Chocos Breakfast Cereal",
        "productDescription": "Chocolate-flavored wheat curls loved by kids and adults alike.",
        "averageReview": 4.2,
        "reviewCount": 312
    },
    {
        "categoryId": 1,
        "productId": 105,
        "brand": "MTR",
        "productTitle": "Ready Mix Gulab Jamun",
        "productDescription": "Instant dessert mix to prepare soft and juicy Gulab Jamuns.",
        "averageReview": 4.1,
        "reviewCount": 98
    },
    {
        "categoryId": 1,
        "productId": 106,
        "brand": "Unibic",
        "productTitle": "Cashew Cookies",
        "productDescription": "Rich buttery cookies loaded with crunchy cashew nuts.",
        "averageReview": 4.3,
        "reviewCount": 177
    },
    {
        "categoryId": 1,
        "productId": 107,
        "brand": "Lay's",
        "productTitle": "Classic Salted Potato Chips",
        "productDescription": "Light, crispy, and perfectly salted potato chips for snacking.",
        "averageReview": 4.0,
        "reviewCount": 245
    },
    {
        "categoryId": 2,
        "productId": 201,
        "brand": "Amul",
        "productTitle": "Amul Butter",
        "productDescription": "Fresh, creamy and salty butter loved across Indian households.",
        "averageReview": 4.6,
        "reviewCount": 521
    },
    {
        "categoryId": 2,
        "productId": 202,
        "brand": "Mother Dairy",
        "productTitle": "Toned Milk - 500ml",
        "productDescription": "Pasteurized toned milk, ideal for daily tea, coffee or cooking.",
        "averageReview": 4.2,
        "reviewCount": 189
    },
    {
        "categoryId": 2,
        "productId": 203,
        "brand": "Nestlé",
        "productTitle": "Milkmaid Sweetened Condensed Milk",
        "productDescription": "Rich and creamy condensed milk used in desserts and sweets.",
        "averageReview": 4.7,
        "reviewCount": 230
    },
    {
        "categoryId": 2,
        "productId": 204,
        "brand": "Danone",
        "productTitle": "Greek Yogurt - Strawberry",
        "productDescription": "Protein-packed, smooth and creamy yogurt with real fruit.",
        "averageReview": 4.4,
        "reviewCount": 163
    },
    {
        "categoryId": 2,
        "productId": 205,
        "brand": "Britannia",
        "productTitle": "Cheese Cubes",
        "productDescription": "Soft and tasty processed cheese cubes for quick snacking.",
        "averageReview": 4.3,
        "reviewCount": 110
    },
    {
        "categoryId": 2,
        "productId": 206,
        "brand": "Amul",
        "productTitle": "Fresh Paneer - 200g",
        "productDescription": "Soft and fresh paneer made from pure milk for cooking.",
        "averageReview": 4.5,
        "reviewCount": 148
    },
    {
        "categoryId": 2,
        "productId": 207,
        "brand": "Nandini",
        "productTitle": "Curd (Dahi) - 500g",
        "productDescription": "Rich and thick curd made from fresh cow milk.",
        "averageReview": 4.2,
        "reviewCount": 97
    },
    {
        "categoryId": 3,
        "productId": 301,
        "brand": "Coca-Cola",
        "productTitle": "Coca-Cola Original Taste - 750ml",
        "productDescription": "Classic cola drink to refresh and uplift your mood instantly.",
        "averageReview": 4.4,
        "reviewCount": 520
    },
    {
        "categoryId": 3,
        "productId": 302,
        "brand": "Tropicana",
        "productTitle": "Tropicana 100% Orange Juice",
        "productDescription": "No added sugar, 100% pure fruit juice with natural Vitamin C.",
        "averageReview": 4.5,
        "reviewCount": 214
    },
    {
        "categoryId": 3,
        "productId": 303,
        "brand": "Red Bull",
        "productTitle": "Red Bull Energy Drink - 250ml",
        "productDescription": "Gives you wings when you need energy, focus and performance.",
        "averageReview": 4.3,
        "reviewCount": 412
    },
    {
        "categoryId": 3,
        "productId": 304,
        "brand": "Paper Boat",
        "productTitle": "Aam Panna Traditional Drink",
        "productDescription": "Tangy mango-based summer drink made from traditional recipe.",
        "averageReview": 4.6,
        "reviewCount": 179
    },
    {
        "categoryId": 3,
        "productId": 305,
        "brand": "Bru",
        "productTitle": "Bru Instant Coffee - 100g",
        "productDescription": "Aromatic and strong instant coffee for your perfect mornings.",
        "averageReview": 4.4,
        "reviewCount": 293
    },
    {
        "categoryId": 3,
        "productId": 306,
        "brand": "Lipton",
        "productTitle": "Lipton Green Tea - Honey Lemon",
        "productDescription": "Refreshing green tea blend with soothing honey and lemon.",
        "averageReview": 4.2,
        "reviewCount": 221
    },
    {
        "categoryId": 3,
        "productId": 307,
        "brand": "Bournvita",
        "productTitle": "Cadbury Bournvita Health Drink",
        "productDescription": "Nutritious malt drink packed with essential vitamins and minerals.",
        "averageReview": 4.6,
        "reviewCount": 331
    },
    {
        "categoryId": 4,
        "productId": 401,
        "brand": "MTR",
        "productTitle": "Paneer Butter Masala - Ready Meal",
        "productDescription": "North Indian favorite with rich creamy gravy, just heat & eat.",
        "averageReview": 4.1,
        "reviewCount": 188
    },
    {
        "categoryId": 4,
        "productId": 402,
        "brand": "ITC Kitchens of India",
        "productTitle": "Dal Bukhara - Heat & Eat",
        "productDescription": "Authentic slow-cooked black lentils in creamy tomato gravy.",
        "averageReview": 4.3,
        "reviewCount": 254
    },
    {
        "categoryId": 4,
        "productId": 403,
        "brand": "Haldiram's",
        "productTitle": "Pav Bhaji - Instant Meal",
        "productDescription": "Spicy mashed vegetable curry with real Mumbai flavor.",
        "averageReview": 4.0,
        "reviewCount": 176
    },
    {
        "categoryId": 4,
        "productId": 404,
        "brand": "Gits",
        "productTitle": "Instant Khatta Dhokla Mix",
        "productDescription": "Just add water and steam for soft and fluffy dhoklas.",
        "averageReview": 4.5,
        "reviewCount": 132
    },
    {
        "categoryId": 4,
        "productId": 405,
        "brand": "Haldiram's",
        "productTitle": "Rajma Chawal Meal Box",
        "productDescription": "Comfort food combo of spicy rajma and rice, microwavable.",
        "averageReview": 4.2,
        "reviewCount": 211
    },
    {
        "categoryId": 4,
        "productId": 406,
        "brand": "Maiyas",
        "productTitle": "Ready Idli Sambar",
        "productDescription": "South Indian combo of soft idlis with tangy sambar.",
        "averageReview": 4.1,
        "reviewCount": 99
    },
    {
        "categoryId": 4,
        "productId": 407,
        "brand": "MTR",
        "productTitle": "Poha - Instant Breakfast",
        "productDescription": "Flattened rice cooked with spices, just add hot water.",
        "averageReview": 4.3,
        "reviewCount": 165
    },
    {
        "categoryId": 5,
        "productId": 501,
        "brand": "Himalaya",
        "productTitle": "Ashwagandha Tablets",
        "productDescription": "Herbal stress reliever to support mental and physical wellness.",
        "averageReview": 4.5,
        "reviewCount": 275
    },
    {
        "categoryId": 5,
        "productId": 502,
        "brand": "Ensure",
        "productTitle": "Ensure Nutritional Powder - Vanilla",
        "productDescription": "Complete, balanced nutrition for adults with essential vitamins.",
        "averageReview": 4.4,
        "reviewCount": 198
    },
    {
        "categoryId": 5,
        "productId": 503,
        "brand": "MuscleBlaze",
        "productTitle": "Whey Protein - Chocolate",
        "productDescription": "Premium whey protein supplement to support muscle growth.",
        "averageReview": 4.6,
        "reviewCount": 412
    },
    {
        "categoryId": 5,
        "productId": 504,
        "brand": "Zandu",
        "productTitle": "Zandu Chyavanprash",
        "productDescription": "Immunity-boosting Ayurvedic tonic enriched with herbs.",
        "averageReview": 4.3,
        "reviewCount": 146
    },
    {
        "categoryId": 5,
        "productId": 505,
        "brand": "Kapiva",
        "productTitle": "Apple Cider Vinegar - 500ml",
        "productDescription": "Natural detox drink to boost metabolism and digestion.",
        "averageReview": 4.1,
        "reviewCount": 137
    },
    {
        "categoryId": 5,
        "productId": 506,
        "brand": "Fast&Up",
        "productTitle": "Recharge Electrolyte Drink",
        "productDescription": "Fast-acting effervescent tablets to hydrate and energize.",
        "averageReview": 4.4,
        "reviewCount": 219
    },
    {
        "categoryId": 5,
        "productId": 507,
        "brand": "Horlicks",
        "productTitle": "Horlicks Protein+",
        "productDescription": "Specialized protein nutrition for adults with added minerals.",
        "averageReview": 4.3,
        "reviewCount": 264
    },
    {
        "categoryId": 6,
        "productId": 601,
        "brand": "McDonald's",
        "productTitle": "McAloo Tikki Burger",
        "productDescription": "Iconic vegetarian burger with spiced potato patty.",
        "averageReview": 4.2,
        "reviewCount": 841
    },
    {
        "categoryId": 6,
        "productId": 602,
        "brand": "Domino's",
        "productTitle": "Peppy Paneer Pizza - Medium",
        "productDescription": "Loaded with paneer, capsicum, and spicy seasoning.",
        "averageReview": 4.4,
        "reviewCount": 637
    },
    {
        "categoryId": 6,
        "productId": 603,
        "brand": "Subway",
        "productTitle": "Veggie Delite Sub",
        "productDescription": "Freshly baked sub filled with crunchy veggies and sauces.",
        "averageReview": 4.5,
        "reviewCount": 403
    },
    {
        "categoryId": 6,
        "productId": 604,
        "brand": "Pizza Hut",
        "productTitle": "Tandoori Paneer Personal Pizza",
        "productDescription": "Indian-style pizza with spicy paneer chunks and capsicum.",
        "averageReview": 4.3,
        "reviewCount": 378
    },
    {
        "categoryId": 6,
        "productId": 605,
        "brand": "Burger King",
        "productTitle": "Crispy Veg Burger",
        "productDescription": "Crunchy burger patty with fresh veggies and mayo.",
        "averageReview": 4.1,
        "reviewCount": 321
    },
    {
        "categoryId": 6,
        "productId": 606,
        "brand": "KFC",
        "productTitle": "Hot & Crispy Chicken Bucket - 4 pcs",
        "productDescription": "Signature fried chicken, juicy and crunchy with secret spices.",
        "averageReview": 4.6,
        "reviewCount": 509
    },
    {
        "categoryId": 6,
        "productId": 607,
        "brand": "Starbucks",
        "productTitle": "Cold Coffee - Tall",
        "productDescription": "Chilled blend of coffee, milk, and ice with whipped cream.",
        "averageReview": 4.5,
        "reviewCount": 287
    }
]





collection=db["Products"]
@app.route("/insert-data", methods=["GET"])
def insert_data():
    collection.insert_many(products)
    return jsonify({"message": "Data inserted successfully!"})
















if __name__ == '__main__':
    app.run(debug=True)