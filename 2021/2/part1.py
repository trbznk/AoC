with open("inputs.txt") as f:
    inputs = f.read().splitlines()

h, d = 0, 0

for cmd in inputs:
    cmd, v = cmd.split()
    v = int(v)
    if cmd == "forward":
        h += v
    elif cmd == "down":
        d += v
    elif cmd == "up":
        d -= v

print(h, d, h*d)
