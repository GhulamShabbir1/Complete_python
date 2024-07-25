# Hierarchical Inheritance
class ceo:
  def __init__(self,name):
    self.name = "Ali"
    print(f"the ceo of company is: {self.name}")

class Web(ceo):
  def __init__(self, team):
    self.team = "Web"
    super().__init__(team)

class App(ceo):
  def __init__(self, team):
    self.team = "App"
    super().__init__(team)

class Blockchain(ceo):
  def __init__(self):
    self.team = "Blockchain"
    super().__init__()

# a=ceo("ghulam Shabbir")
a=Blockchain()
print(a)