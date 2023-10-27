from flask import Flask, request, jsonify
from pymongo import MongoClient
import requests

app = Flask(__name__)

# MongoDB Configuration
mongo_client = MongoClient("mongodb://localhost:27017/")  # UMongoDB connection string
db = mongo_client["dictionary"]  # MongoDB database name
collection = db["wordscollection"]  # MongoDB collection name

# Dictionary API Endpoint
dictionary_api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"  # Dictionary API URL

@app.route('/search', methods=['GET'])
def query():
    query_string = request.args.get('word')

    # Check if the word is in MongoDB
    result = collection.find_one({"word": query_string})
    if result:
        response_data = result['result']
    else:
        # If not found in MongoDB, fetch data from the Dictionary API
        dict_api_response = requests.get(f"{dictionary_api_url}{query_string}")
        response_data = dict_api_response.json()

        # Save the response in MongoDB
        collection.insert_one({"word": query_string, "result": response_data})

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(port=8088)
