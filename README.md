# House Price Prediction using Machine Learning

## Project Overview

This project predicts house prices based on various property features such as location, size, number of bedrooms, bathrooms, construction quality, amenities, and other housing-related factors.

The objective is to build a machine learning model that can accurately estimate property prices and assist in data-driven real estate decision-making.

---

## Dataset Features

The dataset contains the following features:

- Location
- Size_sqft
- Bedrooms
- Bathrooms
- Year_Built
- Garage
- Nearby_Schools
- Crime_Rate
- Transport_Accessibility
- Green_Space_Availability
- Local_Amenities
- HOA_Fees
- Property_Tax
- Average_Income_Area
- Internet_Availability
- Electricity_Availability
- Construction_Quality

### Target Variable

- Property_Price

---

## Project Workflow

### 1. Data Preprocessing

- Handled missing values
- Removed duplicates
- Checked data types
- Performed feature engineering where required

### 2. Exploratory Data Analysis (EDA)

- Statistical summary
- Distribution analysis
- Correlation analysis
- Feature relationship visualization

### 3. Data Encoding

Categorical variables were converted into numerical format using:

- One-Hot Encoding

### 4. Feature Scaling

Numerical features were standardized using:

- StandardScaler

### 5. Model Building

- Linear Regression

### 6. Model Evaluation

Models were evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Jupyter Notebook

---

## Project Structure

```
House-Price-Prediction/
│
├── data/
│   └── house_price_dataset.csv
│
├── notebooks/
│   └── House_Price_Prediction.ipynb
│
├── models/
│   └── trained_model.pkl
│
├── scaler/
│   └── scaler.pkl
│
├── README.md
│
└── requirements.txt
```


## Results

The final model successfully predicts house prices based on property characteristics and achieves strong predictive performance on unseen data.

---


## Author

Saurabh Singh Bisht
