from phi.agent import Agent,RunResponse
from phi.model.ollama import Ollama
from FarmerAdvisor import FarmerAdvisor
import MarketResearcher
from typing import Iterator, Self
from pydantic import BaseModel, Field
from typing import List


location={"location": "Jhansi"}
soil_type={"soil_type": "Clayey soil"}
# crop_prefrences=#String input
# financial_goals=#String input

class WeatherSchema(BaseModel):
        rainfall: str = Field(description="Aggregate Rainfall of given location in mm")
        temperature: str = Field(description="Temperature of given location in celius")

class AgricultureSchema(BaseModel):
        soil_pH: str = Field(description="soil pH of given soil type")
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
        "Temperature should be within range of 15 degree celcius and 35 degree celcius"
    ],
    markdown=True,
    show_tool_calls=True,
    agent_data=location,
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
        "Soil moisture should be within range of 10 to 50"
    ],
    markdown=True,
    show_tool_calls=True,
    agent_data=soil_type,
    response_model=AgricultureSchema,structured_outputs=True
)

question1=f"I am an weather agent provide me details of weather for given location {location}"
question2=f"I am an agriculture agent provide me details of soil for given location {soil_type}"
        
# weatherAgent: Iterator[RunResponse] = weatherAgent.run(question1)
# agriculturalAgent: Iterator[RunResponse] = agriculturalAgent.run(question2)

# weatherAgent.print_response(question1)
# agriculturalAgent.print_response(question2)


# Run the agents (structured outputs using response_model)
weather_response_iterator = weatherAgent.run(question1)
agriculture_response_iterator = agriculturalAgent.run(question2)

# Convert iterators to list to extract responses
weather_responses = list(weather_response_iterator)
agriculture_responses = list(agriculture_response_iterator)

# Each response is a tuple: (id, RunResponse)
_, weather_response = weather_responses[0]
_, agriculture_response = agriculture_responses[0]

# Now access structured outputs
rainfall = weather_response.rainfall
temperature = weather_response.temperature

soil_pH = agriculture_response.soil_pH
soil_moisture = agriculture_response.soil_moisture

print("🌧 Rainfall:", rainfall)
print("🌡 Temperature:", temperature)
print("🌱 Soil pH:", soil_pH)
print("💧 Soil Moisture:", soil_moisture)

temperature = weather_response.temperature
FarmerAdvisor.run(Self,soil_pH,soil_moisture,temperature,rainfall)