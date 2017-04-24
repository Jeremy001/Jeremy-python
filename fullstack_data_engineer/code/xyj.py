#!/usr/bin/env python3
# -*- coding: utf-8 -*-

fr = open('xyj.txt', 'r')

characters = []
stat = {}

for line in fr:
    line = line.strip()
    if len(line) == 0:
        continue
    for x in range(0, len(line)):
        if not line[x] in characters:
            characters.append(line[x])
        if not line[x] in stat:
            stat[line[x]] = 0
        stat[line[x]] += 1
print(len(characters))
print(characters)
print(len(stat))
for key, value in stat.items():
    print(key, value)

fr.close()
