import sys

iteravel = ["Eu", "Tenho", "__iter__"]
iterator = iter(iteravel)
generator = (n for n in range(1000))

print(next(iterator))
print(next(iterator))
print(next(iterator))

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

print(sys.getsizeof(generator))