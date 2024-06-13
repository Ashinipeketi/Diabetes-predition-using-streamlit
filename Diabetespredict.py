insulin=st.select_slider("insulin",options=range(0,846),value=70)
bmi=st.select_slider("BMI",options=range(0,67),value=20)
dpf=st.select_slider("Diabetes Pedigree Function",options=range(0,2),value=1)
age=st.select_slider("Age",options=range(21,88),value=33)
user_input=[[pregnancies,glucose,bp,skinthickness,insulin,bmi,dpf,age]]
user_input_scaled=scaler.transform(user_input)
st.write(str(accuracy_score(y_test,classifier.predict(x_test))*100)+'%')
prediction=classifier.predict(user_input_scaled)
if prediction==0:
    st.write('You are Healthy')
else:
    st.write('You are not Healthy')
