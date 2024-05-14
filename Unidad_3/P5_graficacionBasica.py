from matplotlib import pyplot

x = [i for i in range(-10,11)]
print (x)

y = [i**2 for i in x]

print(y)

pyplot.plot(x,y)
pyplot.show()
