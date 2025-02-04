#Convert md (marktdown) to html
import module_md_html as mod
import clean_module as cl

filename = cl.loading_file()
print("Your file name:", filename)

with open(filename, encoding="utf-8") as f:
    lines = f.readlines()

lines = cl.deleting_empty_lines(lines)

outputfile = cl.creating_file()
with open(outputfile, 'w') as fw:
    begin = cl.begin_html()
    fw.write(begin)
    fw.write("\t<body>\n")
    previous_line = "I'm the zero sentence"
    c_list = ""
    for line in lines:
        output_lines, previous_line,c_list = mod.grand_checker(line,previous_line, c_list)
        save = str(output_lines) +"\n"
        fw.write(save)
    fw.write("\t</body>\n</html>")
print("Done!")