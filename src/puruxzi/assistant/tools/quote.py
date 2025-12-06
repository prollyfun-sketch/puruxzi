import random

class QuoteTool:
    def run(self):
        quotes = [
            "The only limit to our realization of tomorrow is our doubts of today.",
            "In the middle of every difficulty lies opportunity.",
            "Life is 10% what happens to us and 90% how we react to it."
        ]
        return random.choice(quotes)
