# -*- coding: utf-8 -*-
def part1():
    with open("../data/day2inp.txt", "r") as f:
        hor = 0
        depth = 0
        for line in f:
            (k,v) = line.strip().split()
            if k == "forward":
                hor+=int(v)
            elif k == "down":
                depth+=int(v)
            else:
                depth-=int(v)
    return hor*depth
def part2():
    with open("../data/day2inp.txt", "r") as f:
        hor = 0
        depth = 0
        aim = 0
        for line in f:
            (k,v) = line.strip().split()
            if k == "forward":
                hor+=int(v)
                depth+=aim * int(v)
            elif k == "down":
                aim+=int(v)
            else:
                aim-=int(v)
    return hor*depth

print("solution to part 1",part1())
print("solution to part 2",part2())

#solution to part 1 1480518
#solution to part 2 1282809906