#  Network Traffic Anomaly Detection using Machine Learning

##  Author: Sukanya Ghosh  
GitHub: [SukanyaGhosh6](https://github.com/SukanyaGhosh6)

---

##  Introduction

In the vast ocean of cyberspace, **data packets** are like digital couriers, transporting information across routers, switches, and firewalls. Most of this traffic follows routine patterns—browsing, video calls, API requests—but occasionally, there’s an anomaly: a probe, a ping, a DDoS surge, or worse, a subtle infiltration. These are **network anomalies**, and detecting them is the first line of defense in modern cybersecurity.

This project is my attempt to **demystify anomaly detection** in network traffic using **machine learning**. It's a self-guided research-backed implementation aimed at combining my knowledge of Python, algorithms, and cybersecurity. It’s designed to be educational, practical, and ready to scale.

---

##  Objective

The primary goal of this project is to build an **intelligent anomaly detection system** that:
- Processes structured network traffic data (e.g., from NSL-KDD or CICIDS datasets).
- Learns what “normal” traffic looks like.
- Flags traffic that doesn’t fit the pattern—possible threats like scanning, probing, brute-forcing, or flooding.

---

##  What is Network Traffic Anomaly Detection?

- **Normal Traffic**: Routine communication between devices. Has statistical and temporal patterns.
- **Anomaly**: Any deviation from these norms—sudden bursts, unexpected port access, malformed headers.
- **Why Detection Matters**: Signature-based IDS can miss novel attacks. ML-based systems generalize patterns and detect previously unseen threats.

We focus on **supervised learning** (binary classification), but the system can evolve into unsupervised techniques (Isolation Forests, Autoencoders) later.

---

##  Project Structure
```
network-anomaly-detection/
├── data/                  # Raw and preprocessed network traffic datasets (e.g., CICIDS2017)
├── scripts/               # Python scripts for preprocessing, training, and evaluation
│   ├── preprocess.py
│   ├── train_model.py
│   └── detect_anomaly.py
├── models/                # Trained machine learning models (e.g., .pkl or .joblib files)
├── utils/                 # Utility functions for feature engineering and metrics
├── results/               # Logs, plots, confusion matrices
├── README.md               # This file
|-- RESEARCH_REPORT.md      #Research Report      
├── requirements.txt       # All dependencies
└── main.py                # CLI-based execution entry point

```
---

##  Machine Learning Concepts

- **Feature Engineering**: Protocol types, service ports, packet durations are converted into numerical features.
- **Binary Classification**: The model learns to differentiate between `normal` and `attack`.
- **Evaluation Metrics**:
  - **Accuracy**: % of correctly predicted traffic.
  - **Recall**: Important to catch as many attacks as possible.
  - **F1 Score**: Balance between false positives and false negatives.

We use models like:
- `RandomForestClassifier`
- `LogisticRegression`
- `IsolationForest` (future scope for unsupervised anomaly detection)

---

##  Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SukanyaGhosh6/network-anomaly-detector.git
   cd network-anomaly-detector


2. **Create a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   

3. **Install required libraries**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the main pipeline**:

   ```bash
   python scripts/run_model.py
   ```

5. **Explore results** in your terminal or export predictions to CSV.

---

##  Dataset Info

You can use the **NSL-KDD**, **CICIDS 2017**, or simplified `.csv` datasets with the following typical columns:

* `duration`, `protocol_type`, `service`, `flag`, `src_bytes`, `dst_bytes`
* `count`, `srv_count`, `same_srv_rate`, etc.
* `label` → Binary (normal, anomaly)

Each row represents a connection or flow session.

---

##  Challenges Tackled

* Imbalanced dataset → Used class weights and sampling
* Categorical features → One-hot encoding and label encoding
* High dimensionality → Feature importance analysis with tree-based models
* Model saving → `joblib` used to persist models for deployment

---

##  Why This Project Matters

This project isn’t just a learning experiment—it’s a **security research prototype**. It mimics how real-world **Intrusion Detection Systems (IDS)** work, but with the added flexibility and intelligence of machine learning. For anyone interested in becoming a **Security Analyst**, **Threat Hunter**, or **Data Scientist in cybersecurity**, this project bridges the technical and conceptual.

---

##  Future Work

* Deploy in real-time using `scapy` or `pyshark` for packet sniffing.
* Use **Deep Learning** (LSTM/GRU) for temporal anomaly detection.
* Build a simple dashboard using Streamlit for visual alerts.
* Add adversarial testing to simulate evasion tactics.

---

##  References

* NSL-KDD dataset: [http://www.unb.ca/cic/datasets/nsl.html](http://www.unb.ca/cic/datasets/nsl.html)
* CICIDS 2017 dataset
* Hands-On ML with Scikit-Learn, Aurélien Géron
* MITRE ATT\&CK and OWASP Top 10

---

##  Contact

If you're a fellow nerd, learner, or enthusiast — let’s connect!
**GitHub**: [SukanyaGhosh6](https://github.com/SukanyaGhosh6)

---

> *"Cybersecurity isn’t just about firewalls; it’s about foresight. This project helped me build both."* – Sukanya Ghosh




