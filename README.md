# AI-Powered Sustainable Agriculture

An innovative AI-driven multi-agent system designed to promote sustainable agricultural practices by integrating advanced technologies with traditional farming methods. This project aims to reduce environmental impact, optimize resource utilization, and increase profitability for farmers by providing actionable insights and intelligent automation.

---

## Key Features

### 1. **Farmer Advisor**
- Provides personalized recommendations for crop selection and management based on soil type, weather conditions, and historical data.

### 2. **Market Researcher**
- Analyzes pricing trends and market conditions to help farmers make informed decisions on crop sales and investments.

### 3. **Multi-Agent AI Framework**
- Coordinates interactions between various agents (e.g., farmers, weather stations, agricultural experts) for efficient decision-making.

### 4. **Data Management**
- Utilizes an SQLite database for storing and processing historical data, ensuring long-term learning and system improvement.

---

## Project Structure

```
AI-Powered-Sustainable-Agriculture/
|-- datasets/         # Datasets used for training and testing
|-- src/              # Core implementation files
|   |-- advisor.py    # Farmer Advisor logic
|   |-- researcher.py # Market Researcher logic
|   |-- main.py       # Main entry point for the application
|   |-- database.py   # SQLite database integration
|-- tests/            # Unit and integration test cases
|-- docs/             # Documentation and API reference
|-- README.md         # Project overview and setup instructions
|-- requirements.txt  # Python dependencies
```

---

## Installation and Setup

### Prerequisites
- Python 3.8+
- SQLite

### Steps to Install
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Pranay-Godghate13/AI-Powered-Sustainable-Agriculture.git
   cd AI-Powered-Sustainable-Agriculture
   ```
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up the database**:
   ```bash
   python src/database.py
   ```

### Running the Application
To start the application, run:
```bash
python src/main.py
```

---

## Usage
1. Input farming details (e.g., soil type, weather conditions) into the Farmer Advisor module.
2. Use the Market Researcher module to analyze current market trends.
3. Review AI-generated insights and take informed decisions for crop selection, resource allocation, and sales.

---

## Testing
Run the unit and integration tests using:
```bash
pytest tests/
```

---

## Future Enhancements
- Integrate real-time IoT sensors for soil and weather monitoring.
- Expand the database to include global agricultural data.
- Develop a mobile-friendly interface for broader accessibility.
- Enhance AI algorithms with deep learning for predictive analytics.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Submit a pull request with detailed descriptions.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contact
For questions or feedback, reach out to:
- **Pranay Godghate**  
  [GitHub](https://github.com/Pranay-Godghate13) | [Email](mailto:pranay.godghate@example.com)
