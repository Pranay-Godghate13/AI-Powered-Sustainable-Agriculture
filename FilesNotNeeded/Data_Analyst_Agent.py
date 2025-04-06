import os
from dotenv import load_dotenv
from pathlib import Path
from phi.agent import Agent
from phi.file.local.csv import CsvFile
from phi.model.ollama import Ollama
import streamlit as st
import json


cwd = Path(__file__).parent.resolve()
tmp = cwd.joinpath("tmp")
if not tmp.exists():
    tmp.mkdir(exist_ok=True, parents=True)

local_csv_path = "farmer_advisor_dataset.csv"

if not os.path.exists(local_csv_path):
    raise FileNotFoundError(f"The file {local_csv_path} does not exist.")


python_agent = Agent(
    model=Ollama(id="llama3"),
    semantic_model=json.dumps(
        {
            "tables": [
                {
                    "name": "farmer_advisor_dataset",
                    "description": "Contains information about rainfall, temperature, soil pH, soil moisture etc in farmer_advisor_dataset.",
                    "path": "C:/Users/hp/OneDrive/Desktop/Hackathon/Sustainable_farming/farmer_advisor_dataset.csv",
                }
            ]
        }
    ),
    markdown=True,
    show_tool_calls=True,
)


st.title("Farmer Agent - Chat with expert")  # App title

st.write("Welcome! Ask questions about the farmer dataset, and I’ll fetch the answers for you.")  # App description

question = st.text_area("Enter your question:", placeholder="e.g., Temperature, Soil moisture,Soil PH, Rainfall in mm")

if st.button("Run Flow"):
    if not question.strip():
        st.error("Please enter a valid question.")

    
    try:
        with st.spinner("Processing your question..."):  # Show a loading spinner
            response = python_agent.run(question)  # Run the agent with the user query
            print(response)
            st.markdown(response.content)  # Display the response in markdown format
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")  # Handle and display any errors



# agent = Agent(
#     model=Ollama(id="llama3")
# )

# # Get the response in a variable
# # run: RunResponse = agent.run("Share a 2 sentence horror story.")
# # print(run.content)

# # Print the response in the terminal
# agent.print_response("Share a 2 sentence horror story.")