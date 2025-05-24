a =  [1, 11, 21, 1211, 111221]

solution = str(1)
for x in range(30):
    a = list(solution)
    solution = []
    counter = 1
    for i in range(0, len(a)):
        try:
            if a[i] == a[i+1]:
                counter += 1
              
            else:
                part_a = str(counter) + a[i]
                solution += part_a
                counter = 1
        except IndexError:
            part_a = str(counter)+ a[i]
            solution += part_a
print(solution)
print(len(solution))