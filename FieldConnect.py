from typing import Self
from Coordinator import Coordinator

def main():
    question = f"I am a coordinator who take data from farmer advisor agent, and market researcher agent.Give me best possible output after analysing data from farmer advisor agent & market researcher agent and rank the crop in order with justification."
    Coordinator.run(Self,question)
    

if __name__ == "__main__":
    main()
