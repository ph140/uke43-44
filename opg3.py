from matplotlib import pyplot as plt


xliste = list()
yliste = list()

with open('akselerasjon.txt', 'r') as f:
    akselerasjonsliste = f.read().split(' ')

for i, val in enumerate(akselerasjonsliste):
    xliste.append(i*5)
    yliste.append(int(val))


plt.plot(xliste, yliste, 'b--')
plt.title('Akselerasjon over tid')
plt.xlabel('Tid / ms')
plt.ylabel('Akselerasjon / m/s^2')
plt.show()
