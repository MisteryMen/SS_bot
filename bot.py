import os
from io import FileIO

from discord_easy_commands import EasyBot

class test_DASS:
    def __init__(self):
        self.questions = []
        self.answers = []
        self.id = 0

    def set_Question(self,pregunta):
        self.questions.append(pregunta)
        self.id += 1

    def set_answer(self,answer):
        self.answers.append(answer)

    def get_questions(self):
        return self.questions

class bot_instructions:

    def __init__(self):
        self.bot = EasyBot
        self.questions = test_DASS()


    def load_questions(self):
        questions = open("questions.txt","r")
        for i in questions:
            self.questions.set_Question(i)

    def imprime(self):
        print(self.questions.get_questions())

if __name__ == '__main__':

    mybot = bot_instructions()
    mybot.load_questions()
    mybot.imprime()