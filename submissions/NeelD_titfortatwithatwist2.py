class Strategy:
  total = 0
  coops = 0
  defects = 0
  threshhold = 0.73
  switches = 0
  prevprev = None
  def action(self, prev_action):
    self.total += 1
    if prev_action is not None:
      if self.prevprev is not None:
        if prev_action != self.prevprev:
          self.switches += 1
      if prev_action:
        self.coops += 1
      else:
        self.defects += 1
      self.prevprev = prev_action

    if self.coops / self.total > self.threshhold:
      return True
    elif self.defects / self.total > self.threshhold:
      return False
    else:
      if self.switches/self.total > 0.5: return not prev_action
      else: return prev_action
    