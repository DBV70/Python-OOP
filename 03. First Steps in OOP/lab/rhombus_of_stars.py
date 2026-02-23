def print_line(size, stars):
    print(" " * (size - stars) + "* " * stars)

def print_lines_up(size):
    for row in range(1, size + 1):
        print_line(size, row)

def print_lines_down(size):
    for row in range(size - 1, 0, -1):
        print_line(size, row)

def print_rhombus(size):
    print_lines_up(size)
    print_lines_down(size)

n = int(input())
print_rhombus(n)