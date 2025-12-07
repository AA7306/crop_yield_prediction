# crop_yield_prediction
#  Crop Yield Prediction System

A Machine Learning–based web application that predicts **agricultural crop yield** using environmental conditions, crop details, and farming practices.  
Built using **Linear Regression** and deployed with an interactive **Streamlit UI** for real-time predictions and decision support.


##  Features

- End-to-end Machine Learning pipeline  
- Linear Regression–based prediction model  
- Streamlit-powered web interface  
- Real-time crop yield prediction  
- Yield classification:
  -  Low Yield  
  -  Medium Yield  
  -  High Yield  
- Smart farming advisory feedback  
- Visual indicator for yield level  


##  Machine Learning Workflow

1. Dataset loading  
2. Missing value handling  
3. One-hot encoding of categorical features  
4. Feature selection  
5. Train–test split  
6. Model training using Linear Regression  
7. Model evaluation (R², MAE, RMSE)  
8. Prediction system  
9. Web application integration  
10. Live inference through UI  


##  Tech Stack

- **Language:** Python  
- **Libraries:**
  - pandas  
  - numpy  
  - scikit-learn  
  - matplotlib  
  - seaborn  
  - streamlit  
- **Model:** Linear Regression  
- **Frontend:** Streamlit Web UI  


##  Input Parameters

- Region  
- Soil Type  
- Crop Type  
- Rainfall (mm)  
- Temperature (°C)  
- Fertilizer Used (True / False)  
- Irrigation Used (True / False)  
- Weather Condition  
- Days to Harvest  


##  Output

- Predicted Crop Yield (tons / hectare)  
- Yield Category (Low / Medium / High)  
- Smart advisory message  
- Visual progress indicator  


##  Model Performance Metrics

- R² Score  
- Mean Absolute Error (MAE)  
- Root Mean Squared Error (RMSE)  

*(Exact values depend on the dataset used.)*


##  Project Structure

```text
crop_yield/
│
├── app.py                     # Streamlit web application
├── crop_yield_06_12_2025.py   # Model training & evaluation script
├── crop_yield_model.pkl      # Trained ML model
├── model_features.pkl        # Feature columns
├── yield_thresholds.pkl      # Yield classification thresholds
├── crop_yield.csv            # Dataset
└── README.md                 # Project documentation

```


## How to Run the Project Locally  
### Install Dependencies  
- pip install streamlit pandas numpy scikit-learn matplotlib seaborn

### Train the Model (Only Once)  
- python crop_yield_06_12_2025.py  
This will generate:
  - crop_yield_model.pkl
  - model_features.pkl


### Run the Web App  
- streamlit run app.py  


## Project Status  
This project is currently under iterative improvement.
Model sensitivity to categorical features and prediction accuracy are being optimized in future updates.  

## Author  
*Alen Alex Paul*








