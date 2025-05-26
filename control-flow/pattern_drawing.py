# Utilize while loops and nested for loops to draw a simple text-based pattern.

pattern_size = int(input('Enter the size of the pattern: '))

for i in range(pattern_size):
    for j in range(pattern_size):
        print('*', end='')
    print()
