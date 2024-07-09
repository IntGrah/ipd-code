class Strategy:
    forgive = True
    betrayed = False
    def action(self, prev_action):
        if self.betrayed: return False
        elif prev_action is False and self.forgive is True:
            self.forgive = False
            return True
        elif prev_action is False and self.forgive is False:
            self.betrayed = True
            return False
        elif prev_action is True:
            return True
        else:
            # ========================
            # NOTE Your code was modified
            return True
            # ========================
            # raise TypeError

