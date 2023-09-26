class Section:

    def __init__(self) -> None:
        self.l = 0
        self.m = 0
        self.s = 0

    def add(self, b):
        if b == "L":
            self.l += 1
        if b == "M":
            self.m += 1
        if b == "S":
            self.s += 1

    def __str__(self) -> str:
        return str(l.l) + " " + str(l.m) + " " + str(l.s)


books = input()
total = Section()
for book in books:
    total.add(book)

l, m, s = Section(), Section(), Section()

j = 0
for i in range(total.l):
    l.add(books[j])
    j += 1
for i in range(total.m):
    m.add(books[j])
    j += 1
for i in range(total.s):
    s.add(books[j])
    j += 1

print(l.m + l.s + m.l + m.s - min(m.l, l.m))