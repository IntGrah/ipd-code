# Suspicious Tit for Two Tats

class Strategy:
    def __init__(self):
        self.defect_count = 0

    def action(self, prev_action):
        if prev_action is None:
            return False
        if prev_action is False:
            self.defect_count += 1
        else:
            self.defect_count = 0
        return self.defect_count < 2
