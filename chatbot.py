from transformers import pipeline

print("Loading AI model... please wait ⏳")

chatbot = pipeline("text-generation", model="gpt2")

print("AI Chatbot Started (type 'exit' to stop)")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    response = chatbot(user, max_length=100, num_return_sequences=1)
    print("AI:", response[0]['generated_text'])
