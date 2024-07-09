class Strategy:
  def __init__(self):
    self.prev_actions = []
    self.identified = None
    self.myself = [False, False, False, True, False, False, False, False, True, True]
    self.bestie = [True, False, False, True, False, False, True, False, True, True]

  def action(self, prev_action):
    prev_actions = self.prev_actions
    if prev_action is not None: prev_actions += [prev_action]
    
    if sum(1 for (a,b) in zip(self.bestie, prev_actions) if a != b) > 1: 
      self.identified = False
    elif len(prev_actions) == 10: self.identified = True

    if self.identified is not None:
      if self.identified: return False 
      return prev_action

    return self.myself[len(prev_actions)]