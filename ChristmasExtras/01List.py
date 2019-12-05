#give a chosen number of elements of a list counting from the end
import module01 as mod

choice = mod.user_choice()

if choice == "s":
    user_list = mod.option_separate()
elif choice == "l":
    user_list = mod.option_list()

el_number = mod.user_number(user_list)
output_list = mod.tail(el_number,user_list)
print(output_list)