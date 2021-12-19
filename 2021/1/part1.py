with open("input.txt") as f:
    inputs = f.read().splitlines()


last_x = None
increases = 0
for x in inputs:
    x = int(x)
    if last_x is not None:
        if x > last_x:
            increases += 1
    last_x = x

print(increases)
