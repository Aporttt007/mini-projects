# Digital Forensic Stego-Detection

## Description
This project implements an anomaly-based steganographic detection system for digital forensic applications. It utilizes:
- **Feature Extraction:** Statistical measures (mean, variance, entropy, skewness, kurtosis) are extracted from multimedia files.
- **Anomaly Detection:** A hybrid approach using Convolutional Neural Networks (CNN) and One-Class SVMs to detect steganographic modifications.
- **Database Integration:** MongoDB is used for forensic storage and efficient query optimization.
- **Batch Processing:** Automates the detection and storage of anomalies for large-scale forensic analysis.

## Installation

### **1️⃣ Install Python & Virtual Environment**
1. Ensure **Python 3.8+** is installed. Check with:
   ```bash
   python --version
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

### **2️⃣ Install Dependencies**
Run:
```bash
pip install -r requirements.txt
```

### **3️⃣ Install & Configure MongoDB**
1. **Download & Install MongoDB** (Community Edition) from:
   - [MongoDB Official Download](https://www.mongodb.com/try/download/community)
2. **Add MongoDB to System PATH** (If not recognized):
   - Add `C:\Program Files\MongoDB\Server\8.0\bin` to your **system environment variables** under `Path`.
3. **Create Database Directory** (If not exists):
   ```bash
   mkdir C:\data\db
   ```
4. **Start MongoDB Server:**
   ```bash
   mongod --dbpath "C:\data\db"
   ```
5. **Verify MongoDB is Running:**
   ```bash
   mongo
   ```

### **4️⃣ Run the Project**
1. Ensure MongoDB is running.
2. Run the main script:
   ```bash
   python main.py
   ```

### **5️⃣ Query Anomalies from MongoDB (Optional)**
Retrieve detected anomalies:
```bash
python -c "from query_optimization import query_anomalies; print(query_anomalies(threshold=0.8))"
```

### **Troubleshooting**
✅ **MongoDB not recognized?** Add MongoDB `bin` folder to PATH.
✅ **Module not found?** Run `pip install -r requirements.txt` again.
✅ **Permission issues?** Run Command Prompt as **Administrator**.
✅ **MongoDB connection error?** Ensure MongoDB is running with `mongod --dbpath "C:\data\db"`.

## Project Structure
```
digital_forensic_stego/
├── feature_extraction.py   # Extracts statistical features from media files
├── anomaly_detection.py    # Implements CNN + One-Class SVM for anomaly detection
├── database.py             # MongoDB integration for forensic storage
├── batch_processing.py     # Automates large-scale forensic analysis
├── query_optimization.py   # Optimized forensic data retrieval
├── main.py                 # Main execution script
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

## Future Work
Future improvements include enhancing feature extraction, optimizing real-time detection using GPU acceleration, integrating advanced stego-resistant models, and exploring blockchain integration for forensic data integrity.

