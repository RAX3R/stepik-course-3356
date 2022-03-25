with open(input()) as file:
    text = file.read().split('\n')

print(sum([int(i) for i in text if i]))
