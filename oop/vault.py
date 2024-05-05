class Vault:
  def __init__(self, galleons, sickels, knuts):
    self.knuts = knuts
    self.sickels = sickels
    self.galleons = galleons

  def __str__(self):
    return f"{self.galleons} Galleons, {self.sickels} Sickels, {self.knuts} Knuts"

  # Operator Overloading
  def __add__(self, other):
    galleons = self.galleons + other.galleons
    sickels = self.sickels + other.sickels
    knuts = self.knuts + other.knuts
    return Vault(galleons, sickels, knuts)

wisely = Vault(75, 50, 25)
potter = Vault(50, 100, 10)
total = wisely + potter
print(total)

# python under the hood does this operator overloading to concate two strings or add two lists

# theoratically we can use operator overloading in two separate classes