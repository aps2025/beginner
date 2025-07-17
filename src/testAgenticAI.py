import random

class SimpleAgenticAI:
    def __init__(self, name="Agent"):
        self.name = name
        self.goals = ["explore", "learn", "help"]

    def perceive(self, environment):
        # Simple perception: just read the environment
        return environment

    def decide(self, perception):
        # Decide action based on perception and goals
        if "question" in perception:
            return "answer"
        return random.choice(self.goals)

    def act(self, action):
        # Perform the chosen action
        print(f"{self.name} decides to {action}.")

if __name__ == "__main__":
    agent = SimpleAgenticAI("AI-Agent")
    environment = {"question": "What is the weather?"}
    perception = agent.perceive(environment)
    action = agent.decide(perception)
    agent.act(action)