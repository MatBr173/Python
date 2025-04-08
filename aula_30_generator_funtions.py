def generator(n = 0, maximum = 10000):
    while True:
        yield n
        n += 1

        if n > maximum:
            return print('fim')
        
gen = generator()

for n in gen:
    print(n)