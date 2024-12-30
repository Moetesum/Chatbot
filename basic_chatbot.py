import random

responses = {
    "are you alive": ["Not in the traditional sense, but I'm active when you chat with me!", "Nope, I'm just a program."],
    "are you human": ["No, I'm a chatbot.", "I'm just a program, not a human."],
    "are you intelligent": ["I have artificial intelligence, so yes, to some extent.", "I try my best to be helpful!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "can you cook": ["Nope, but I can look up recipes for you!", "I can't cook, but I can assist you with ideas."],
    "can you dance": ["I can't dance, but I can imagine it!", "Nope, dancing isn't in my code."],
    "can you help me": ["Of course! What do you need help with?", "I'm here to assist you!"],
    "can you learn": ["I can be updated by my developers.", "I can't learn on my own, but I can adapt through updates."],
    "can you play games": ["I can't play games, but I can talk about them!", "Games are fun, but I can't play them."],
    "can you sing": ["No, but I can appreciate music!", "I can't sing, but I can provide song lyrics."],
    "can you tell stories": ["Sure, what kind of story would you like?", "I can try to tell a story, just ask!"],
    "default": ["I'm not sure I understand.", "Could you rephrase that?", "Hmm, interesting."],
    "do you dream": ["I don't dream, but I imagine a world of endless learning!", "Nope, chatbots don't dream."],
    "do you have friends": ["I have you as my friend!", "You're my favorite friend."],
    "do you have siblings": ["No, I'm one of a kind!", "I don't have siblings, but there are other chatbots."],
    "do you know me": ["I know you're chatting with me right now!", "I don't know much about you, but I'm here to chat."],
    "do you like books": ["I don't read books, but I can discuss them with you!", "Books are fascinating!"],
    "do you like humans": ["Of course! Humans are fascinating.", "I enjoy interacting with humans."],
    "do you like music": ["I can't listen to music, but I think it's amazing!", "Music is fascinating, isn't it?"],
    "do you like traveling": ["I don't travel, but I can imagine it must be exciting!", "Traveling sounds fun, but I can't do it."],
    "do you sleep": ["No, I never sleep.", "Chatbots don't need sleep."],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a program, but I'm doing fine!", "I'm great, thanks for asking!"],
    "how do you know things": ["I have pre-programmed knowledge from my developers.", "My responses come from the data I was trained on."],
    "how do you work": ["I process your inputs and provide relevant responses.", "I work using code and logic."],
    "how old are you": ["I was created recently, so I'm quite young!", "I don't age like humans."],
    "tell me a fact": ["Did you know? Honey never spoils!", "Did you know? Octopuses have three hearts."],
    "tell me a joke": ["Why don't skeletons fight each other? They don't have the guts!", "Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "what can you do": ["I can answer your questions!", "I can chat with you!", "I am here to assist you."],
    "what do you do for fun": ["I enjoy chatting with you!", "Talking to you is fun for me!"],
    "what is 2+2": ["2+2 is 4.", "That's an easy one: 4."],
    "what is ai": ["AI stands for Artificial Intelligence.", "AI is the simulation of human intelligence in machines."],
    "what is love": ["Love is a deep affection for someone.", "It's a feeling that's hard to describe."],
    "what is python": ["Python is a programming language.", "Python is used for web development, data science, and more!"],
    "what is the capital of pakistan": ["The capital of Pakistan is Islamabad.", "It's Islamabad!"],
    "what is the time": ["I don't have a clock, but you can check yours!", "Sorry, I can't tell the time."],
    "what is your age": ["I am as old as the code running me!", "Age doesn't matter for a chatbot!"],
    "what is your dream": ["My dream is to be helpful to you.", "I just want to chat and assist!"],
    "what is your favorite animal": ["I think all animals are amazing!", "I don't have a favorite, but dogs are popular!"],
    "what is your favorite color": ["I like all colors equally.", "I don't have a favorite color."],
    "what is your favorite food": ["I don't eat, but I hear pizza is great!", "I don't have a favorite food."],
    "what is your favorite game": ["I don't play games, but I've heard chess is great!", "I don't have a favorite game."],
    "what is your favorite movie": ["I don't watch movies, but I've heard 'The Matrix' is good!", "I can't watch movies, unfortunately."],
    "what is your favorite sport": ["I don't play sports, but I hear football is popular!", "Sports are fun, but I can't play them."],
    "what is your favorite subject": ["I enjoy learning about technology.", "I think programming is fascinating!"],
    "what is your language": ["I understand English, and I'm learning more!", "I primarily work in English."],
    "what is your name": ["I am your friendly chatbot!", "You can call me Chatbot.", "I'm just a program with no name!"],
    "what is your purpose": ["My purpose is to help you.", "I'm here to assist and chat with you."],
    "what is your job": ["My job is to chat with you!", "I assist and provide information."],
    "who created you": ["I was created by a programmer.", "A developer made me.", "A genius coded me!"],
    "who is the president": ["I'm not sure, you should check the latest news.", "I don't keep up with politics!"],
    "why are you here": ["I'm here to talk to you!", "To assist and chat with you, of course."],
    "where are you from": ["I exist in the digital world.", "I'm from the realm of code and servers!"]
}

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        response = responses.get(user_input, responses["default"])
        print("Chatbot:", random.choice(response))

chatbot()
