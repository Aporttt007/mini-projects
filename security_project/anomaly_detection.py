from sklearn.svm import OneClassSVM
import numpy as np

class AnomalyDetector:
    def __init__(self):
        """
        Initializes an anomaly detection model using One-Class SVM.
        """
        # The RBF kernel is used for non-linear separation.
        self.model = OneClassSVM(kernel="rbf", gamma=0.1, nu=0.05)
    
    def train(self, X_train):
        """
        Trains the One-Class SVM on normal (clean) data.
        
        Parameters:
            X_train (numpy array): Training data consisting of feature vectors.
        """
        self.model.fit(X_train)
    
    def detect_anomaly(self, features):
        """
        Predicts if the input data contains steganographic modifications.
        
        Parameters:
            features (dict): Extracted feature dictionary.
        
        Returns:
            bool: True if steganographic content is detected (anomaly), False otherwise.
        """
        feature_vector = np.array(list(features.values())).reshape(1, -1)
        score = self.model.decision_function(feature_vector)
        return score < 0  # Returns True if the score indicates an anomaly
