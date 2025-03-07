from database import collection

def query_anomalies(threshold=0.8):
    """
    Retrieves files flagged as anomalies with high confidence.
    
    Parameters:
        threshold (float): Minimum anomaly score to filter results.
        
    Returns:
        list: Retrieved forensic records from MongoDB.
    """
    results = collection.find({"anomaly_score": {"$gt": threshold}})
    return list(results)
