from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np
import datetime,time
import streamlit.components.v1 as stc

model = load_model('house_pricing_model_01_15_2021')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():

    from PIL import Image
    # image = Image.open('Images\logo.png')
    image_sidebar = Image.open('renager.jpg')

    # st.image(image,use_column_width=False)
    st.sidebar.image(image_sidebar)  
    add_selectbox = st.sidebar.selectbox("Please select the option of your choice",("Home","About"))

    st.sidebar.info("This app is created to predict the price of an house, the dataset was curated by Renager data science team https://www.renager.com")
    
    
    stc.html("""
		<div style="background-color:#31333F;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">House pricing Prediction App</h1>
		</div>	""")
       

    # st.title("House pricing Prediction App")
    
    if add_selectbox == 'Home':
        # col1,col2= st.beta_columns(2)
        # with col1:
        Property_Type= st.selectbox('Category',['Flat', 'Serviced Residential Land', 'Self Contain Flat',
                                                    'Self Contain', 'Terraced Duplex House', 'Warehouse',
                                                    'Detached Duplex House', 'Mixed Use Land', 'Blocks Of Flats House',
                                                    'Event Centre Commercial Property', 'Residential Land',
                                                    'Detached Bungalow House', 'Penthouse Flat',
                                                    'Semi Detached Duplex House', 'House', 'Co Working Space',
                                                    'Semi Detached Bungalow House', 'Mini Flat', 'Office Space',
                                                    'Commercial Land', 'Studio Apartment Flat', 'Land',
                                                    'Shared Apartment Flat', 'Warehouse Commercial Property',
                                                    'Massionette House', 'Hotel/Guest House Commercial Property',
                                                    'Commercial Property', 'Shop Commercial Property',
                                                    'Show Room Commercial Property', 'School Commercial Property',
                                                    'Boys Quarters Flat', 'Shop In A Mall Commercial Property',
                                                    'Mini Flat Detached Bungalow House',
                                                    'Office Space Commercial Property', 'Hotel',
                                                    'Terraced Bungalow House', 'Tank Farm Commercial Property',
                                                    'Workstation Co Working Space', 'Church Commercial Property',
                                                    'Industrial Land', 'Mini Flat Commercial Property',
                                                    'Factory Commercial Property', 'Private Office Co Working Space',
                                                    'Mini Flat Studio Apartment Flat',
                                                    'Conference Room Co Working Space', 'Joint Venture Land'])
           
        Beds= st.selectbox('Number of Beds', [0,1,2,3,4,5,6,7,8,9,10])
            
        Baths= st.selectbox('Number of Bathroom', [0,1,2,3,4,5,6,7,8,9,10])
            
            
        # with col1:
        Toilets= st.selectbox('Number of toilet', [0,1,2,3,4,5,6,7,8,9,10])
            
        Property_attribute= st.selectbox('Property Type', ['SALE', ' SHORTLET', 'RENT'])
            
        State= st.selectbox('Loction by state', ['Lagos', 'Ogun', 'Enugu', 'Oyo', 'Abuja', 'Rivers', 'Anambra',
                                                    'Delta', 'Bayelsa', 'Kaduna', 'Kwara'])
                
        
        output=""

        input_dict = {
                        'Property_Type': Property_Type,
                        'Beds': Beds,
                        'Baths':Baths,
                        'Toilets':Toilets,
                        'Property_attribute':Property_attribute,
                        'State':State
                     }
        
        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output = '₦' + str(output)
        # with st.spinner("Predicting ..."):
        #     time.sleep(5)
        #     st.success('The Predicted Price is {}'.format(output))
        st.success('The predicted Price is: {}'.format(output))

    if add_selectbox == 'About':
        st.subheader("")

       
if __name__ == '__main__':
    run()