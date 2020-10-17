from random import randint

with open("tilfeldigeTall.txt", "w") as file:
    for i in range(100):
        file.write(str(randint(1, 100))+",")


with open("tilfeldigeTall.txt", "r") as file:
    minliste = file.read().split(",")

minliste.pop()

for index, item in enumerate(minliste):
    minliste[index] = int(item)


minliste.sort(reverse=True)
print(minliste)
