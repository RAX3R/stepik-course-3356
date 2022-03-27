with open(sheet) as file:
    lst = [int(i) for i in file.read().split() if i.isdigit()]

with open(mean) as file:
    m = file.read()

if (sum(lst) // len(lst)) == int(m):
    print('OK')
else:
    print('ERROR')
