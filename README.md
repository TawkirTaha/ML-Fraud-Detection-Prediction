<div align="center">

<img src="https://img.shields.io/badge/🛡️_FraudShield_AI-Live_Demo-00D4FF?style=for-the-badge" alt="FraudShield AI"/>

# 🛡️ FraudShield AI — ML Fraud Detection System

### Real-time transaction fraud detection powered by Machine Learning

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://fraud-detection-prediction-rd6iuvzbb3zswygtxgccet.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML_Pipeline-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Detection Rate](https://img.shields.io/badge/Detection_Rate-94%25-00CC88?style=for-the-badge&logo=checkmarx&logoColor=white)](https://github.com/TawkirTaha/ML-Fraud-Detection-Prediction)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br/>

> **Analyze financial transactions in real-time. Detect fraud with a single click.**

<br/>

![FraudShield Demo](https://fraud-detection-prediction-rd6iuvzbb3zswygtxgccet.streamlit.app/)

</div>

---

## 🌟 Live Demo

🔗 **[Click here to try the live app →](https://fraud-detection-prediction-rd6iuvzbb3zswygtxgccet.streamlit.app/)**

Enter any transaction details and instantly get a **Fraud Risk Score** with an animated result — no setup required.

---

## 📌 About The Project

**FraudShield AI** is an end-to-end machine learning project that detects fraudulent financial transactions in real-time. Built on the **PaySim financial dataset** (6.3M+ transactions), the system uses a trained **scikit-learn ML pipeline** exposed through a beautiful, interactive **Streamlit web app**.

This project covers the full data science lifecycle:

```
Data Exploration → Feature Engineering → Model Training → Evaluation → Deployment
```

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🎯 **94% Detection Rate** | High-accuracy fraud identification on real-world data |
| 🔍 **Real-time Prediction** | Instant fraud analysis on any transaction |
| 📊 **Risk Gauge** | Animated fraud probability score (0–100%) |
| 🚨 **Visual Alerts** | Pulsing red/green result cards with animation |
| 📋 **Transaction Summary** | Detailed breakdown of sender/receiver balance deltas |
| 🧠 **ML Pipeline** | Robust scikit-learn pipeline with preprocessing |
| 🌙 **Dark Mode UI** | Premium glassmorphism dark theme |
| ⚡ **Fast Inference** | Sub-100ms prediction latency |

---

## 🖥️ App Preview

<div align="center">

### 🟢 Legitimate Transaction
```
✅  TRANSACTION SAFE
No suspicious patterns detected. This transaction appears
to be legitimate and within normal parameters.
Risk Score: 4.5%
```

### 🔴 Fraudulent Transaction
```
🚨  FRAUD DETECTED
This transaction exhibits high-risk patterns consistent with
fraudulent activity. Immediate review is recommended.
Risk Score: 92.3%
```

</div>

---

## 🗂️ Dataset

| Property | Value |
|----------|-------|
| **Source** | PaySim — Mobile Money Fraud Simulation |
| **Records** | 6,362,620 transactions |
| **Fraud Rate** | ~0.13% (highly imbalanced) |
| **Model Detection Rate** | **94%** |
| **Size** | ~494 MB |
| **Storage** | GitHub LFS |

### Transaction Types

| Type | Description |
|------|-------------|
| `PAYMENT` | Customer paying a merchant |
| `TRANSFER` | Sending money to another customer |
| `CASH_OUT` | Withdrawing money via a merchant |
| `DEPOSIT` | Depositing money via a merchant |

### Features Used by Model

```python
features = [
    "type",           # Transaction type (categorical)
    "amount",         # Transaction amount
    "oldbalanceOrg",  # Sender's balance before
    "newbalanceOrig", # Sender's balance after
    "oldbalanceDest", # Receiver's balance before
    "newbalanceDest", # Receiver's balance after
]
```

---

## 🧠 Model Architecture

```
Input Features
     │
     ▼
┌─────────────────────────────┐
│     Scikit-learn Pipeline    │
│                             │
│  ┌─────────────────────┐   │
│  │  Column Transformer  │   │
│  │  • OneHotEncoder     │   │
│  │  • StandardScaler    │   │
│  └──────────┬──────────┘   │
│             │               │
│  ┌──────────▼──────────┐   │
│  │  Classifier          │   │
│  │  (Random Forest /    │   │
│  │   Decision Tree)     │   │
│  └─────────────────────┘   │
└─────────────────────────────┘
     │
     ▼
  0 = Legitimate ✅
  1 = Fraudulent 🚨
```

---

## 📁 Project Structure

```
ML-Fraud-Detection-Prediction/
│
├── 📓 Untitled.ipynb               # EDA & model training notebook
├── 🐍 fraud_detection_pipeline.py  # Original simple app
├── 🚀 app.py                       # Premium Streamlit app (deployed)
├── 🧠 fraud_detection_pipeline.pkl # Trained ML pipeline (joblib)
├── 📊 AIML Dataset.csv             # Training data (via Git LFS)
├── 📦 requirements.txt             # Python dependencies
├── 🎨 .streamlit/
│   └── config.toml                 # Streamlit dark theme config
├── 🙈 .gitignore                   # Git ignore rules
└── 📄 README.md                    # This file
```

---

## 🚀 Run Locally

### Prerequisites
- Python 3.9+
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/TawkirTaha/ML-Fraud-Detection-Prediction.git
cd ML-Fraud-Detection-Prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py
```

Open your browser at **http://localhost:8501** 🎉

---

## 📊 Exploratory Data Analysis

Key findings from the EDA notebook:

- 📈 **6,362,620** total transactions in the dataset
- 🚨 Only **8,213** (~0.13%) are fraudulent — highly imbalanced
- 🎯 Trained ML model achieves a **94% fraud detection rate**
- 🔍 Fraud predominantly occurs in **TRANSFER** and **CASH_OUT** types
- 💡 Key fraud signal: sender's new balance drops to **0** while amount was large
- ⚠️ `isFlaggedFraud` (system flag) only caught **16** out of 8,213 real fraud cases — vs **94%** by our model

---

## 🛠️ Tech Stack

<div align="center">

| Tool | Purpose |
|------|---------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat) | Core language |
| ![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white&style=flat) | Data manipulation |
| ![NumPy](https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white&style=flat) | Numerical computing |
| ![Scikit-learn](https://img.shields.io/badge/-Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white&style=flat) | ML pipeline |
| ![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?logo=python&logoColor=white&style=flat) | Visualizations |
| ![Seaborn](https://img.shields.io/badge/-Seaborn-76B900?logo=python&logoColor=white&style=flat) | Statistical plots |
| ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white&style=flat) | Web app framework |
| ![Plotly](https://img.shields.io/badge/-Plotly-3F4F75?logo=plotly&logoColor=white&style=flat) | Interactive charts |
| ![Git LFS](https://img.shields.io/badge/-Git_LFS-F05032?logo=git&logoColor=white&style=flat) | Large file storage |

</div>

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔃 Open a Pull Request

---

## 📬 Connect

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/tawkirtaha)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/TawkirTaha)

</div>

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">

Made with ❤️ by **Tawkir Taha**

⭐ **Star this repo** if you found it helpful!

[![Live App](https://img.shields.io/badge/🚀_Try_Live_App-Click_Here-00D4FF?style=for-the-badge)](https://fraud-detection-prediction-rd6iuvzbb3zswygtxgccet.streamlit.app/)

</div>
