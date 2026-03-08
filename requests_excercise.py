from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic
client = Anthropic()
model = 'claude-sonnet-4-5'

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text

# Make an initial list of messages
messages = []

# Use a 'while true' loop to run the chatbot forever
while True:
    # Get user input
    user_input = input("> ")
    #print(">", user_input)

    # Add user input to the list of messages
    add_user_message(  messages, user_input)

    #Call Claude with the 'chat' function
    answer = chat(messages)

    #Add generated text to the list of messages
    add_assistant_message(messages, answer)

    # Print the generated text
    print(answer)