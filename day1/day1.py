import pyperclip

input = list(map(int, (pyperclip.paste()).split()))

l1 = sorted(input[::2])
l2 = sorted(input[1::2])

print(l1, l1)