grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# x=0
#
# for y in range(len(grid[0])):
#     s = ''
#     while x < len(grid):
#         s = s + grid[x][y]
#         x += 1
#     print(s)
#     x = 0

print()
for y in range(len(grid[0])):
    for x in range(len(grid)):
        print(grid[x][y], end = ' ')
    print()