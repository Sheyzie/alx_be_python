# Utilize while loops and nested for loops to draw a simple text-based pattern.

pattern_size = int(input('Enter the size of the pattern: '))

i = 1
while i <= pattern_size:
    for j in range(pattern_size):
        print('*', end='')
    print()
    i += 1
