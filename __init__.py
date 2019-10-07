
def get_file_paths():
    print("Enter filename or -1 to stop")
    print('-' * 30)
    ch = 0
    files = []
    while ch != "-1":
        ch = input("filename: ")
        files.append(ch)

    files.pop()
    return files


def get_file_content(filename):
    try:
        with open(filename) as f:
            return f.read()

    except Exception as e:
        print("-" * 50)
        print(e)
        print("-" * 50)
        return ''


def remove_special_chars(chars=["'", '"', ",", ";", "~", "`",
                                "!", "@", "#", "$", "%", "^",
                                "&", "*", "(", ")", "-", "_", "=", "+",
                                "/", ".", ">", "<", "?", "/",
                                "|"], str=""):
    for ch in chars:
        str = str.replace(ch, '')

    return str


def tokenize(str):
    arr = str.split(' ')
    for val in arr:
        try:
            arr.remove('')
        except Exception:
            pass

    return arr


if __name__ == "__main__":
    files = get_file_paths()
    for file in files:
        file_content = get_file_content(file)
        str = remove_special_chars(str=file_content)
        tokens = tokenize(str)
        print(tokens)
