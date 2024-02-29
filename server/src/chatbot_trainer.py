class ChatBotTrainer:
    def __init__(self, chatbot):
        self.chatbot = chatbot

    def add_qa_pair(self, question, answer):
        self.chatbot.add_to_corpus(question, answer)
        self.chatbot.train_bot()
