message = 'It was a bright cold day in Apri, and the clocks were striking thrteen.'
count = {}

for chracter in message:
    count.setdefault(chracter, 0)
    count[chracter] = count[chracter] + 1

print(count)