
colors= ["Red","Green","white","Black","Pink","Yellow"]

colors = [x for (i, x) in enumerate(colors) if i not in (0, 4, 5)]

print(colors)