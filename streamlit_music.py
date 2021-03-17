
import pickle
import streamlit as st
title_temp="""
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit Music Classification App </h2>
</div>
""" 
st.markdown(title_temp, unsafe_allow_html = True)

#image='image/images.jpeg'
#st.image(image,width=200)

text = st.text('Model Loading...')
#loading the train model

filename = 'models/model_gbc.pkl'

@st.cache
def load_model():
    classifier = pickle.load(open(filename, 'rb'))
    return classifier

classifier = load_model()
text.text('Model Loaded!')


#classifier.predict(test_features)
# #text.text(type(classifier))
 


@st.cache()
## defining the function which will make the prediction using the data which the user inputs
def prediction(bit_rate,duration,acousticness,danceability,energy,instrumentalness,liveness,speechiness,tempo,valence):

    prediction = classifier.predict([[bit_rate,duration,acousticness,danceability,energy,instrumentalness,liveness,speechiness,tempo,valence]])
    return prediction 

#this is main function define webpage
def main():
    
    # following lines create boxes in which user can enter data required to make prediction 
    st.sidebar.title("music classification Features")
    bit_rate=st.sidebar.slider('bit rate',-100,10000)
    duration=st.sidebar.slider('Duration',0,500)
    acousticness=st.sidebar.slider('Acousticness',-10,100)
    danceability=st.sidebar.slider('Danceability',-10,100)
    energy=st.sidebar.slider('Energy',-10,100)
    instrumentalness=st.sidebar.slider('instrumentalness',-100,100)
    liveness=st.sidebar.slider('liveness',-5,10)
    speechiness=st.sidebar.slider('speechiness',0,10)
    tempo=st.sidebar.slider('Tempo',0,500)
    valence=st.sidebar.slider('valence',0,10)
    result=""
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
            result = prediction(bit_rate,duration,acousticness,danceability,energy,instrumentalness,liveness,speechiness,tempo,valence) 
            st.success('Your music is {}'.format(result[0]))
            print("done")
     
if __name__=='__main__': 
    main()
