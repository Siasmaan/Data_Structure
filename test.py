class Track:
    def __init__(self, title, next):
        self.title = title
        self.next = next

class Player:
    def __init__(self):
        self.head = None

    def add(self, title):
        if not self.head:
            self.head = Track(title, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Track(title, None)

    def show(self):
        n = self.head
        while(n != None):
            print(n.title)
            n = n.next
            if n == None:
                break

p = Player()
while True:
    x = input()
    if x == 'end':
        break
    p.add(x)

#your code goes here

p.show()
