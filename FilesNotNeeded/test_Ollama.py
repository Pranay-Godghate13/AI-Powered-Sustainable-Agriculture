import ollama
# Define the model name (use a lightweight model like "mistral")
model_name = "mistral"
# Define the user input prompt
prompt = "give a estimate on behalf of past data on  montly rainfall in mm for latitude 12.97, and longitude 77.59"
# Run the model and get a response
response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])
# Print the response
print("AI Response:", response["message"]["content"])


