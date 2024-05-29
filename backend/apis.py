from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import requests
import os

app = Flask(__name__)

RASA_SERVER_URL = os.environ.get("RASA_SERVER_URL", "http://localhost:5005/webhooks/rest/webhook")


@app.route('/')
def index():
    print("In index")
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    # user_message = request.json.get("message")
    # response = requests.post(RASA_SERVER_URL, json={"sender": "user", "message": user_message, "action": "action_ask_python"})
    # response_data = response.json()
    #
    # if response_data:
    #     bot_response = response_data[0].get("text", "Sorry, I didn't understand that.")
    # else:
    #     bot_response = "Sorry, I didn't understand that."
    #
    # return jsonify({'answer': bot_response})
    #######################################################################
    data = request.json
    query = data.get('message', '')

    print(f"Query: {query}")
    # Convert speech to text if the query starts with 'listen:'
    if query.startswith('listen:'):
        query = query.replace('listen:', '')
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            query = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            query = "Sorry, I could not understand what you said."
        except sr.RequestError as e:
            query = "Sorry, I could not request results from Google Speech Recognition service; {0}".format(e)

    # Send the query to Rasa and get the response
    response = requests.post(RASA_SERVER_URL, json={"sender": "user", "message": query})
    data = response.json()
    #
    # # Convert Rasa response to speech
    response_text = ""
    for message in data:
        if 'text' in message:
            response_text += message['text'] + "\n"
    #
    # # Convert text to speech
    # tts_engine = pyttsx3.init()
    # tts_engine.say(response_text)
    # tts_engine.runAndWait()
    #
    return jsonify({"answer": response_text})


if __name__ == '__main__':
    app.run(host="0.0.0.0")
