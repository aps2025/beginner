import random

class AgenticAI:
    def __init__(self, name):
        self.name = name
        self.knowledge = [
            "The sky is blue.",
            "Python is a popular programming language.",
            "AI stands for Artificial Intelligence.",
            "Water boils at 100°C."
        ]

    def perceive(self, input_text):
        print(f"{self.name} perceives: {input_text}")

    def reason(self):
        fact = random.choice(self.knowledge)
        print(f"{self.name} reasons: {fact}")
        return fact

    def act(self, action):
        print(f"{self.name} acts: {action}")

    def interact(self, user_input):
        self.perceive(user_input)
        response = self.reason()
        self.act(f"Responds to user: {response}")
        return response

if __name__ == "__main__":
    agent = AgenticAI("AgenticBot")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        agent.interact(user_input)