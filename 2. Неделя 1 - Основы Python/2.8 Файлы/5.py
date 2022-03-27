import os.path

i = input()

if os.path.isdir(i):
    print("ERROR:\nЭто каталог, а не файл")
elif os.path.exists(i):
    with open(i) as f:
        print("CONTENT:", f.read(), sep='\n')
else:
    print("ERROR:\nФайл не существует")
