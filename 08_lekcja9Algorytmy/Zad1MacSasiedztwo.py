el_list = ["house", "school", "church", "bar", "hospital", "cinema", "theatre"]
graph = [
    [0,1,1,1,0,0,0],
    [1,0,0,0,1,0,0],
    [1,0,0,1,0,1,0],
    [1,0,1,0,1,0,0],
    [0,1,0,1,0,1,1],
    [0,0,1,0,1,0,1],
    [0,0,0,0,1,1,0]
]

for row in range(7):
    print(el_list[row], ":")
    for col in range(7):
        if graph[row][col] == 1:
            print(el_list[row], "<--->", el_list[col])