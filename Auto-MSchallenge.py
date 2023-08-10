def get_strings_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if len(lines) >= 3:
            id = lines[0].strip()
            password = lines[1].strip()
            url = lines[2].strip()
            return id, password, url
        else:
            return None

file_path = '../info.txt'
strings = get_strings_from_file(file_path)
if strings:
    id, password, url = strings
    print(f"ID: {id}")
    print(f"Password: {password}")
    print(f"URL: {url}")
else:
    print("ファイルの行数が足りません。")