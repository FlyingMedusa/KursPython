

def deleting_empty_lines(lines):
    for line in lines:
        if line == "\n":
            lines.remove("\n")
    return lines


def loading_file():

    while True:
        filename = input("\nPlease give me the name of your markdown file\n\t")
        if filename[-3:] == ".md":
            break
        elif "." in filename:
            print("Wrong extension")
        elif "." not in filename:
            filename = filename + ".md"
            break
        else:
            print("It shouldn't have happened")

    return filename


def creating_file():
    while True:
        filename = input("\nPlease give me the name of your new html file\n\t")
        if filename[-5:] == ".html":
            break
        elif "." in filename:
            print("Sorry - wrong extension")
        elif "." not in filename:
            filename = filename + ".html"
            break
        else:
            print("It shouldn't have happened")

    return filename