class Strategy:

  defects_in_a_row = 0

  def action(self, prev_action: bool | None) -> bool:
    if prev_action is False:
      self.defects_in_a_row += 1
    if self.defects_in_a_row >= 5:
      return False
    if prev_action is True:
      self.defects_in_a_row = 0
    return True
