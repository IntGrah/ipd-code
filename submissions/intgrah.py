class Strategy:
    def __init__(self):
        self.history = []

    def action(self, prev_action: bool | None) -> bool:
        if prev_action is not None:
            self.history.append(prev_action)
        if len(self.history) < 2:
            return True
        return self.history[-2] or self.history[-1]
