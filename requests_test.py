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

# Make starting list of messages
messages = []

# Add in the initial user question of 'Define quantum computing in one sentence'
add_user_message(  messages, "Define quantum computing in one sentence")

# Pass the list of messages into 'chat' to get the answer
answer = chat(messages)

# Take the answer and add it as an assistant message into our list
add_assistant_message(messages, answer)

# Add in the user's follow-up question
add_user_message(messages, "Write another sentence")

# Call chat again with the list of messages to get a final answer
answer = chat(messages)

print(answer)