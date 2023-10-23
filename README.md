# Zenko-Hackathon
##Introduction
This project is a Flask web application that uses OpenAI's API and the LangChain library to process and analyze text data from multiple sources. It splits text data into chunks, embeds each chunk, and loads it into a vector store. The app also has a chat feature that uses OpenAI's GPT-3.5-turbo model to generate conversational responses. It uses the Google Translate API to support multilingual interactions. You can interact with the AI chat feature through the site, with your message being redirected to the Python script for processing and response generation.

##Getting Started
To get started with this project, you need to clone the repository and install the required dependencies:

git clone <repository-url>
cd <repository-name>
pip install -r requirements.txt
Set your OpenAI API key in a key.py file, the variable has to be named key.

##File Structure
The main script, API.py, imports necessary modules and defines the Flask application. The Flask app serves static files, handles routes, and defines the chat feature. The langchain module is used to process and analyze text data, and the googletrans module is used for translating text.

##Usage
To run the Flask application:
```
flask run
```
This will start the application on your localhost. You can interact with the application by navigating to the home route (http://localhost:5000/). The application includes a chat feature, which can be accessed by sending a POST request to the /chat route with a 'message' parameter. This message is then redirected to the Python script, processed, and a response is generated by the AI chat feature. Flask is used to send the message that the user entered in the web app to the Python script.

To execute the main function in the terminal:
```
python API.py
```
This function runs an interactive chat session in the terminal. You can input text and the application will return a response generated by the OpenAI model.

##Features
The application uses the LangChain library to load text data from JSON and CSV files, split it into chunks, embed each chunk using OpenAI's embeddings, and load it into a vector store. It uses OpenAI's GPT-3.5-turbo model to generate conversational responses to user input. The application also uses the Google Translate API to translate user input and bot responses, supporting multilingual interactions.
