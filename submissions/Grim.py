class Strategy:
    nice = True

    def action(self, prev_action):
        if prev_action == False:
            self.nice = False
        return self.nice