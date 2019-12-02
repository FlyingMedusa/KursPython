

def the_future_mode(previous_line, now):
    now = now.lstrip("\t")
    if previous_line[-4:] == "/li>" and now[:3] != "<li":
        if ord_list_possibility(previous_line):
            now = "\t</ol>\n" + now
        if unord_list_poss(previous_line):
            now = "\t</ul>\n" + now

    return now


def ord_list_possibility(line):
    line = line.lstrip("\t")
    line = line.lstrip("<li>")
    for k in range(0, len(line)):
        if line[k].isnumeric() and line[k + 1] == "." and line[k + 2] == " ":
            return True
        elif line[k].isnumeric() and line[k + 1].isnumeric():
            continue
        elif (line[k] == " " and line[k + 1].isnumeric()):
            continue
        elif line[k] == " " and line[k + 1] == " ":
            continue
        else:
            return False



def into_ord_list(line, previous_line):
    if previous_line[-4:] != "/li>":
        list = "\t<ol>\n\t\t<li>" + line + "</li>"
    else:
        list = "\t\t<li>" + line + "</li>"
    return list


def unord_list_poss(line):
    line = line.lstrip("\t")
    line = line.lstrip("<li>")
    for k in range(0, len(line)):
        if (line[k] == "+" or line[k] == "*" or line[k] == "-") and line[k+1] == " ":
            return True
        elif line[k] == " " and ((line[k+1] == "+" or line[k+1] == "*" or line[k+1] == "-") or line[k+1] == " "):
            continue
        else:
            return False


def into_unord_list(line, previous_line):
    if previous_line[-4:] != "/li>":
        list = "\t<ul>\n\t\t<li>" + line + "</li>"
    else:
        list = "\t\t<li>" + line + "</li>"
    return list

list = ["\t\t<li> 1. I just love <b>bold text</b>.</li>" ,
        "\t\t<li> 2. I just love <em>italic text</em>.</li>",
        "\t\t<li> 2. I just love <b>bold text</b>.</li>",
        "\t jnisdn"
        "\t\t<li> 2. I just love <em>italic text</em>.</li>",
        "\t\t<li> 3. Love<b>is</b> bold.</li>"]


for i in range(0,len(list)-1):
    previous_line = list[i]
    now = list[i+1]
    now = the_future_mode(previous_line, now)
    print(now)

