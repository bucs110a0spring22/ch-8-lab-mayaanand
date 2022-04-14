class StringUtility:
  def __init__ (self,string):
    self.string = string
  def __str__ (self):
    return self.string 
  def vowels(self):
    count = 0
    for i in self.string:
      if i in "aeiouAEIOU":
        count += 1
    if count >= 5:
      return "many"
    else: return str(count)
  def bothEnds(self):
    if len(self.string) <= 2:
      return ""
    else:
      return self.string[0:2] + self.string[-2:]
  def fixStart(self):
    if len(self.string) <= 1:
      return self.string
    else:
      return self.string[0] + self.string[1:].replace(self.string[0], "*")
  def asciiSum(self):
    sum = 0
    for i in self.string:
      sum += ord(i)
    return sum
  def cipher(self):
    newString = ""
    for i in self.string:
      value = ord(i)
      if value <= 90 and value >= 65:
        value += len(self.string) % 26
        if value > 90:
          value -= 26
        newString += chr(int(value))
      elif value <= 122 and value >= 97:
        value += len(self.string) % 26
        if value > 122:
          value -= 26
        newString += chr(int(value))
      else:
        newString += i
    return newString