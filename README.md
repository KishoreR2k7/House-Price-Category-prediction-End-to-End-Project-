## 🚀 Live Demo

Try the app online:  


## https://huggingface.co/spaces/KishoreR123/HousePricePrediction


# House Price Predictor

A simple machine learning web application that predicts the **price category** of a house based on **size (m²)**, **number of bedrooms**, and **location score**. The project uses a **Decision Tree Classifier** and is deployed with **Gradio** for interactive predictions.

---

## 🔹 Project Overview

The app predicts whether a house falls into one of the following categories:

- **Low**
- **Medium**
- **High**

**Dataset Features:**

1. `size_m2` – Size of the house in square meters  
2. `bedrooms` – Number of bedrooms  
3. `location_score` – Score representing location quality  
4. `price_category` – Target variable (Low/Medium/High)

---

## 📊 Exploratory Data Analysis

- No missing values in the dataset.  
- Correlation analysis performed using heatmaps.  
- Feature distributions visualized with KDE plots.  
---

## 🛠️ Features

- Input: Size (m²), Bedrooms, Location Score  
- Output: Predicted price category  
- Model: Decision Tree Classifier (max depth = 3)  
- Feature scaling with StandardScaler  

--- 

**App Screenshot:**

<img width="1919" height="788" alt="image" src="https://github.com/user-attachments/assets/523ffc49-bcc2-4003-9db5-c4d14a9abb83" />

---

## 💻 Installation

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/House-Price-Predictor.git
cd House-Price-Predictor
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Ensure the following files are present:

house_price_tree.csv (dataset)

model.plk (trained model)

scaler.plk (StandardScaler)

🧪 How to Run Locally
bash
Copy
Edit
python app.py
Open the local link (e.g., http://127.0.0.1:7860) in your browser

Enter the house details

Click Submit to get the predicted price category

📁 File Structure
bash
Copy
Edit
House-Price-Predictor/
│
├─ assets/                   # Screenshots and images
├─ house_price_tree.csv       # Dataset
├─ model_training.py          # Model training script
├─ app.py                     # Gradio web app
├─ model.plk                  # Trained Decision Tree model
├─ scaler.plk                 # Scaler
└─ README.md                  # Project documentation
⚡ Technologies Used
Python

pandas, numpy

scikit-learn (DecisionTreeClassifier, StandardScaler)

matplotlib, seaborn (EDA & visualizations)

Gradio (Web app interface)

📌 Notes
Make sure feature order in the app matches training features: size_m2, bedrooms, location_score

Model and scaler are loaded from pickle files (model.plk and scaler.plk)
