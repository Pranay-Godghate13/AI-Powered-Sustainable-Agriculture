import streamlit as st
from Distributor import Distributor
from Coordinator import Coordinator
import sqlite3

st.title("FieldConnect")
st.caption("Where Data Meets Dirt. Grow Smarter, Sell Smarter.")

distributor = Distributor()
coordinator = Coordinator()

connection = sqlite3.connect('C:/Users/hp/OneDrive/Desktop/Agriculture_database.db',check_same_thread=False)

# Create the table if it doesn't exist
connection.execute('''
    CREATE TABLE IF NOT EXISTS Data (
        
        location TEXT,
        soil_type TEXT,
        crops TEXT,
        goals TEXT,
        feedback TEXT,
        comments TEXT
    );
''')


def stream_data():
    for word in answer.split(" "):
        yield word + " "


location = st.text_input(label = "Location",placeholder="eg.: Nagpur, Guntur etc...")
if location:
    soil_type = st.selectbox(label="Soil Type",options = ["Sandy", "Clay","Slit","Loamy","Peaty","Saline","Black","Red","Chalky","Others"])
    if soil_type == "Others":
        soil_type = st.text_input(label = "Soil Type",placeholder="Provide the solid type here...")
    if soil_type:
        options = ['Wheat', 'Rice', 'Corn', 'Soybean']
        crop_preferences= st.multiselect("Choose crops you're interested in:",options)
        print(crop_preferences)
        if crop_preferences:
            financial_goals = st.text_input(label="Provide use with your financial goals:",placeholder="e.g: Get maximum returns, give minimum losses")
            if financial_goals:
                
                with st.spinner(text = "Processing...", show_time=True):

                    soil_pH_clean,soil_moisture_clean,temperature_clean,rainfall_clean,farmer_advices, market_advices = distributor.run_agent(location,soil_type,financial_goals)
                
                st.markdown("### Based on the location and soil type provided, we understood that")
                st.markdown(f"🌧 Rainfall in {location}: {rainfall_clean}")
                st.markdown(f"🌡 Temperature at {location}: {temperature_clean}")
                st.markdown(f"🌱 Soil pH of {soil_type} soil: {soil_pH_clean}")
                st.markdown(f"💧 Soil Moisture of {soil_type}: {soil_moisture_clean}")
                # If crop_preferences is a list like ['Wheat', 'Corn', 'Rice']
                crop_preferences_str = ", ".join(crop_preferences)

                if farmer_advices and market_advices:
                    with st.spinner(text = "Thinking...", show_time=True):
                        answer = coordinator.run_agent(farmer_advices, market_advices, financial_goals,crop_preferences)
                        # st.write(type(answer))
                        with st.container():
                            st.write_stream(stream_data)

                        col1, col2 = st.columns([1, 6])
                        feedback = None
                        with col1:
                            if st.button("👍 Yes"):
                                    feedback = "positive"
                        with col2:
                            if st.button("👎 No",):
                                    feedback = "negative"

                        while feedback != None:
                            # Show result
                            comments="No comments"
                            if feedback == "positive":
                                st.success("Thanks for the thumbs up! 😊")
                            if feedback == "negative":
                                st.error("Thanks for your feedback. Help us try to improve by your valuable comments! 🙏")
                                comments = st.text_input(label="Comments",placeholder="Please add you comments here...",label_visibility="collapsed")
                                if comments !=None:
                                    st.write(comments)
                                    st.success("Thank you for your comments! 😊")
                            
                            query = "INSERT INTO Data VALUES (?, ?, ?, ?, ?, ?)"
                            connection.execute(query, (location, soil_type, crop_preferences_str, financial_goals, feedback, comments))

                            # Commit changes
                            connection.commit()
