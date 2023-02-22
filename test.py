class CallCenter:
    def __init__(self):
      self.customers = []

    def is_empty(self):
      return self.customers == []

    def add(self, x):
      self.customers.insert(0, x)

    def next(self):
      return self.customers.pop()


c = CallCenter()

while True:
    n = input()
    if n == 'end':
        break
    c.add(n)

#your code goes here

#variable 
times_general = 0
times_technical = 0
for i in c.customers:
   if i == "general":
      times_general+=1
   elif i == "technical": 
      times_technical+=1

total = (times_general*5) + (times_technical*10)

#check
print(times_general)
print(times_technical)
print(total)