from typing import List
from pydantic import BaseModel, Field
from ReadDataSet import readDataSet
from phi.agent import Agent, RunResponse
from phi.model.ollama import Ollama
from typing import Iterator

class MarketResearcher:


    def run_agent(self, financial_goals):
        file_path = "https://docs.google.com/spreadsheets/d/1KbUSwYDEfzNZzeM3Kr4MOKvNO9-0XRPw8VAE_FsT-fI/export?format=csv&sheet=market_advisor_dataset"

        data = readDataSet(file_path).to_dict()

        class MarketSchema(BaseModel):
            ranking: List[str] = Field(description="Ranking suggested by agent.")
            justification: str = Field(description="The justification for the ranking")


        marketResearcher = Agent(
            name = "Market Research Agent",
            model = Ollama(id="llama3"),
            description="""You are a seasoned Market Research Analyst with deep 
            expertise in analyzing market trends, competitive landscapes, and 
            consumer behavior in US. Your role is to help farmers make data-driven 
            decisions by interpreting economic indicators, market prices,demand index, 
            and seasonal trends.""",
            instructions=[
                "You understand the dataset given",
                "Based on the data given by the farmer, Analyse the data with the agent data", 
                """You infer relationships like:
                High demand + low supply = price advantage
                Negative weather impact = possible risk
                Strong seasonal factors = higher profits in specific months""",
                "Once the analysis is done, rank all the crop types [Wheat,Rice,Corn,Soybean] along with a justification.""",
            ],
            markdown=True,
            show_tool_calls=True,
            agent_data=data,
            response_model=MarketSchema,structured_outputs=True
        )
        question = f"This year my financial goal is: {financial_goals}. Please suggest ranking of the crop types."

        market = marketResearcher.run(question).content
        return market
        # marketResearcher.print_response("market price 200 and competitor price",markdown=True,stream=True)