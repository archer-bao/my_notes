#!/usr/bin/python3

import sys
import collections

if len(sys.argv) != 2:
    print("参数错误，请重新输入")
    print("usage: " + sys.argv[0] + " file")
    exit()

print("准备统计文件: " + sys.argv[1])

removeDUP = set()
file_set = set()

file = open(sys.argv[1])
for line in file:
    arr = line.split()
    removeDUP.add(arr[0] + "\t" + arr[1] + "\t" + arr[2])
    file_set.add(arr[0])
file.close()

dic = collections.defaultdict(list)
for line in removeDUP:
    for one in file_set:
        if 0 == line.find(one) and line[len(one)] == "\t":
            arr = line.split()
            dic[one].append([arr[1], arr[2]])

res = open("result.txt", "w")
res.write("{:<89}".format("文件名") + "{:<12}".format("进程名") +
          "{:>6}".format("进程号") + "\n")

final = {}
for key in dic:
    temp = collections.defaultdict(set)
    for first in dic[key]:
        for second in dic[key]:
            if first[0] == second[0]:
                temp[second[0]].add(second[1])
    final[key] = temp

for index in final:
    for elem in final[index]:
        res.write("{:<92}".format(index)
                  + "{:<16}".format(elem)
                  + "{:>6}".format(str(final[index][elem]))
                  + "\n")
res.close()

print("统计结束，请查看文件: " + "result.txt")
