#!/usr/bin/python3

def draw_tree(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

# Укажите желаемую высоту ёлки (количество уровней)
tree_height = 5
draw_tree(tree_height)
