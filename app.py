import streamlit as st
import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("CPP.pkl", "rb"))

st.title("Food Delivery Time Prediction")

distance = st.number_input("Distance (km)", min_value=0.0, value=5.0)
traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
time = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
vehicle = st.selectbox("Vehicle Type", ["Bike", "Scooter", "Car"])
prep_time = st.number_input("Preparation Time (min)", min_value=0, value=20)
experience = st.number_input("Courier Experience (years)", min_value=0, value=2)

traffic_dict = {"Low": 1, "Medium": 2, "High": 0}
time_dict = {"Morning": 2, "Afternoon": 0, "Evening": 1, "Night": 3}
vehicle_dict = {"Bike": 0, "Scooter": 2, "Car": 1}

if st.button("Predict Delivery Time"):
    data = pd.DataFrame([[distance,
                          traffic_dict[traffic],
                          time_dict[time],
                          vehicle_dict[vehicle],
                          prep_time,
                          experience]],
                        columns=[
                            "Distance_km",
                            "Traffic_Level",
                            "Time_of_Day",
                            "Vehicle_Type",
                            "Preparation_Time_min",
                            "Courier_Experience_yrs"
                        ])

    prediction = model.predict(data)

    st.success(f"Estimated Delivery Time: {prediction[0]:.2f} minutes")