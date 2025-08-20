# find all valid paths in a 20x20 grid.
# use backtracking

LIMIT = 20
END_POS = (LIMIT, LIMIT)
#print(GRID, len(GRID[0]), len(GRID))

# implement a backtracking algorithm

def uniquePath(cur_idx):
    cur_total = 0
    # choices, constraints, goals
    if cur_idx == END_POS:
        return 1
    
    # check constraints:
    x = cur_idx[0]
    y = cur_idx[1]
    if x < LIMIT + 1:
        # make choices
        cur_total += uniquePath((x + 1, y))
    if y < LIMIT + 1:
        cur_total += uniquePath((x, y + 1))
    
    return cur_total


total = uniquePath((0, 0))
print(total)