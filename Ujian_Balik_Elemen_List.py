def balikPosisi(x):
    i=0
    while i<len(x):
        x.insert(i,x[len(x)-1])
        x.pop(len(x)-1)
        i+=1
    return x

print(balikPosisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balikPosisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikPosisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))