from pymongo.mongo_client import MongoClient
MONGO_URI="mongodb+srv://yash:yash@cluster0.bcuflio.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)

db=client["grade-eat"]
