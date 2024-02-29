from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import MyChatBot
from chatbot_trainer import ChatBotTrainer

app = Flask(__name__)
CORS(app)

chatbot = MyChatBot()
trainer = ChatBotTrainer(chatbot)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('user_input', '')
    response = chatbot.get_response(user_input)
    return jsonify({'response': str(response)})

@app.route('/add_qa', methods=['POST'])
def add_qa():
    data = request.json
    question = data.get('question', '')
    answer = data.get('answer', '')
    trainer.add_qa_pair(question, answer)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(port=5000)
