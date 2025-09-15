"""
Airbnb Listings Analysis - Sample Queries
Author: Morgan Burch
Description:
This script demonstrates sample MongoDB queries for analyzing Airbnb listings.
All sensitive connection info has been removed. The queries were written for
educational and demonstration purposes using a sample dataset.
"""

import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pprint

# -----------------------------
# CONNECTION (SANITIZED)
# -----------------------------
# Replace with your MongoDB URI if running locally
MONGO_URI = "<YOUR_MONGO_URI>"
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

# Database and collection
db = client.sample_airbnb  # sample database
collection = db.listingsAndReviews  # sample collection

# -----------------------------
# QUERY 1: Accessibility & Size
# -----------------------------
# List properties that are waterfront or have a wide entryway/doorway
# Sort by number of beds descending and return top 5
proj1 = {"_id": 1, "name": 1, "property_type": 1, "beds": 1}

query1 = collection.find(
    {"$or": [
        {"amenities": "Wide doorway"},
        {"amenities": "Wide entryway"}
    ]},
    proj1
).sort("beds", -1).limit(5)

print("Query 1: Accessibility & Size")
for entry in query1:
    pprint.pprint(entry)
print("***********************************\n")

# -----------------------------
# QUERY 2: Top 5 Most Expensive Listings
# -----------------------------
proj2 = {"_id": 1, "name": 1, "price": 1}

query2 = collection.find({}, proj2).sort("price", -1).limit(5)

print("Query 2: Highest Priced Listings")
for entry in query2:
    pprint.pprint(entry)
print("***********************************\n")

# -----------------------------
# QUERY 3: Cleanliness > Location
# -----------------------------
proj3 = {
    "_id": 1,
    "name": 1,
    "bathrooms": 1,
    "review_scores.cleanliness": 1,
    "review_scores.location": 1
}

query3 = collection.find(
    {"$expr": {"$gt": ["$review_scores.cleanliness", "$review_scores.location"]}},
    proj3
).sort("bathrooms", -1).limit(5)

print("Query 3: Cleanliness Higher than Location")
for entry in query3:
    pprint.pprint(entry)
print("***********************************\n")

# -----------------------------
# QUERY 4: Most Reviewed Listings in Portugal
# -----------------------------
proj4 = {"_id": 1, "name": 1, "address.country": 1, "number_of_reviews": 1}

query4 = collection.find(
    {"address.country": "Portugal"}, proj4
).sort("number_of_reviews", -1).limit(5)

print("Query 4: Most Reviewed Listings in Portugal")
for entry in query4:
    pprint.pprint(entry)
print("***********************************\n")

# -----------------------------
# QUERY 5: High Review Count & Perfect Cleanliness
# -----------------------------
proj5 = {
    "_id": 1,
    "name": 1,
    "number_of_reviews": 1,
    "review_scores.cleanliness": 1
}

query5 = collection.find(
    {"$and": [
        {"$expr": {"$gt": [{"$size": "$reviews"}, 50]}},
        {"review_scores.cleanliness": 10}
    ]},
    proj5
).sort("number_of_reviews", -1).limit(5)

print("Query 5: High Reviews & Cleanliness")
for entry in query5:
    pprint.pprint(entry)
print("***********************************\n")

# -----------------------------
# QUERY 6: Top Hosts by Listings (<90% Response Rate)
# -----------------------------
proj6 = {
    "host.host_id": 1,
    "host.host_name": 1,
    "host.host_listings_count": 1,
    "host.host_response_rate": 1
}

query6 = collection.aggregate([
    {"$match": {"host.host_response_rate": {"$lt": 90}}},
    {"$group": {
        "_id": "$host.host_id",
        "host_name": {"$first": "$host.host_name"},
        "host_listings_count": {"$first": "$host.host_listings_count"},
        "host_response_rate": {"$first": "$host.host_response_rate"}
    }},
    {"$sort": {"host_listings_count": -1}},
    {"$limit": 5}
])

print("Query 6: Top Hosts with Large Portfolios & <90% Response Rate")
for entry in query6:
    pprint.pprint(entry)
print("***********************************\n")

# -----------------------------
# END OF FILE
# -----------------------------
