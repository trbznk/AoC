with open("inputs.txt") as f:
    inputs = f.read().splitlines()

h, d, aim = 0, 0, 0

for cmd in inputs:
    cmd, v = cmd.split()
    v = int(v)
    if cmd == "forward":
        h += v
        d += v*aim
    elif cmd == "down":
        aim += v
    elif cmd == "up":
        aim -= v

print(h, d, h*d)
