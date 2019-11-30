list = ["b**a**b**by**", "**pizza", "****piz**za","***pizza", "Ba***by", "B*by", "P*izz*a","B***b*y", "**Baby**y","B*b**bby**"]

for el in list:
    occ = el.count('**')
    if occ > 1:
        if occ%2 == 0:
            print(el, occ)
            for i in range(0, occ+1):
                if i % 2 == 0:
                    el = el.replace("**", "<br>", 1)
                else:
                    el = el.replace("**", "</br>", 1)
            print(el)

        else:
            print(el, occ)
            for i in range(0, occ-1):
                if i % 2 == 0:
                    el = el.replace("**", "<br>", 1)
                else:
                    el = el.replace("**", "</br>", 1)
            print(el)
            pass


