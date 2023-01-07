
numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]

print(f"\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10")

for n in numbers:
    print(f'{n}\t', end="")
    for m in numbers:
        if m != 10:
            print(f'{m*n}\t' , end="")
        if m == 10:
            print(f'{10*n}')




