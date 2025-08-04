
s = set()
data = []
with open('Include/IL/LLLL.vrt', 'r') as f:
    for line in f:
        s.add(int(line.split(";")[1]))

snew = dict(zip(sorted(s), range(len(s))))

with open('Include/IL/LLLL.vrt', 'r') as f:
    for i, line in enumerate(f):
        seq = int(line.split(";")[1])
        print(seq, snew[seq])
        data.append(line.replace(f";{seq};", f";{snew[seq] + 1};").strip())
# for seq in s:
#     print(seq)
    print(data)
        # data.append(line.replace)

with open('Include/IL/LLLL.vrt.new', 'w') as f:
    for line in data:
        f.write(line + "\n")

