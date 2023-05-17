fpath = "cascade.py"
f = open(fpath, "r")
for c in f.read(100):
    if ord(c) not in range(0,127):
        print("nonprintable!")