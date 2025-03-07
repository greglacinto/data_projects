# -*- coding: utf-8 -*-
"""
Created on Saturday Feb 10 20:54:00 2024

@author: gregory.odiase
"""

# -*- coding: utf-8 -*-
"""
Created on Saturday Feb 10 20:54:00 2024

@author: gregory.odiase
"""


import pickle
import streamlit as st 

pickle_in = open("pred_fraud_model.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_fraud(distance_from_home,distance_from_last_transaction,ratio_to_median_purchase_price,repeat_retailer,used_chip,used_pin_number,online_order):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: distance_from_home
        in: query
        type: number
        required: true
      - name: distance_from_last_transaction
        in: query
        type: number
        required: true
      - name: ratio_to_median_purchase_price
        in: query
        type: number
        required: true
      - name: repeat_retailer
        in: query
        type: number
        required: true
      - name: used_chip
        in: query
        type: number
        required: true
      - name: used_pin_number
        in: query
        type: number
        required: true
      - name: online_order
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[distance_from_home,distance_from_last_transaction,ratio_to_median_purchase_price,repeat_retailer,used_chip,used_pin_number,online_order]])
    print(prediction)
    return prediction



def main():
    st.title("Fraud Check")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Credit Card Fraud Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    distance_from_home = st.text_input("distance_from_home","Type Here")
    distance_from_last_transaction = st.text_input("distance_from_last_transaction","Type Here")
    ratio_to_median_purchase_price = st.text_input("ratio_to_median_purchase_price","Type Here")
    repeat_retailer = st.text_input("repeat_retailer","Type Here")
    used_chip = st.text_input("used_chip","Type Here")
    used_pin_number = st.text_input("used_pin_number","Type Here")
    online_order = st.text_input("online_order","Type Here")

    result=""
    if st.button("Predict"):
        result=predict_fraud(distance_from_home,distance_from_last_transaction,ratio_to_median_purchase_price,repeat_retailer,used_chip,used_pin_number,online_order)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    