from anomaly_detection import AnomalyDetector
from batch_processing import batch_detect_and_store, load_file_data
from query_optimization import query_anomalies
import numpy as np

if __name__ == "__main__":
    # Initialize the anomaly detection model
    detector = AnomalyDetector()

    # Generate some dummy training data (replace with real non-stego samples)
    X_train = np.random.rand(100, 5)  # 100 samples, 5 features each
    detector.train(X_train)  # Train the One-Class SVM on clean data

    # Example input files
    files = ["file1.png", "file2.wav"]

    # Process each file: extract features, detect anomalies, and store metadata
    batch_detect_and_store(files, detector)

    # Query and print anomalies from the forensic database
    anomalies = query_anomalies(threshold=0.8)
    print("Detected anomalies:")
    for anomaly in anomalies:
        print(anomaly)
