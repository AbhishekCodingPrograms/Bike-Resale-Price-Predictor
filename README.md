# 🏍️ Bike Resale Price Predictor

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.56.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8.0-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Predict the resale price of a used bike in seconds using Machine Learning.**

[🚀 Live Demo](#) • [📊 Dataset](#dataset) • [🛠️ Installation](#installation) • [📸 Screenshots](#screenshots)

</div>

---

## 📌 Overview

The **Bike Resale Price Predictor** is an end-to-end machine learning web application that estimates the fair market resale value of a used bike. Simply enter a few details about the bike — brand, engine power, kilometers driven, age, and city — and the model instantly predicts its price.

Built with a **Random Forest Regressor** trained on **32,648 real-world bike listings** from across India, the app achieves highly accurate predictions for popular brands like Royal Enfield, Bajaj, Hero, Yamaha, Honda, and more.

---

## ✨ Features

- 🔮 **Instant Price Prediction** — Real-time estimates powered by a trained ML model
- 🏍️ **9 Major Brands Supported** — Bajaj, Hero, Honda, KTM, Royal Enfield, Suzuki, TVS, Yamaha, and others
- 🌆 **24 Indian Cities** — Delhi, Bangalore, Mumbai, Hyderabad, Pune, Chennai, and more
- 📊 **32,000+ Training Samples** — Robust model trained on a large real-world dataset
- ⚡ **Auto-Train Fallback** — Automatically retrains the model from CSV if `.pkl` files are missing
- 🖼️ **Brand Logo Display** — Shows the brand image alongside predictions
- 🌐 **Deployed on Streamlit Cloud** — Accessible from any browser, no installation needed

---

## 🖥️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend / UI** | Streamlit |
| **ML Model** | scikit-learn — Random Forest Regressor |
| **Data Processing** | Pandas, NumPy |
| **Preprocessing** | OneHotEncoder, StandardScaler, ColumnTransformer |
| **Serialization** | Pickle |
| **Deployment** | Streamlit Cloud |

---

## 📊 Dataset

| Property | Value |
|----------|-------|
| **File** | `Used_Bikes.csv` |
| **Rows** | 32,648 |
| **Features** | `bike_name`, `brand`, `city`, `kms_driven`, `age`, `power`, `owner` |
| **Target** | `price` (INR ₹) |
| **Source** | Scraped from Indian used-bike marketplaces |

### Feature Engineering
- Cities with low frequency are grouped into `"Other"`
- Brands with low frequency are grouped into `"Other"`
- Pipeline: `OrdinalEncoder → StandardScaler → RandomForestRegressor`

---

## 🚀 Installation & Local Setup

### Prerequisites
- Python 3.9+
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/AbhishekCodingPrograms/Bike-Resale-Price-Predictor.git
cd Bike-Resale-Price-Predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app will open at **http://localhost:8501** 🎉

> **Note:** If `bike_predictor_rf.pkl` is missing, the app will automatically retrain the model from `Used_Bikes.csv` on first launch (~60 seconds).

---

## 🎮 How to Use

1. **Open the app** in your browser
2. **Select Brand** — choose from the sidebar dropdown (e.g., Royal Enfield)
3. **Enter Kms Driven** — total kilometers the bike has been ridden
4. **Enter Power (CC)** — engine displacement in cubic centimeters
5. **Enter Age** — how many years old the bike is
6. **Select City** — the city where the bike is being sold
7. **Click "Predict Bike Price"** — the estimated resale price appears instantly!

---

## 📁 Project Structure

```
Bike-Resale-Price-Predictor/
│
├── app.py                  # Main Streamlit application
├── retrain_model.py        # Script to retrain and regenerate .pkl files
├── requirements.txt        # Python dependencies
├── Used_Bikes.csv          # Training dataset (32,648 records)
├── bike_predictor_rf.pkl   # Trained Random Forest model (serialized)
├── search.pkl              # Brand & city dropdown values
├── Procfile                # Deployment configuration
├── .gitignore              
│
└── images/                 # Brand logo images
    ├── Royal Enfield.jpg
    ├── bajaj.jpg
    ├── Hero.jpg
    ├── Honda.png
    ├── KTM.jpg
    ├── Suzuki.jpg
    ├── TVS.png
    ├── yamaha.png
    └── Other.jpg
```

---

## 🤖 Model Details

| Parameter | Value |
|-----------|-------|
| **Algorithm** | Random Forest Regressor |
| **n_estimators** | 100 |
| **Random State** | 42 |
| **Categorical Encoding** | OneHotEncoder (handle_unknown='ignore') |
| **Numerical Scaling** | StandardScaler |
| **Pipeline** | ColumnTransformer → RandomForest |

### Input Features Used for Prediction

| Feature | Type | Example |
|---------|------|---------|
| `brand` | Categorical | `Royal Enfield` |
| `kms_driven` | Numerical | `6100` |
| `power` | Numerical (CC) | `350` |
| `age` | Numerical (years) | `3` |
| `city` | Categorical | `Delhi` |

---

## 📸 Screenshots

> The app features a clean sidebar-based UI with brand images and price predictions displayed on the main panel.

| Sidebar Inputs | Prediction Result |
|---|---|
| Brand, KMs, Power, Age, City | Estimated Price in ₹ |

---

## 🔄 Retraining the Model

If you want to retrain the model (e.g., after updating the dataset):

```bash
python retrain_model.py
```

This will:
1. Load and preprocess `Used_Bikes.csv`
2. Train a new Random Forest model
3. Save updated `bike_predictor_rf.pkl` and `search.pkl`

---

## 🌐 Deployment

This app is deployed on **Streamlit Cloud**.

To deploy your own copy:
1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **"New app"** → connect your GitHub repo
4. Set **Main file path** to `app.py`
5. Click **Deploy!**

---

## 👨‍💻 Author

**Abhishek Maurya**

[![GitHub](https://img.shields.io/badge/GitHub-AbhishekCodingPrograms-181717?style=for-the-badge&logo=github)](https://github.com/AbhishekCodingPrograms)

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

<div align="center">

⭐ **If you found this project useful, please give it a star!** ⭐

</div>
