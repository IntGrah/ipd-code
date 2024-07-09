import random;

class Strategy:
    def action(self, prev_action):
        if prev_action == None:
            return 1;
        return prev_action if random.random() < 0.99 else 1;