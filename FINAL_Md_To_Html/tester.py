list = ["babby**", "**pizza", "****pizza","***pizza", "Ba***by", "B*by", "P*izz*a","B***b*y", "**Baby**y","B*b**bby**"]


for el in list:
    occurence = el.count('**')
    print(el, occurence, "\n")

# result:
# babby** 1
#
# **pizza 1
#
# ****pizza 2
#
# ***pizza 1
#
# Ba***by 1
#
# B*by 0
#
# P*izz*a 0
#
# B***b*y 1
#
# **Baby**y 2
#
# B*b**bby** 2