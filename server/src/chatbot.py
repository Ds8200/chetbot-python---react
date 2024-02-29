import json
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement

class MyChatBot:
    def __init__(self):
        self.chatbot = ChatBot('MyChatBot')
        self.trainer = ChatterBotCorpusTrainer(self.chatbot)
        self.train_bot()

    def train_bot(self):
        # Load corpus data from JSON file
        training_data = self.load_training_data()
        for item in training_data:
            self.add_to_corpus(item['question'], item['answer'])

        # Train the model
        self.trainer.train('chatterbot.corpus.english')

    def get_response(self, user_input):
        return self.chatbot.get_response(user_input)

    def load_training_data(self):
        try:
            with open('training_data.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading training data: {str(e)}")
            return []

    def add_to_corpus(self, question, answer):
        # Add question and answer to the training data file
        training_data = self.load_training_data()
        training_data.append({'question': question, 'answer': answer})
        try:
            with open('training_data.json', 'w', encoding='utf-8') as file:
                json.dump(training_data, file, ensure_ascii=False, indent=4)
        except FileNotFoundError as e:
            print(f"Error writing to training data: {str(e)}")

        # Add question and answer to the model's corpus
        statement = Statement(text=question, in_response_to=answer)
        self.chatbot.storage.create(**statement.serialize())
