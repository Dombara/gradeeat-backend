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




data=[
  {
    "categoryId": 1,
    "productId": 101,
    "reviewerName": "Aadhya Rao",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 1,
    "productId": 101,
    "reviewerName": "Vivaan Shah",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 1,
    "productId": 101,
    "reviewerName": "Diya Sharma",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 1,
    "productId": 101,
    "reviewerName": "Vihaan Patel",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 1,
    "productId": 101,
    "reviewerName": "Ananya Gupta",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 1,
    "productId": 102,
    "reviewerName": "Ira Bhattacharya",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 1,
    "productId": 102,
    "reviewerName": "Vivaan Shah",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 1,
    "productId": 102,
    "reviewerName": "Ira Bhattacharya",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 1,
    "productId": 102,
    "reviewerName": "Meera Nambiar",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 1,
    "productId": 102,
    "reviewerName": "Diya Sharma",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 1,
    "productId": 103,
    "reviewerName": "Myra Das",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 1,
    "productId": 103,
    "reviewerName": "Meera Nambiar",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 1,
    "productId": 103,
    "reviewerName": "Aarav Mehta",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 1,
    "productId": 103,
    "reviewerName": "Pari Kapoor",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 1,
    "productId": 103,
    "reviewerName": "Kunal Verma",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 1,
    "productId": 104,
    "reviewerName": "Ananya Gupta",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 1,
    "productId": 104,
    "reviewerName": "Ananya Gupta",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 1,
    "productId": 104,
    "reviewerName": "Kunal Verma",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 1,
    "productId": 104,
    "reviewerName": "Ishaan Roy",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 1,
    "productId": 104,
    "reviewerName": "Vihaan Patel",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 1,
    "productId": 105,
    "reviewerName": "Reyansh Iyer",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 1,
    "productId": 105,
    "reviewerName": "Ishaan Roy",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 1,
    "productId": 105,
    "reviewerName": "Saanvi Singh",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 1,
    "productId": 105,
    "reviewerName": "Vivaan Shah",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 1,
    "productId": 105,
    "reviewerName": "Saanvi Singh",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 1,
    "productId": 106,
    "reviewerName": "Saanvi Singh",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 1,
    "productId": 106,
    "reviewerName": "Ira Bhattacharya",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 1,
    "productId": 106,
    "reviewerName": "Ananya Gupta",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 1,
    "productId": 106,
    "reviewerName": "Aditya Joshi",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 1,
    "productId": 106,
    "reviewerName": "Diya Sharma",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 1,
    "productId": 107,
    "reviewerName": "Rohan Malhotra",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 1,
    "productId": 107,
    "reviewerName": "Ishaan Roy",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 1,
    "productId": 107,
    "reviewerName": "Rohan Malhotra",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 1,
    "productId": 107,
    "reviewerName": "Kunal Verma",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 1,
    "productId": 107,
    "reviewerName": "Aditya Joshi",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 2,
    "productId": 201,
    "reviewerName": "Krishna Nair",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 2,
    "productId": 201,
    "reviewerName": "Ira Bhattacharya",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 2,
    "productId": 201,
    "reviewerName": "Kunal Verma",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 2,
    "productId": 201,
    "reviewerName": "Ananya Gupta",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 2,
    "productId": 201,
    "reviewerName": "Aarav Mehta",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 2,
    "productId": 202,
    "reviewerName": "Krishna Nair",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 2,
    "productId": 202,
    "reviewerName": "Diya Sharma",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 2,
    "productId": 202,
    "reviewerName": "Aadhya Rao",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 2,
    "productId": 202,
    "reviewerName": "Reyansh Iyer",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 2,
    "productId": 202,
    "reviewerName": "Ishaan Roy",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 2,
    "productId": 203,
    "reviewerName": "Saanvi Singh",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 2,
    "productId": 203,
    "reviewerName": "Kiara Desai",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 2,
    "productId": 203,
    "reviewerName": "Vivaan Shah",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 2,
    "productId": 203,
    "reviewerName": "Saanvi Singh",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 2,
    "productId": 203,
    "reviewerName": "Tanya Menon",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 2,
    "productId": 204,
    "reviewerName": "Ishaan Roy",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 2,
    "productId": 204,
    "reviewerName": "Kiara Desai",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 2,
    "productId": 204,
    "reviewerName": "Arjun Reddy",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 2,
    "productId": 204,
    "reviewerName": "Myra Das",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 2,
    "productId": 204,
    "reviewerName": "Aadhya Rao",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 2,
    "productId": 205,
    "reviewerName": "Vivaan Shah",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 2,
    "productId": 205,
    "reviewerName": "Kiara Desai",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 2,
    "productId": 205,
    "reviewerName": "Arjun Reddy",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 2,
    "productId": 205,
    "reviewerName": "Reyansh Iyer",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 2,
    "productId": 205,
    "reviewerName": "Vivaan Shah",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 2,
    "productId": 206,
    "reviewerName": "Aarav Mehta",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 2,
    "productId": 206,
    "reviewerName": "Aarav Mehta",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 2,
    "productId": 206,
    "reviewerName": "Saanvi Singh",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 2,
    "productId": 206,
    "reviewerName": "Meera Nambiar",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 2,
    "productId": 206,
    "reviewerName": "Meera Nambiar",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 2,
    "productId": 207,
    "reviewerName": "Aarav Mehta",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 2,
    "productId": 207,
    "reviewerName": "Vivaan Shah",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 2,
    "productId": 207,
    "reviewerName": "Myra Das",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 2,
    "productId": 207,
    "reviewerName": "Myra Das",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 2,
    "productId": 207,
    "reviewerName": "Myra Das",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 3,
    "productId": 301,
    "reviewerName": "Krishna Nair",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 3,
    "productId": 301,
    "reviewerName": "Arjun Reddy",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 3,
    "productId": 301,
    "reviewerName": "Reyansh Iyer",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 3,
    "productId": 301,
    "reviewerName": "Pari Kapoor",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 3,
    "productId": 301,
    "reviewerName": "Rohan Malhotra",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 3,
    "productId": 302,
    "reviewerName": "Ananya Gupta",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 3,
    "productId": 302,
    "reviewerName": "Diya Sharma",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 3,
    "productId": 302,
    "reviewerName": "Aditya Joshi",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 3,
    "productId": 302,
    "reviewerName": "Arjun Reddy",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 3,
    "productId": 302,
    "reviewerName": "Saanvi Singh",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 3,
    "productId": 303,
    "reviewerName": "Rohan Malhotra",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 3,
    "productId": 303,
    "reviewerName": "Tanya Menon",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 3,
    "productId": 303,
    "reviewerName": "Kiara Desai",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 3,
    "productId": 303,
    "reviewerName": "Krishna Nair",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 3,
    "productId": 303,
    "reviewerName": "Reyansh Iyer",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 3,
    "productId": 304,
    "reviewerName": "Meera Nambiar",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 3,
    "productId": 304,
    "reviewerName": "Arjun Reddy",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 3,
    "productId": 304,
    "reviewerName": "Aarav Mehta",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 3,
    "productId": 304,
    "reviewerName": "Ananya Gupta",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 3,
    "productId": 304,
    "reviewerName": "Meera Nambiar",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 3,
    "productId": 305,
    "reviewerName": "Meera Nambiar",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 3,
    "productId": 305,
    "reviewerName": "Vihaan Patel",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 3,
    "productId": 305,
    "reviewerName": "Kiara Desai",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 3,
    "productId": 305,
    "reviewerName": "Rohan Malhotra",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 3,
    "productId": 305,
    "reviewerName": "Saanvi Singh",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 3,
    "productId": 306,
    "reviewerName": "Ananya Gupta",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 3,
    "productId": 306,
    "reviewerName": "Krishna Nair",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 3,
    "productId": 306,
    "reviewerName": "Kiara Desai",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 3,
    "productId": 306,
    "reviewerName": "Vivaan Shah",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 3,
    "productId": 306,
    "reviewerName": "Diya Sharma",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 3,
    "productId": 307,
    "reviewerName": "Rohan Malhotra",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 3,
    "productId": 307,
    "reviewerName": "Kunal Verma",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 3,
    "productId": 307,
    "reviewerName": "Aarav Mehta",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 3,
    "productId": 307,
    "reviewerName": "Kiara Desai",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 3,
    "productId": 307,
    "reviewerName": "Ishaan Roy",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 4,
    "productId": 401,
    "reviewerName": "Rohan Malhotra",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 4,
    "productId": 401,
    "reviewerName": "Aarav Mehta",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 4,
    "productId": 401,
    "reviewerName": "Pari Kapoor",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 4,
    "productId": 401,
    "reviewerName": "Krishna Nair",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 4,
    "productId": 401,
    "reviewerName": "Aarav Mehta",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 4,
    "productId": 402,
    "reviewerName": "Aditya Joshi",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 4,
    "productId": 402,
    "reviewerName": "Aarav Mehta",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 4,
    "productId": 402,
    "reviewerName": "Ananya Gupta",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 4,
    "productId": 402,
    "reviewerName": "Ananya Gupta",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 4,
    "productId": 402,
    "reviewerName": "Saanvi Singh",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 4,
    "productId": 403,
    "reviewerName": "Myra Das",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 4,
    "productId": 403,
    "reviewerName": "Arjun Reddy",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 4,
    "productId": 403,
    "reviewerName": "Kunal Verma",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 4,
    "productId": 403,
    "reviewerName": "Krishna Nair",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 4,
    "productId": 403,
    "reviewerName": "Pari Kapoor",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 4,
    "productId": 404,
    "reviewerName": "Tanya Menon",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 4,
    "productId": 404,
    "reviewerName": "Kunal Verma",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 4,
    "productId": 404,
    "reviewerName": "Aditya Joshi",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 4,
    "productId": 404,
    "reviewerName": "Tanya Menon",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 4,
    "productId": 404,
    "reviewerName": "Diya Sharma",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 4,
    "productId": 405,
    "reviewerName": "Ishaan Roy",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 4,
    "productId": 405,
    "reviewerName": "Meera Nambiar",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 4,
    "productId": 405,
    "reviewerName": "Ananya Gupta",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 4,
    "productId": 405,
    "reviewerName": "Ishaan Roy",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 4,
    "productId": 405,
    "reviewerName": "Kunal Verma",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 4,
    "productId": 406,
    "reviewerName": "Ananya Gupta",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 4,
    "productId": 406,
    "reviewerName": "Pari Kapoor",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 4,
    "productId": 406,
    "reviewerName": "Ira Bhattacharya",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 4,
    "productId": 406,
    "reviewerName": "Pari Kapoor",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 4,
    "productId": 406,
    "reviewerName": "Vivaan Shah",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 4,
    "productId": 407,
    "reviewerName": "Aadhya Rao",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 4,
    "productId": 407,
    "reviewerName": "Ira Bhattacharya",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 4,
    "productId": 407,
    "reviewerName": "Aditya Joshi",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 4,
    "productId": 407,
    "reviewerName": "Pari Kapoor",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 4,
    "productId": 407,
    "reviewerName": "Meera Nambiar",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 5,
    "productId": 501,
    "reviewerName": "Ishaan Roy",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 5,
    "productId": 501,
    "reviewerName": "Tanya Menon",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 5,
    "productId": 501,
    "reviewerName": "Vivaan Shah",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 5,
    "productId": 501,
    "reviewerName": "Aadhya Rao",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 5,
    "productId": 501,
    "reviewerName": "Krishna Nair",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 5,
    "productId": 502,
    "reviewerName": "Kunal Verma",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 5,
    "productId": 502,
    "reviewerName": "Aditya Joshi",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 5,
    "productId": 502,
    "reviewerName": "Meera Nambiar",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 5,
    "productId": 502,
    "reviewerName": "Meera Nambiar",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 5,
    "productId": 502,
    "reviewerName": "Ira Bhattacharya",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 5,
    "productId": 503,
    "reviewerName": "Vivaan Shah",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 5,
    "productId": 503,
    "reviewerName": "Vihaan Patel",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 5,
    "productId": 503,
    "reviewerName": "Ira Bhattacharya",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 5,
    "productId": 503,
    "reviewerName": "Ishaan Roy",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 5,
    "productId": 503,
    "reviewerName": "Tanya Menon",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 5,
    "productId": 504,
    "reviewerName": "Reyansh Iyer",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 5,
    "productId": 504,
    "reviewerName": "Reyansh Iyer",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 5,
    "productId": 504,
    "reviewerName": "Aditya Joshi",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 5,
    "productId": 504,
    "reviewerName": "Rohan Malhotra",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 5,
    "productId": 504,
    "reviewerName": "Aadhya Rao",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 5,
    "productId": 505,
    "reviewerName": "Aditya Joshi",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 5,
    "productId": 505,
    "reviewerName": "Ananya Gupta",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 5,
    "productId": 505,
    "reviewerName": "Ananya Gupta",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 5,
    "productId": 505,
    "reviewerName": "Vihaan Patel",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 5,
    "productId": 505,
    "reviewerName": "Ira Bhattacharya",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 5,
    "productId": 506,
    "reviewerName": "Ishaan Roy",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 5,
    "productId": 506,
    "reviewerName": "Arjun Reddy",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 5,
    "productId": 506,
    "reviewerName": "Ishaan Roy",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 5,
    "productId": 506,
    "reviewerName": "Kiara Desai",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 5,
    "productId": 506,
    "reviewerName": "Aarav Mehta",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 5,
    "productId": 507,
    "reviewerName": "Aadhya Rao",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 5,
    "productId": 507,
    "reviewerName": "Tanya Menon",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 5,
    "productId": 507,
    "reviewerName": "Reyansh Iyer",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 5,
    "productId": 507,
    "reviewerName": "Aadhya Rao",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 5,
    "productId": 507,
    "reviewerName": "Kunal Verma",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 6,
    "productId": 601,
    "reviewerName": "Kunal Verma",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 6,
    "productId": 601,
    "reviewerName": "Rohan Malhotra",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 6,
    "productId": 601,
    "reviewerName": "Rohan Malhotra",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 6,
    "productId": 601,
    "reviewerName": "Reyansh Iyer",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 6,
    "productId": 601,
    "reviewerName": "Meera Nambiar",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 6,
    "productId": 602,
    "reviewerName": "Arjun Reddy",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 6,
    "productId": 602,
    "reviewerName": "Tanya Menon",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 6,
    "productId": 602,
    "reviewerName": "Kiara Desai",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 6,
    "productId": 602,
    "reviewerName": "Krishna Nair",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 6,
    "productId": 602,
    "reviewerName": "Diya Sharma",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 6,
    "productId": 603,
    "reviewerName": "Reyansh Iyer",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 6,
    "productId": 603,
    "reviewerName": "Vihaan Patel",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 6,
    "productId": 603,
    "reviewerName": "Aadhya Rao",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 6,
    "productId": 603,
    "reviewerName": "Reyansh Iyer",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 6,
    "productId": 603,
    "reviewerName": "Pari Kapoor",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 6,
    "productId": 604,
    "reviewerName": "Ira Bhattacharya",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 6,
    "productId": 604,
    "reviewerName": "Krishna Nair",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 6,
    "productId": 604,
    "reviewerName": "Aadhya Rao",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 6,
    "productId": 604,
    "reviewerName": "Arjun Reddy",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 6,
    "productId": 604,
    "reviewerName": "Arjun Reddy",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 6,
    "productId": 605,
    "reviewerName": "Aditya Joshi",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 6,
    "productId": 605,
    "reviewerName": "Diya Sharma",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 6,
    "productId": 605,
    "reviewerName": "Diya Sharma",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 6,
    "productId": 605,
    "reviewerName": "Saanvi Singh",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 6,
    "productId": 605,
    "reviewerName": "Aditya Joshi",
    "review": "Absolutely loved it! Will buy again."
  },
  {
    "categoryId": 6,
    "productId": 606,
    "reviewerName": "Pari Kapoor",
    "review": "Fresh and delicious, great flavor."
  },
  {
    "categoryId": 6,
    "productId": 606,
    "reviewerName": "Kunal Verma",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 6,
    "productId": 606,
    "reviewerName": "Ishaan Roy",
    "review": "Convenient and easy to prepare."
  },
  {
    "categoryId": 6,
    "productId": 606,
    "reviewerName": "Vihaan Patel",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 6,
    "productId": 606,
    "reviewerName": "Tanya Menon",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 6,
    "productId": 607,
    "reviewerName": "Ananya Gupta",
    "review": "Tastes amazing, perfect for snacks."
  },
  {
    "categoryId": 6,
    "productId": 607,
    "reviewerName": "Vihaan Patel",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 6,
    "productId": 607,
    "reviewerName": "Reyansh Iyer",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 6,
    "productId": 607,
    "reviewerName": "Kiara Desai",
    "review": "Not worth the hype."
  },
  {
    "categoryId": 6,
    "productId": 607,
    "reviewerName": "Reyansh Iyer",
    "review": "Convenient and easy to prepare."
  }
]


@app.route('/add-all',methods=['POST'])
def addall():
    
    db.Products.insert_many(data)
        




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