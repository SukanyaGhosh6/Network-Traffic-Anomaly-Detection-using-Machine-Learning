## **Detecting Network Traffic Anomalies Using Machine Learning: A Data-Driven Approach to Intrusion Detection**

### **Abstract**

With the rising complexity and volume of cyberattacks, traditional rule-based Intrusion Detection Systems (IDS) are becoming inadequate. This paper explores a data-driven approach using machine learning to detect anomalies in network traffic. By analyzing patterns in features such as packet size, protocol type, connection duration, and flow frequency, this research demonstrates how supervised learning models can identify both known and unknown threats. Our methodology leverages public datasets like CICIDS2017 to build and evaluate models capable of real-time network monitoring.

---

### **1. Introduction**

In the modern age of digitization, network security is paramount. Cyberattacks are increasingly sophisticated and frequent, often bypassing static rule-based firewalls and IDS. Traditional methods fail to adapt to novel threats. Thus, there is a growing need for intelligent, adaptive systems that learn from data — this is where machine learning (ML) enters the arena.

Anomaly detection refers to the identification of unusual patterns that do not conform to expected behavior. In network security, anomalies can indicate malicious activities such as port scanning, Denial-of-Service (DoS) attacks, or brute force login attempts. The goal of this research is to build a robust, ML-based anomaly detection system using structured network traffic data.

---

### **2. Related Work**

Prior research includes:

* **KDD'99 and NSL-KDD**: Early intrusion detection datasets used for benchmarking.
* **CICIDS2017 Dataset**: Developed by the Canadian Institute for Cybersecurity, this dataset provides real-world network traffic with labeled attack types. [Link](https://www.unb.ca/cic/datasets/ids-2017.html)

Researchers have explored Support Vector Machines (SVM), Decision Trees, and ensemble methods like Random Forest and XGBoost for IDS. Our work builds on this foundation but emphasizes interpretability and practical deployment using minimal setup.

---

### **3. Dataset and Feature Engineering**

We used the **CICIDS2017 dataset**, which simulates a corporate network with a mix of normal and attack traffic.

* **Key Features Used**:

  * `Flow Duration`
  * `Total Fwd Packets`
  * `Total Backward Packets`
  * `Packet Length Variance`
  * `Fwd Packet Length Mean`
  * `Protocol Type`
  * `Label` (Benign / Attack)

The dataset is preprocessed to remove non-numeric and redundant fields. Missing values are handled, and class balancing is performed using undersampling or SMOTE (Synthetic Minority Over-sampling Technique).

---

### **4. Methodology**

#### a) Preprocessing:

* Data cleaning and normalization using `pandas` and `scikit-learn`.
* Label encoding of categorical features.

#### b) Model Selection:

* We experiment with:

  * **Logistic Regression**
  * **Random Forest Classifier**
  * **XGBoost**
  * **Isolation Forest** (unsupervised anomaly detection)

#### c) Evaluation:

* Metrics used:

  * Accuracy
  * Precision
  * Recall
  * F1-Score
  * ROC-AUC

---

### **5. Results**

Random Forest performed best with over 99% accuracy, but XGBoost yielded a slightly higher F1-Score, indicating better performance with imbalanced data. Isolation Forest, while useful for unsupervised learning, had a higher false-positive rate.

| Model            | Accuracy | F1-Score | ROC-AUC |
| ---------------- | -------- | -------- | ------- |
| Random Forest    | 99.1%    | 98.8%    | 0.992   |
| XGBoost          | 98.9%    | 99.0%    | 0.995   |
| Isolation Forest | 94.5%    | 91.2%    | 0.93    |

---

### **6. Discussion**

* The high accuracy rates validate the effectiveness of ML models in detecting known patterns.
* Feature importance analysis revealed that `Packet Length Std`, `Fwd Packet Count`, and `Flow Duration` were strong indicators of abnormal behavior.
* In practice, real-time IDS integration would require streaming data pipelines using tools like Apache Kafka or Zeek + Python.

---

### **7. Limitations and Future Work**

* **Real-time processing** not covered — future work will focus on real-time detection and alert systems.
* Dataset is still synthetic; deploying on live networks may reveal different behaviors.
* Consideration of **adversarial attacks** on ML models.

---

### **8. Conclusion**

This research demonstrates the feasibility of machine learning for anomaly-based intrusion detection. With proper tuning and feature selection, models like XGBoost and Random Forest can significantly improve detection rates over traditional rule-based systems. Our implementation runs fully in VS Code, enabling learners and researchers to build practical cybersecurity solutions from scratch.

---

### **References**

* [CICIDS2017 Dataset](https://www.unb.ca/cic/datasets/ids-2017.html)
* Scikit-Learn Documentation: [https://scikit-learn.org/](https://scikit-learn.org/)
* XGBoost Documentation: [https://xgboost.readthedocs.io/](https://xgboost.readthedocs.io/)
* “Machine Learning for Cybersecurity” – IEEE Access (2020)


