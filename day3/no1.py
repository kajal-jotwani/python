COMMA = ','
for line in open('data.txt'):
    name , age = line.split(COMMA)
    first_name = name.split()[0]
    age = int(age)

print(f'{first_name:20}{age:3}')
