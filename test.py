d = { "vishal" : 90, "shrey": 40, "vivek": 95}
print(d)
d["nitin"] = 85
print(d)
p = d.values()
print(p)
for i in d:
    if i > 89:
        print(d[i])