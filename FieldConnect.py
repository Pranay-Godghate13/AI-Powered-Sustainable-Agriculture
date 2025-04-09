
# import streamlit as st
# from Distributor import Distributor
# from Coordinator import Coordinator
# import sqlite3

# st.title("FieldConnect")
# st.caption("Where Data Meets Dirt. Grow Smarter, Sell Smarter.")

# distributor = Distributor()
# coordinator = Coordinator()

# connection = sqlite3.connect('C:/Users/hp/Documents/Database/Agriculture_database.db',check_same_thread=False,timeout=10)

# # Create the table if it doesn't exist
# connection.execute('''
#     CREATE TABLE IF NOT EXISTS Data (
        
#         location TEXT,
#         soil_type TEXT,
#         crops TEXT,
#         goals TEXT,
#         feedback TEXT,
#         answer TEXT
#     );
# ''')


# def stream_data():
#     for word in answer.split(" "):
#         yield word + " "


# location = st.text_input(label = "Location",placeholder="eg.: Nagpur, Guntur etc...")
# if location:
#     soil_type = st.selectbox(label="Soil Type",options = ["Sandy", "Clay","Slit","Loamy","Peaty","Saline","Black","Red","Chalky","Others"])
#     if soil_type == "Others":
#         soil_type = st.text_input(label = "Soil Type",placeholder="Provide the solid type here...")
#     if soil_type:
#         options = ['Wheat', 'Rice', 'Corn', 'Soybean']
#         crop_preferences= st.multiselect("Choose crops you're interested in:",options)
#         print(crop_preferences)
#         if crop_preferences:
#             financial_goals = st.text_input(label="Provide use with your financial goals:",placeholder="e.g: Get maximum returns, give minimum losses")
#             print(financial_goals)
#             if financial_goals:
                
#                 with st.spinner(text = "Processing...", show_time=True):

#                     soil_pH_clean,soil_moisture_clean,temperature_clean,rainfall_clean,farmer_advices, market_advices = distributor.run_agent(location,soil_type,financial_goals)
                
#                 st.markdown("### Based on the location and soil type provided, we understood that")
#                 st.markdown(f"🌧 Rainfall in {location}: {rainfall_clean}")
#                 st.markdown(f"🌡 Temperature at {location}: {temperature_clean}")
#                 st.markdown(f"🌱 Soil pH of {soil_type} soil: {soil_pH_clean}")
#                 st.markdown(f"💧 Soil Moisture of {soil_type}: {soil_moisture_clean}")
#                 # If crop_preferences is a list like ['Wheat', 'Corn', 'Rice']
#                 crop_preferences_str = ", ".join(crop_preferences)

#                 if farmer_advices and market_advices:
#                     st.session_state.answer = coordinator.run_agent(farmer_advices, market_advices, financial_goals, crop_preferences)
#                     # with st.spinner(text = "Thinking...", show_time=True):
#                     #     answer = coordinator.run_agent(farmer_advices, market_advices, financial_goals,crop_preferences)
#                     #     # st.write(type(answer))
#                     #     with st.container():
#                     #         st.write_stream(stream_data)
#                 # Handle feedback and comments
#                 # Save processed data in session state
                
#                 feedback = None
#                 comments = "No comments"  # Default value for comments

#                 col1, col2 = st.columns([1, 6])

#                 with col1:
#                     if st.button("👍 Yes"):
#                         feedback = "positive"

#                 with col2:
#                     if st.button("👎 No"):
#                         feedback = "negative"
#                         comments = st.text_input(label="Comments", placeholder="Please add your comments here...")
#                         if comments.strip():
#                             st.write(f"Your comment: {comments}")
#                             st.success("Thank you for your comments! 😊")

#                 # Ensure feedback is recorded and data is inserted
#                 if feedback:
#                     query = "INSERT INTO Data (location, soil_type, crops, goals, feedback, answer) VALUES (?, ?, ?, ?, ?, ?)"
#                     connection.execute(query, (location, soil_type, crop_preferences_str, financial_goals, feedback, answer))
#                     connection.commit()
#                     st.success("Your feedback has been recorded. Thank you! 😊")


#                 # col1, col2 = st.columns([1, 6])
#                 # feedback = None
                
#                 # # comments="No comments"
#                 # with col1:
#                 #         if st.button("👍 Yes",):
#                 #             feedback = "positive"
#                 # with col2:
#                 #     if st.button("👎 No",):
#                 #         feedback = "negative"
                        
#                 # if feedback=="positive":
#                 #     st.success("Thanks for the thumbs up! 😊")
#                 # elif feedback=="negative":
#                 #     st.info("Thanks for your feedback. Help us try to improve by your valuable comments! 🙏")
#                 #     comments = st.text_input(label="Comments", placeholder="Please add your comments here...")
#                 #     if comments.strip():
#                 #         st.write(f"Your comment: {comments}")
#                 #         st.success("Thank you for your comments! 😊")
                     

#                 #         # st.error("Thanks for your feedback. Help us try to improve by your valuable comments! 🙏")
#                 #         # comments = st.text_input(label="Comments",placeholder="Please add you comments here...")
#                 #         # if comments != "":
#                 #         #     comments=st.write(comments)
#                 #         #     st.success("Thank you for your comments! 😊")
                    
#                 # query = "INSERT INTO Data VALUES (?, ?, ?, ?, ?,?)"
#                 # connection.execute(query, (location, soil_type, crop_preferences_str, financial_goals, feedback,answer))

#                 #     # Commit changes
#                 # connection.commit()



import streamlit as st
from Distributor import Distributor
from Coordinator import Coordinator
import sqlite3

st.title("FieldConnect")
st.caption("Where Data Meets Dirt. Grow Smarter, Sell Smarter.")

# Initialize session state variables
if "data_processed" not in st.session_state:
    st.session_state.data_processed = False
if "answer" not in st.session_state:
    st.session_state.answer = ""
if "feedback" not in st.session_state:
    st.session_state.feedback = None
if "crop_preferences_str" not in st.session_state:
    st.session_state.crop_preferences_str = ""
if "location" not in st.session_state:
    st.session_state.location = ""
if "soil_type" not in st.session_state:
    st.session_state.soil_type = ""
if "financial_goals" not in st.session_state:
    st.session_state.financial_goals = ""
if "comments" not in st.session_state:  # Initialize comments
    st.session_state.comments = ""
distributor = Distributor()
coordinator = Coordinator()

connection = sqlite3.connect('C:/Users/hp/Documents/Database/Agriculture_database.db', check_same_thread=False, timeout=10)

# Create the table if it doesn't exist
connection.execute('''
    CREATE TABLE IF NOT EXISTS Data (
        location TEXT,
        soil_type TEXT,
        crops TEXT,
        goals TEXT,
        feedback TEXT,
        answer TEXT
    );
''')

# Input collection
location = st.text_input(label="Location", placeholder="eg.: Nagpur, Guntur etc...")
if location:
    st.session_state.location = location
    soil_type = st.selectbox(label="Soil Type", options=["Sandy", "Clay", "Slit", "Loamy", "Peaty", "Saline", "Black", "Red", "Chalky", "Others"])
    if soil_type == "Others":
        soil_type = st.text_input(label="Soil Type", placeholder="Provide the soil type here...")
    if soil_type:
        st.session_state.soil_type = soil_type
        options = ['Wheat', 'Rice', 'Corn', 'Soybean']
        crop_preferences = st.multiselect("Choose crops you're interested in:", options)
        if crop_preferences:
            st.session_state.crop_preferences_str = ", ".join(crop_preferences)
            financial_goals = st.text_input(label="Provide us with your financial goals:", placeholder="e.g.: Get maximum returns, give minimum losses")
            if financial_goals:
                st.session_state.financial_goals = financial_goals
                if not st.session_state.data_processed:
                    with st.spinner(text="Processing..."):
                        soil_pH_clean, soil_moisture_clean, temperature_clean, rainfall_clean, farmer_advices, market_advices = distributor.run_agent(
                            location, soil_type, financial_goals
                        )
                        st.markdown("### Based on the location and soil type provided, we understood that")
                        st.markdown(f"🌧 Rainfall in {location}: {rainfall_clean}")
                        st.markdown(f"🌡 Temperature at {location}: {temperature_clean}")
                        st.markdown(f"🌱 Soil pH of {soil_type} soil: {soil_pH_clean}")
                        st.markdown(f"💧 Soil Moisture of {soil_type}: {soil_moisture_clean}")

                        if farmer_advices and market_advices:
                            st.session_state.answer = coordinator.run_agent(
                                farmer_advices, market_advices, financial_goals, crop_preferences
                            )
                        st.session_state.data_processed = True

                if st.session_state.data_processed:
                    st.markdown("### Advice and Feedback")
                    st.write(st.session_state.answer)

                    col1, col2 = st.columns([1, 6])
                    with col1:
                        if st.button("👍 Yes"):
                            st.session_state.feedback = "positive"
                            st.session_state.comments = None  # Clear comments for "Yes"

                    with col2:
                        if st.button("👎 No"):
                            st.session_state.feedback = "negative"

                    # Always render the text input for comments if feedback is "negative"
                    if st.session_state.feedback == "negative":
                        st.session_state.comments = st.text_input(
                            label="Comments",
                            placeholder="Please add your comments here...",
                            key="comments_input"
                        )
                        if st.session_state.comments.strip():
                            st.write(f"Your comment: {st.session_state.comments}")
                            st.success("Thank you for your comments! 😊")
                            print(f"Comment entered: {st.session_state.comments}")

                    # Record feedback and comments in the database
                    if st.session_state.feedback:
                        query = "INSERT INTO Data (location, soil_type, crops, goals, feedback, comments, answer) VALUES (?, ?, ?, ?, ?, ?, ?)"
                        connection.execute(
                            query,
                            (
                                st.session_state.location,
                                st.session_state.soil_type,
                                st.session_state.crop_preferences_str,
                                st.session_state.financial_goals,
                                st.session_state.feedback,
                                st.session_state.comments,
                                st.session_state.answer
                            )
                        )
                        connection.commit()
                        st.success("Your feedback has been recorded. Thank you! 😊")
                        print(f"Feedback: {st.session_state.feedback}, Comment: {st.session_state.comments}")

                    # col1, col2 = st.columns([1, 6])
                    # with col1:
                    #     if st.button("👍 Yes"):
                    #         st.session_state.feedback = "positive"
                    # with col2:
                    #     if st.button("👎 No"):
                    #         st.session_state.feedback = "negative"
                    #         st.session_state.comments =st.text_input(label="Comments", placeholder="Please add your comments here...")
                    #         print(st.session_state.comments)
                    #         if st.session_state.comments.strip():
                    #             st.write(f"Your comment: {st.session_state.comments}")
                    #             st.success("Thank you for your comments! 😊")
                    #             print(f"{st.session_state.comments}")

                    # if st.session_state.feedback:
                    #     print(f"{st.session_state.comments}")
                    #     query = "INSERT INTO Data (location, soil_type, crops, goals, feedback, comments, answer) VALUES (?, ?, ?, ?, ?, ?, ?)"
                    #     connection.execute(
                    #         query,
                    #         (st.session_state.location, st.session_state.soil_type, st.session_state.crop_preferences_str,
                    #          st.session_state.financial_goals, st.session_state.feedback, st.session_state.comments,st.session_state.answer)
                    #     )
                    #     connection.commit()
                    #     st.success("Your feedback has been recorded. Thank you! 😊")
