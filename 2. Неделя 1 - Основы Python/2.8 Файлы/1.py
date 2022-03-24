file_name = input()

if file_name.endswith('.txt'):
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
        print(text)
else:
    print("А я - файл, имя которого не имеет расширения")
