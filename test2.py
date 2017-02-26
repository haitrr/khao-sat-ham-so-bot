from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
chatterbot = ChatBot("Training Example")
chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train(
    "chatterbot.corpus.english"
)
# Get a response to the input text 'How are you?'
response = chatterbot.get_response('I am Hai')

print(response)