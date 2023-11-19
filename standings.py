import json
from tabulate import tabulate


with open("elo.json", "r") as f: eloData = json.load(f)
l = []
for i in eloData.items():
    if i[1]['races'] > 50:
        l.append([
            i[0],
            i[1]['rating']
        ])

sl = sorted(l, key=lambda x: x[1])

print(tabulate(sl[::-1], headers=['Driver', 'Rating'], tablefmt="grid"))

# sort(l)