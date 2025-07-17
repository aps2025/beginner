import random

class SimpleAIAgent:
    def __init__(self, name="Agent"):
        self.name = name

    def greet(self):
        greetings = [
            "Hello! How can I assist you today?",
            "Hi there! What can I do for you?",
            "Greetings! Need any help?"
        ]
        print(greetings)
        return random.choice(greetings)

    def respond(self, message):
        if "hello" in message.lower():
            return self.greet()
        elif "bye" in message.lower():
            return "Goodbye! Have a great day!"
        else:
            return "I'm not sure how to respond to that."

if __name__ == "__main__":
    agent = SimpleAIAgent("SampleAgent")
    print(agent.greet())
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Goodbye!")
            break
        response = agent.respond(user_input)
        print(f"Agent: {response}")