with open("./input", "r") as f:
    file_input=f.readlines()

map = [line.replace('\n', '') for line in file_input]
map_height = len(map)
line_size = len(map[0])

# Slope Inputs
all_dx = [[3], [1,3,5,7,1]]
all_dy = [[1], [1,1,1,1,2]]
# Starting Point
all_x = [0,0]
all_y = [0,0]

def tree_count(x, y, dx, dy):
    num_trees = 0

    while y < map_height:
        map_x = x % line_size
        if map[y][map_x] == "#":
            num_trees += 1
        x += dx
        y += dy
    return num_trees
 
for i in range(len(all_dx)):
    print(f"\n---Start of solution for part {i}---")
    part_x = all_x[i]
    part_y = all_y[i]
    part_dx = all_dx[i]
    part_dy = all_dy[i]

    output = 1
    for j in range(len(part_dx)):
        output *= tree_count(part_x, part_y, part_dx[j], part_dy[j])
    
    print(f"Result is: {output}")

    print(f"----End of solution for part {i}----\n")
