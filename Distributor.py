from phi.agent import Agent
from phi.model.ollama import Ollama
from FarmerAdvisor import FarmerAdvisor
from MarketResearcher import MarketResearcher
from pydantic import BaseModel, Field
import re


# location={"location": "Jhansi"}
# soil_type={"soil_type": "Clayey soil"}
# financial_goals = {"financial_goals": "max profits"}
# crop_prefrences=#String input
# financial_goals=#String input

def extract_number(value):
            match = re.search(r"[-+]?\d*\.\d+|\d+", value)
            return float(match.group()) if match else None

class Distributor:

    def __init__(self):
          return None
    
    def run_agent(self,location,soil_type,financial_goals):

        class WeatherSchema(BaseModel):
                rainfall: str = Field(description="Aggregate Rainfall of given location in mm")
                temperature: str = Field(description="Temperature of given location in celius")

        class AgricultureSchema(BaseModel):
                soil_pH: str = Field(description="soil pH value of given soil type")
                soil_moisture: str = Field(description="soil moisture in percentage for given soil type")

        weatherAgent=Agent(
            name="Weather Agent",
            model=Ollama(id="llama3"),
            description="You are an experienced weather expert with 15+ who have to provide accurate information on rainfall in mm and temperature in degree celcius for any given location",
            instructions=[
                "From the given location give me only aggregate rainfall and average aggregate temperature for next 3 months , both rainfall and temperature as single value",
                "The rainfall should be in mm and temperature should be in degree celcius units",
                "Make sure the data shared is accurate",
                "Rainfall in mm should be within range 50 mm to 300 mm",
                "Temperature should be within range of 15 degree celcius and 35 degree celcius", "Avoid sending None"
            ],
            markdown=True,
            show_tool_calls=True,
            agent_data={"location": location},
            response_model=WeatherSchema,structured_outputs=True
        )

        agriculturalAgent=Agent(
            name="Agricultural Agent",
            model=Ollama(id="llama3"),
            description="You are an experienced Agriculture expert with 15+ who have to provide accurate information on soil ph and soil moisture for given soil type",
            instructions=[
                "From the given soil type give me an exact soil ph in decimal and exact soil moisture in percentage for that soil type",
                "Make sure the data shared is accurate",
                "Don't send me values in range",
                "Soil moisture should be within range of 10 to 50","Avoid sending None."
            ],
            markdown=True,
            show_tool_calls=True,
            agent_data={"soil_type": soil_type},
            response_model=AgricultureSchema,structured_outputs=True
        )

        question1=f"I am an weather agent provide me details of weather for given location {location}"
        question2=f"I am an agriculture agent provide me details of soil for given location {soil_type}"


        # Run the agents (structured outputs using response_model)
        weather_response_iterator = weatherAgent.run(question1)
        agriculture_response_iterator = agriculturalAgent.run(question2)

        # Convert iterators to list to extract responses
        weather_responses = list(weather_response_iterator)
        agriculture_responses = list(agriculture_response_iterator)

        # Each response is a tuple: (id, RunResponse)
        _, weather_response = weather_responses[0]
        _, agriculture_response = agriculture_responses[0]
        print(agriculture_response)
        # Now access structured outputs
        rainfall = weather_response.rainfall
        temperature = weather_response.temperature
        # print(rainfall)
        # print(temperature)

        soil_pH = agriculture_response.soil_pH
        soil_moisture = agriculture_response.soil_moisture
        # print(soil_moisture)
        # print(soil_pH)

        rainfall_clean = extract_number(rainfall)
        temperature_clean = extract_number(temperature)
        soil_pH_clean = extract_number(soil_pH)
        soil_moisture_clean = extract_number(soil_moisture)
        if rainfall_clean == None:
               rainfall_clean = 175
        if temperature_clean == None:
               temperature_clean = 25
        if soil_pH_clean == None:
               soil_pH_clean = 6.5
        if soil_moisture_clean == None:
               soil_moisture_clean = 55

        print(f"Cleaned rainfall: {rainfall_clean}")
        print(f"Cleaned temperature: {temperature_clean}")
        print(f"Cleaned soil pH: {soil_pH_clean}")
        print(f"Cleaned soil moisture: {soil_moisture_clean}")

        farmer_agent = FarmerAdvisor()
        market_agent = MarketResearcher()

        farmer_advices = farmer_agent.run_agent(soil_pH_clean,soil_moisture_clean,temperature_clean,rainfall_clean)
        market_advices = market_agent.run_agent(financial_goals)

        return soil_pH_clean,soil_moisture_clean,temperature_clean,rainfall_clean,farmer_advices,market_advices
    
