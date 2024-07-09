class Strategy:
    def action(self, prev_action):
        if prev_action is None:
            return True
        return prev_action