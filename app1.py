import streamlit as st
from src.pipline.prediction_pipeline import VehicleData, VehicleDataClassifier


# Function to make predictions
def make_prediction(form_data):
    try:
        # Create VehicleData instance with the form data
        vehicle_data = VehicleData(
            Gender=form_data["Gender"],
            Age=form_data["Age"],
            Driving_License=form_data["Driving_License"],
            Region_Code=form_data["Region_Code"],
            Previously_Insured=form_data["Previously_Insured"],
            Annual_Premium=form_data["Annual_Premium"],
            Policy_Sales_Channel=form_data["Policy_Sales_Channel"],
            Vintage=form_data["Vintage"],
            Vehicle_Age_lt_1_Year=form_data["Vehicle_Age_lt_1_Year"],
            Vehicle_Age_gt_2_Years=form_data["Vehicle_Age_gt_2_Years"],
            Vehicle_Damage_Yes=form_data["Vehicle_Damage_Yes"],
        )

        # Convert form data into a DataFrame for the model
        vehicle_df = vehicle_data.get_vehicle_input_data_frame()

        # Initialize the prediction pipeline
        model_predictor = VehicleDataClassifier()

        # Make a prediction and retrieve the result
        value = model_predictor.predict(dataframe=vehicle_df)[0]

        # Interpret the prediction result as 'Response-Yes' or 'Response-No'
        status = "Response-Yes" if value == 1 else "Response-No"

        return status

    except Exception as e:
        st.error(f"Error: {e}")
        return None


# Streamlit UI for user input
st.title("Vehicle Insurance Prediction")

# Collect inputs from the user
st.header("Enter Vehicle Information")

# Create a dictionary to hold form data
form_data = {}

# Gender
form_data["Gender"] = st.selectbox(
    "Gender", [0, 1], key="gender_select"
)  # 0 for Male, 1 for Female

# Age
form_data["Age"] = st.number_input("Age", min_value=18, max_value=100, key="age_input")

# Driving License
form_data["Driving_License"] = st.selectbox(
    "Driving License", [0, 1], key="license_select"
)

# Region Code
form_data["Region_Code"] = st.number_input(
    "Region Code", min_value=1, key="region_input"
)

# Previously Insured
form_data["Previously_Insured"] = st.selectbox(
    "Previously Insured", [0, 1], key="insured_select"
)

# Annual Premium
form_data["Annual_Premium"] = st.number_input(
    "Annual Premium", min_value=0.0, key="premium_input"
)

# Policy Sales Channel
form_data["Policy_Sales_Channel"] = st.number_input(
    "Policy Sales Channel", min_value=0.0, key="policy_input"
)

# Vintage
form_data["Vintage"] = st.number_input("Vintage", min_value=0, key="vintage_input")

# Vehicle Age less than 1 year
form_data["Vehicle_Age_lt_1_Year"] = st.selectbox(
    "Vehicle Age less than 1 year", [0, 1], key="age_lt_1_select"
)

# Vehicle Age greater than 2 years
form_data["Vehicle_Age_gt_2_Years"] = st.selectbox(
    "Vehicle Age greater than 2 years", [0, 1], key="age_gt_2_select"
)

# Vehicle Damage (Yes/No)
form_data["Vehicle_Damage_Yes"] = st.selectbox(
    "Vehicle Damage (Yes/No)", [0, 1], key="damage_select"
)

# When the "Make Prediction" button is pressed, call the prediction function
if st.button("Make Prediction"):
    with st.spinner("Making prediction..."):
        result = make_prediction(form_data)
        if result:
            st.success(f"Prediction Result: {result}")
        else:
            st.error("Error in making prediction.")
