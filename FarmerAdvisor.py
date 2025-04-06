from phi.agent import Agent, RunResponse
from phi.model.ollama import Ollama
from ReadDataSet import readDataSet
from textwrap import dedent
from typing import List
from rich.pretty import pprint
from pydantic import BaseModel, Field
from typing import Iterator
from phi.utils.pprint import pprint_run_response

class FarmerAdvisor:

    def run_agent(self,soil_ph,soil_moisture,temperature,rainfall):

        FILE_PATH="C:/Users/hp/OneDrive/Desktop/Hackathon/Sustainable_farming/farmer_advisor_dataset.csv"
        data=readDataSet(FILE_PATH).to_dict()

        class FarmerSchema(BaseModel):
            ranking: List[str] = Field(description="Ranking suggested by agent.")
            justification: str = Field(description="The justification for the ranking")

        farmerAdvisor=Agent(
            name="Farmer Advisor",
            model=Ollama(id="llama3"),
            description="""You are a agronomist with 15+ years of expertise in sustainable farming in US. Advises farmers on optimal 
            crop choices based on soil pH, moisture, temperature, and rainfall, while minimizing the need for water, fertilizers, and 
            pesticides. Uses data-driven analysis and eco-conscious principles to recommend the most suitable and sustainable crops.""",
            instructions=[
                "Understand the data and analyze the input such as soil pH, soil moisture, temperature, and rainfall.",
                "Use the preloaded dataset to match crops based on environmental suitability.",
                "Once the analysis is done,provide with a list of  ranked crops [Wheat,Rice,Corn,Soyabean] in order maintain least water, fertilizers, and pesticides used.",
                "Strictly above providing extra information"
            ],
            markdown=True,
            show_tool_calls=True,
            agent_data=data,
            response_model=FarmerSchema,structured_outputs=True
        )
        question = f"I am a farmer my land soil ph is {soil_ph}, soil moisture is {soil_moisture}, temperature is {temperature}, rainfall in mm is {rainfall}. Taking this as input give me list of crops in order with fertilizers and pesticides used"
        
        farmer = farmerAdvisor.run(question).content
        return farmer