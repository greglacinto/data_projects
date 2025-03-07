# Credit Card Fraud Analysis and Prediction

## Description
Digital payments are evolving, but so are cyber criminals. According to the Data Breach Index, more than 5 million records are being stolen on a daily basis, a concerning statistic that shows - fraud is still very common both for Card-Present and Card-not Present type of payments.


## Dataset
-  [https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud](https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud)

## Requirements
- Python 3.5+
- Numpy
- Pandas
- Seaborn
- Mathplotlib
- sklearn
- imblearn
- pickle

## Summary of work
Using the data, we analyzed factors that correlated with credit card transactions being fraudulent, and did some exploratory visualization and analysis.  We then created a model that predicts the chance that a credit card transaction is Fraudulent or not.  This model could be useful for financial business owners.  You can see the exploratory data analysis in the `analysis.ipynb` notebook above.  

The model `pred_fraud_model.pkl` can be tested locally using the python script `credit_card_fraud_app.py` also seen above.