from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

MONGO_URI="mongodb+srv://yash:yash@cluster0.bcuflio.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://yash:yash@cluster0.bcuflio.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo = PyMongo(app)








@app.route('/')
def index():
    return "Welcome to the Flask MongoDB API!"




@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    mongo.db.test_collection.insert_one(data)
    return jsonify({"message": "Data inserted successfully!"})








if __name__ == '__main__':
    app.run(debug=True)