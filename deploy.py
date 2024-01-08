import pickle
import streamlit as st


st.set_page_config(layout="centered")

st.title("Classification and Prediction of Diabetes")
st.header("WQD7003: Data Analytics (APPLE)", divider="grey")
st.write("This is a draft model to help individuals to predict diabetes. must be aware of the limitations of such classification model, \
         and it is not intended to replace lab-based medical tests nor formal diagnosis by medical professionals.")

st.write("*********************************************************************************************************************")
st.write("The best model we achieved used for prediction here is \
         Support Vector Machine classifer. The data used to train our model was obtained from http://hbiostat.org/data courtesy of the \
         Vanderbilt University Department of Biostatistics.")
st.write("The summary of the result for our model is displayed as below: ")
st.write("Accuracy: 93.59%")
st.write("Precision: 78.57%")
st.write("Recall: 84.62%")
st.write("F1-Score: 81.48%")
st.write("ROC AUC Score: 0.90")

st.write("******************************************************************************************************************")

st.subheader("Please enter the following information as accurate as possible.")

chol = st.number_input("Cholesterol Level (mg/dL) ", value = None, placeholder="Type here...")
stab_glu = st.number_input("Stabilized Glucose (mg/dL)", value = None, placeholder="Type here...")
hdl = st.number_input("High Density Lipoprotein (mg/dL)",value = None, placeholder="Type here...")
ratio = 0
if (hdl != None):
    ratio = chol/hdl
age = st.number_input("Age", min_value=0, max_value=150)
weight = st.number_input("Weight (Pound)", min_value=0)
frame = 0
radio = st.radio(
    "What is your body frame size?",
    ["Small", "Medium", "Large"],
    index=None)

if radio == 'Small':
    frame = 0
elif radio == 'Medium':
    frame = 1
else:
    frame = 2

bp_1s = st.number_input("First Systolic Blood Pressure (mmHg)",value = None, placeholder="Type here...")
waist = st.number_input("Waist (Inches)", min_value=0)
hip = st.number_input("Hip (Inches)", min_value=0)


loaded_model = pickle.load(open('SVM_model.sav', 'rb'))

predTest = [[chol,stab_glu,hdl,ratio,age,weight,frame,bp_1s,waist,hip]]

if st.button("Predict"):
    result = loaded_model.predict(predTest)

    result = int(result)
    if (result == 1):
        print("This individual may have diabetes, please seek consultation from a medical professional soon.")
        st.write("This individual may have diabetes, please seek consultation from a medical professional soon.")
    elif (result == 0):
        print("This individual is not at risk of diabetes.")
        st.write("This individual is not at risk of diabetes.")
    else:
        print("Input Error!")
        st.write("Input Error!")


