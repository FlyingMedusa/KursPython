def range_of_time(point):
    point_date = []
    point.split(",")
    for el in point:
        point_date.append(el)
    return point_date


start = input("Please provide the start time:\t")
range_start = range_of_time(start)
end = input("Please provide the end time:\t")
range_end = range_of_time(end)
print(range_start)
print(range_end)