

def deleting_empty_lines(lines):
    for line in lines:
        if line == "\n":
            lines.remove("\n")
    return lines

