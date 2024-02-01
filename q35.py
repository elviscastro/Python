p1 = [50, 40, 30, 20, 10]
p2 = []


def fe(p1, p2):
  for i in range(len(p1)):
    p2.append(p1.pop())


fe(p1, p2)

print("p1 = ", p1)
print("p2 = ", p2)
