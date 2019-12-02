#Convert md (marktdown) to html
import moduleMdHtml as mod
import CleanModule as cl

filename = mod.loading_file()
print("Your file name:", filename)

with open(filename, encoding="utf-8") as f:
    lines = f.readlines()

lines = cl.deleting_empty_lines(lines)

outputfile = mod.creating_file()
with open(outputfile, 'w') as fw:
    previous_line = "I'm the zero sentence"
    for line in lines:
        output_lines, previous_line = mod.grand_checker(line,previous_line)
        save = str(output_lines) +"\n"
        fw.write(save)
print("Done!")