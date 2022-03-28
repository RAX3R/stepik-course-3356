if os.path.exists(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.readlines()

    with open(file_name, 'w', encoding='utf-8') as f:
        i = text[0].split(' - ')[0].replace('event ', '')
        text.insert(0, f"event {int(i) + 1} - '{event}'\n")
        f.writelines(text)
else:
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(f"event 1 - '{event}'")
