gyumolcs = ['alma', 'körte', 'banán']

print(gyumolcs[1])
# print(gyumolcs[10])       IndexError: list index out of range

hossz = len(gyumolcs)
print(hossz, 'elemű a lista')
print()

for i in range(3):
    print(gyumolcs[i])
