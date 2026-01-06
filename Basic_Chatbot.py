# Basic Rule-Based Chatbot
def chatbot_response(user_input):
user_input = user_input.lower()
if user_input == "hello":  
    return "Hi! 👋"  
elif user_input == "how are you":  
    return "I'm fine, thanks! 😊"  
elif user_input == "bye":  
    return "Goodbye! 👋 Have a nice day!"  
else:  
    return "Sorry, I don't understand that"