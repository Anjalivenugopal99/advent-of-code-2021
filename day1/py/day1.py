# -*- coding: utf-8 -*-
def get_input():
    with open("../data/day1inp.txt", "r") as f:
        return [int(line.strip()) for line in f]
    
inp = get_input()
print("count of increases", sum([1 if inp[i]>inp[i-1] else 0 for i in range(1,len(inp))]))
print("count of 3 window increases", sum([1 if inp[i]>inp[i-3] else 0 for i in range(3,len(inp))]))
#count of increases 1752
#count of 3 window increases 1781