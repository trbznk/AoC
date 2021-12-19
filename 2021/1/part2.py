with open("input.txt") as f:
    inputs = f.read().splitlines()
    inputs = [int(x) for x in inputs]

last_window = None
increases = 0
w = 3
for i in range(len(inputs)-w+1):
    window = sum(inputs[i:i+w])
    if last_window is not None:
        if window > last_window:
            increases += 1

    last_window = window

print(increases)
