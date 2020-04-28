import streamlit as st
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')



def load_data(dataset):
    df = pd.read_csv(dataset)
    return df

Bedroom ={'1': 10, '2':2,'3':3,'4':4,'5':5,'6':6}
Bathrooms = {'1': 1, '2':2,'3':3,'4':4,'5':5,'6':6}
Toilets = {'1': 1, '2':2,'3':3,'4':4,'5':5,'6':6}
Totalrooms = {'1': 1, '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'11': 11, '12':12,
           '13':13,'14':14,'15':15,'16':16,'17':17,'18':18,'19':19,'20':20,
          '21': 21, '22':22,'23':23,'24':24,'25':25,'26':26,'27':27}
Typeofhouse = {'Yes':'1', 'No':'0'}


#Get the keys
def get_value(val, my_dict):
    for key, value in my_dict.items():
        if val == key:
            return str(value)

#Find the keys in the dictionary
def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key

#Load Model
# def load_pred(model_file):
#     loaded_model =  joblib.load("m")
modelz = joblib.load("filename.pkl")

def main():
    """Housing Ml App"""
    st.title("Housing Pricing App")
    st.subheader("Built with Streamlit") 
    st.subheader("This is a Demo, Thus accuracy is poor") 

    #menu
    menu = ["Prediction", "About"]
    choices = st.sidebar.selectbox("Select Activities",menu)

    if choices == 'Prediction':
        st.subheader("Prediction")
        Number_of_Bedrooms = st.sidebar.slider("Number of Bedrooms", 1,6)
        Total_rooms = st.sidebar.selectbox("Total Number of rooms",tuple(Totalrooms.keys()) )
        # Number_of_Bedrooms = st.selectbox("Number of Bedrooms",tuple(bedroom.keys()) )
        # Number_of_Bathrooms = st.selectbox("Number of Bathrooms",tuple(bathrooms.keys()) )
        Number_of_Bathrooms = st.sidebar.slider("Number of Bathrooms", 1,6)
        Number_of_Toilet = st.sidebar.selectbox("Number of Toilet",tuple(Toilets.keys()) )

        #estate_or_not = st.sidebar.selectbox("Do you want to live in an Estate",tuple(estate.keys()) )
        #locations = st.sidebar.selectbox("Your preferred location",tuple(location_rank.keys()) )
        terrace_or_not = st.sidebar.selectbox("Do you want to live in an Terracced Apartment",tuple(Typeofhouse.keys()) )
        #Number_of_flag = st.sidebar.selectbox("Do you prefer a new apartment",tuple(New_flag.keys()) )
        #exec_flagg1 = st.sidebar.selectbox("Do you prefer an executive apartment",tuple(exec_flag.keys()) )
        #serviced_flag1 = st.sidebar.selectbox("Do you prefer an serviced apartment",tuple(serviced_flag.keys()) )

        #Encoding
        #v_estate_or_not = get_value(estate_or_not,estate )
        #v_locations = get_value(locations,location_rank )        
        v_terrace_or_not = get_value(terrace_or_not, Typeofhouse)
        #v_Number_of_flag = get_value(Number_of_flag,New_flag )
        # v_exec_flagg1 = get_value(exec_flagg1,exec_flag )
        #v_serviced_flag1 = get_value(serviced_flag1,serviced_flag )

        predictor_data= [Number_of_Bedrooms,Number_of_Bathrooms,Number_of_Toilet,
        Total_rooms, v_terrace_or_not]
        predictor_data= np.array(predictor_data).reshape(1,-1)
        df = load_data('house.csv')

        if st.button("Evaluate"):
            
                    # st.write(z.new_price.max())
                    #b= z.new_price.max()
                    #c = z.new_price.min()
                    #d = int(c)
                    #e = int(b)
                    # st.write(e)
                    # st.write(data.new_price.min())
                    # x=['Yaba']
                    # plt.bar(x,e, bottom= d)
                    #data['price'][(data['location']=="yaba")&(data['bedrooms']==Number_of_Bathrooms)].plot(kind="hist")
                    #st.pyplot()
                    
                    #predicted = modelz.predict(predictor_data)
                    #predicted =  int(predicted)             
                    #st.write("The predicted price for this apartment in ", locations,"is",predicted)
                    #st.write("Maximum amount of apartment in ",locations, "is", e)
                    #st.write("Minimum amount of apartment in ",locations, "is", d)
                    
            
            
            #elif Number_of_Bedrooms ==8:
                # locations =='Yaba'
                #z= df.where(df['Bedroom']==8)
                # st.write(z.new_price.max())
                #b= z.new_price.max()
                #c = z.new_price.min()
                #d = int(c)
                #e = int(b)
                # st.write(e)
                # st.write(data.new_price.min())
                # x=['Yaba']
                # plt.bar(x,e, bottom= d)
                #data['price'][(data['location']=="yaba")&(data['bedrooms']==Number_of_Bathrooms)].plot(kind="hist")
                #st.pyplot()
                
                #predicted = modelz.predict(predictor_data)
                #predicted =  int(predicted)             
                #st.write("The predicted price for this apartment in ", locations,"is",predicted)
                #st.write("Maximum amount of apartment in ",locations, "is", e)
                #st.write("Minimum amount of apartment in ",locations, "is", d)    
            
            

            #else:
                
                #Number_of_Bedrooms ==8
                
                # locations =='Yaba'
                #z= df.where(df['Bedroom']==8)
                # st.write(z.new_price.max())
                #b= z.new_price.max()
                #c = z.new_price.min()
                #d = int(c)
                #e = int(b)
                # st.write(e)
                # st.write(data.new_price.min())
                # x=['Yaba']
                # plt.bar(x,e, bottom= d)
                #data['price'][(data['location']=="yaba")&(data['bedrooms']==Number_of_Bathrooms)].plot(kind="hist")
                #st.pyplot()
                
            predicted = modelz.predict(predictor_data)
            predicted =  int(predicted)             
                #st.write("The predicted price for this apartment in ", locations,"is",predicted)
            st.write("Maximum amount of apartment in ", "is", predicted)
                #st.write("Minimum amount of apartment in ", "is", d) 
        # st.write(v_estate_or_not  )
        # st.write(locations  )
        # st.write(v_terrace_or_not  )
        # st.write(v_Number_of_flag  )
        # st.write(v_serviced_flag1  )
        # st.write(Number_of_Bedrooms)

    if choices == 'About':
        st.subheader("About")



if __name__ == "__main__":
    main()