import random

# ==================================================================================================
# NOTE Your code was modified
# ==================================================================================================

class Strategy:
    def __init__(self):
        self.coops = 0
        self.defects = 0
        self.coop_streak = 0
    def action(self, prev_action: bool | None) -> bool:
        if prev_action is not None:
            if prev_action:
                self.coops += 1
                self.coop_streak += 1
            else:
                self.defects += 1
                self.coop_streak = 0
        total = self.defects + self.coops
        p_defects = self.defects / total if total > 0 else 100
        if total < 7:
            return True
        if p_defects > 0.08 and self.coop_streak < 3:
            return False
        if self.coops + self.defects == 10 or self.coops + self.defects == 42:
            return False
        if random.random() < 0.025:
            return False
        return True
        
# True is cooperate, False is defect.
# prev_action represents your opponent's previous move. On the first round, it is None.
