# Predicting Dopamine Receptor Activity using Molecular Descriptors

An end-to-end machine learning pipeline for predicting **pEC50 values** of compounds targeting dopamine receptor subtypes (D1–D5) using molecular descriptors and regression modeling.

---

## Project Overview

This project builds a QSAR-style regression model to predict biological activity (pEC50) of chemical compounds acting on dopamine receptors. It analyzes structure–activity relationships (SAR) and identifies key molecular features influencing receptor potency.

---

## Objectives

- Predict continuous pEC50 values for dopamine receptor ligands  
- Analyze SAR across D1, D2, D3, D4, and D5 receptors  
- Study correlations between molecular descriptors and biological activity  
- Identify the most influential features affecting potency  

---

## Dataset Description

### Why This Dataset?

- Experimentally measured pEC50 values  
- Multiple dopamine receptor subtypes  
- Numerical and categorical molecular descriptors  
- No missing values  
- Suitable size for cross-validation  

### Key Columns

- pEC50 (target variable)  
- Receptor subtype  
- Assay type  
- Physicochemical descriptors (LogP, MW, TPSA, etc.)  
- Structural features (ring count, HBD, HBA)  

---

## Data Preprocessing

- CSV data loading  
- Standardized receptor subtype naming  
- Verified data integrity and ranges  
- Ensured descriptor formatting consistency  

---

## Exploratory Data Analysis

- pEC50 distribution inspection  
- Receptor-wise activity patterns  
- Descriptor–potency relationship analysis  

---

## Problem Definition

- Task: Regression  
- Input: Molecular descriptors + categorical features  
- Output: Predicted pEC50  
- Metrics: Mean Squared Error (MSE), R-squared (R²)  

---

## Feature Engineering

- Scaling of numerical features  
- One-Hot Encoding of categorical features  
- ColumnTransformer-based preprocessing  
- Pipeline-based transformation to avoid leakage  

---

## Model Selection

**Random Forest Regressor**

- Handles non-linear relationships  
- Robust to multicollinearity  
- Works with mixed feature types  
- Provides feature importance  
- Well-suited for QSAR tasks  

---

## Training and Validation

- Train / validation / test split  
- Cross-validation on training data  
- Fixed random seeds for reproducibility  
- Preprocessing included inside pipeline  

---

## Hyperparameter Tuning

- GridSearchCV optimization  
- Tuned number of estimators and depth  
- Model selected using CV MSE and R²  

---

## Model Evaluation

- Strong predictive performance  
- Unbiased residual distribution  
- Consistent trends across receptor subtypes  

---

## Feature Importance

Top contributing features:

- LogP  
- Molecular Weight  
- TPSA  
- Ring count  
- Receptor subtype encodings  

---

## Conclusions

- Reliable modeling of dopamine receptor activity achieved  
- Random Forest captures SAR effectively  
- Interpretable insights into molecular potency  
- Pipeline extensible to other GPCR families  

---

## Future Work

- Try gradient boosting and XGBoost  
- Apply deep learning methods  
- Add molecular fingerprints or graph features  
- Expand dataset using external sources  
- Train receptor-specific models  

---

## Authors

- Sneh Ajudiya – IC23BTECH11001  
- Sagnik Biswas – IC23BTECH11017  
- Sarvesh Goyal – IC23BTECH11019  
- Shubham Nare – IC23BTECH11020  
