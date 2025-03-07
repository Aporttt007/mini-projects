import numpy as np
from scipy.stats import entropy, kurtosis, skew

def extract_features(data):
    """
    Extracts statistical features from multimedia data.
    
    Parameters:
        data (numpy array): Pixel or frequency values of an image/audio file.
        
    Returns:
        dict: Extracted features including mean, variance, entropy, skewness, and kurtosis.
    """
    mean_val = np.mean(data)
    var_val = np.var(data)
    entropy_val = entropy(data, base=2)
    skewness_val = skew(data)
    kurtosis_val = kurtosis(data)
    
    return {
        "mean": mean_val,
        "variance": var_val,
        "entropy": entropy_val,
        "skewness": skewness_val,
        "kurtosis": kurtosis_val
    }
