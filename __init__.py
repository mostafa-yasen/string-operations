
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
                                "|"], string=""):
    for ch in chars:
        string = string.replace(ch, '')

    return string


if __name__ == "__main__":
    files = get_file_paths()
    for file in files:
        file_content = get_file_content(file)
        str = remove_special_chars(string=file_content)
        print(str)
        print("." * 50)
