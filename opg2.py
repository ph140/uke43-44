from random import randint

with open("tilfeldigeTall.txt", "w") as f:
    for i in range(100):
        f.write(str(randint(1, 100))+",")


with open("tilfeldigeTall.txt", "r") as f:
    minliste = f.read().split(",")

minliste.pop()

for index, item in enumerate(minliste):
    minliste[index] = int(item)


minliste.sort(reverse=True)
print(minliste)
