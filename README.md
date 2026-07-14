# 🏥 Disease Prediction from Medical Data

A Machine Learning-based web application that predicts the possibility of diseases using patient medical data. This project is developed using Python, Flask, and Scikit-learn as part of the **CodeAlpha Machine Learning Internship**.

---

## 📌 Project Objective

The objective of this project is to predict the likelihood of diseases based on structured medical data using classification algorithms. The application allows users to enter patient details and receive a prediction for:

- 🩸 Diabetes
- ❤️ Heart Disease
- 🎗️ Breast Cancer

---

## ✨ Features

- User Registration and Login
- Diabetes Prediction
- Heart Disease Prediction
- Breast Cancer Prediction
- Responsive Web Interface
- Machine Learning Model Integration
- SQLite Database for User Authentication
- Fast and Accurate Predictions

---

## 🛠️ Technologies Used

### Programming Language
- Python 3

### Machine Learning
- Scikit-learn
- XGBoost
- Joblib

### Web Framework
- Flask

### Database
- SQLite

### Frontend
- HTML5
- CSS3
- Bootstrap

### Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 📂 Project Structure

```
CodeAlpha_DiseasePrediction/
│
├── app.py
├── train_models.py
├── requirements.txt
├── README.md
├── database.db
│
├── datasets/
│   ├── diabetes.csv
│   ├── heart.csv
│   └── breast_cancer.csv
│
├── models/
│   ├── diabetes.pkl
│   ├── diabetes_scaler.pkl
│   ├── heart.pkl
│   ├── heart_scaler.pkl
│   ├── cancer.pkl
│   └── cancer_scaler.pkl
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── diabetes.html
│   ├── heart.html
│   ├── cancer.html
│   └── result.html
│
├── static/
│   ├── css/
│   │   └── style.css

---

## 📊 Datasets Used

### 1. Diabetes Prediction
- Pima Indians Diabetes Dataset

### 2. Heart Disease Prediction
- UCI Heart Disease Dataset

### 3. Breast Cancer Prediction
- Breast Cancer Wisconsin (Diagnostic) Dataset

---

## 🤖 Machine Learning Algorithms

The following classification algorithms were trained and evaluated:

- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest
- XGBoost

The best-performing model for each dataset is saved using Joblib and used by the Flask application.

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/CodeAlpha_DiseasePrediction.git
```

### Move to the project directory

```bash
cd CodeAlpha_DiseasePrediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Models

```bash
python train_models.py
```

This generates the trained model files in the **models/** folder.

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---


---

## 📈 Workflow

```
Medical Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Selection
        │
        ▼
Model Training
(Logistic Regression, SVM,
Random Forest, XGBoost)
        │
        ▼
Model Evaluation
        │
        ▼
Save Best Model
        │
        ▼
Flask Web Application
        │
        ▼
Disease Prediction
```

---

## 🚀 Future Enhancements

- Add Liver Disease Prediction
- Add Kidney Disease Prediction
- Add Parkinson's Disease Prediction
- Deploy the application using Render or Railway
- Add PDF report generation
- Display prediction probability
- Store prediction history

---

## 👨‍💻 Author

**Priyadharshini P**

MCA Student

Machine Learning Internship Project – CodeAlpha

---

## 📜 License

This project is developed for educational and internship purposes.

```
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.
```

---

## ⭐ Acknowledgements

- CodeAlpha
- UCI Machine Learning Repository
- Scikit-learn
- Flask
- XGBoost
- Pandas & NumPy
