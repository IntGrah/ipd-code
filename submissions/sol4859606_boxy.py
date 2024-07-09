# this one should lose

class Strategy:

  def __init__(self):
    self.prev_actions = []
    self.identified = None
    self.bestie = [False, False, False, True, False, False, False, False, True, True]
    self.myself = [True, False, False, True, False, False, True, False, True, True]

  def action(self, prev_action):
    prev_actions = self.prev_actions
    if prev_action is None: 
      prev_actions.clear()
      self.identified = None
    else: prev_actions += [prev_action]

    
    if sum(1 for (a,b) in zip(self.bestie, prev_actions) if a != b) > 1: 
      self.identified = False
    elif len(prev_actions) == 10: self.identified = True

    if self.identified is not None:
      if self.identified: return True 
      return prev_action

    return self.myself[len(prev_actions)]
