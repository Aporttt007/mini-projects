from pymongo import MongoClient

# Connect to MongoDB instance
client = MongoClient("mongodb://localhost:27017/")
db = client["ForensicDB"]
collection = db["Media_Metadata"]

def store_metadata(file_id, features, anomaly_score, classification):
    """
    Stores extracted features and detection results in MongoDB.
    
    Parameters:
        file_id (str): Unique identifier of the file.
        features (dict): Extracted statistical features.
        anomaly_score (float): Detection confidence score.
        classification (str): 'stego' if anomalous, otherwise 'clean'.
    """
    document = {
        "file_id": file_id,
        "features": features,
        "anomaly_score": anomaly_score,
        "classification": classification
    }
    collection.insert_one(document)
