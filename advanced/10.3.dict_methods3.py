text = "TheyDon'tKnowThatWeKnowTheyKnowWeKnow"
d = dict()

for ch in text:
    d[ch] = d.get(ch, 0) + 1
print(d)