## Project: Credit Card Fraud Detection

### Problem Statement
This project aims to develop a machine learning model capable of accurately predicting fraudulent credit card transactions. Given a dataset of credit card transactions, the goal is to identify patterns and anomalies indicative of fraudulent activity.

### Data Sources
* **Dataset:** A dataset containing credit card transactions.
* **Features:** The dataset typically includes features such as transaction amount, time, and various other attributes related to the transaction.

### Data Exploration and Preprocessing

* **During the EDA (Exploratory Data Analysis), it was noticed that:**
  * The dataset was massively imbalanced. There are more non-fraudulent transactions than there are fraudulent transactions.
  * There were only a few strong correlations between features. 
  * The ‘Amount’ feature has outliers. However, from domain knowledge we can infer that there are possibilities of amounts been outliers.
  * Certain features were way more important than others. 
  * A base model shows that without any feature engineering or data cleaning, we could have a particularly good accuracy score of 99%.

* **Data Cleaning:**
  * Here we first checked for missing values and noticed that there were no missing values. Next, we looked at the option of handling outliers. As earlier stated, because of the domain of the problem analyzed, credit card fraud, we can ascertain that there can be outliers. Removing such outliers can remove critical information from our data which will in turn affect the model performance. 
  
* **Class Imbalance:**
  * To handle imbalance, we used the imblearn.combine library from SMOTETomek Library. This employed a hybrid of undersampling and oversampling techniques to balance the dataset between the two available classes.

### Feature Engineering

* **Feature selection:** We reduced the dimension of our feature variables based on their feature importances.

### Model Selection and Training

* **Choose appropriate algorithms:** We employed RandomForestClassifier in creating our model. This algorithm was specifically chosen because of it's robustness towards outliers which our data had. 

### Code Structure and Documentation

* **Project Organization:** The zip file or github url provided has the below structure.
  * data folder:  containing the data file
  * models folder: containing the serialized model (.pkl file) 
  * notebooks foler: containing analysis file (EDA), cleaning (missing data and outliers) and modeling (data training and evaluation) notebooks.
  * visuals folder: containing plots from anayalsis done

### Running the Code

1. **unzip the file or download entire folder from github**
2. **Enter project foleder and create a virtual environment (python -m venv .venv)** 
3. **install requirements using : pip install -r requirements.txt** 
4. **download file from [https://kh3-ls-storage.s3.us-east-1.amazonaws.com/Updated%20Project%20guide%20data%20set/creditcard.csv] and move into data directory**


