lista1 = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
dlug = int(len(lista1)/3)
part1 = lista1[0:dlug]
part2 = lista1[dlug: 2*dlug]
part3 = lista1[2*dlug:]

part1.reverse()
part2.reverse()
part3.reverse()

print("\n",part1,"\n",part2,"\n",part3)
