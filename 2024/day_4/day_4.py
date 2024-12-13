directions = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1),
    (1,1),
    (-1,1),
    (-1,-1),
    (1,-1)
]

def get_data():
    with open('data.txt', 'r') as f:
        return [list(line.replace("\n", "")) for line in f.readlines()]
    return []

def check_position(initial_x, initial_y, data, word='XMAS'):
    count = 0
    for dx, dy in directions:
        x, y = initial_x, initial_y
        valid = True
        
        for char in word:
            if not (0 <= x < len(data[0]) and 0 <= y < len(data)):
                valid = False
                break
            
            if data[y][x] != char:
                valid = False
                break
            
            x += dx
            y += dy
        
        if valid:
            count += 1
    
    return count
    
def main():
    data = get_data()
    total_count = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] != ".":
                total_count += check_position(x,y, data)
            
    print(total_count)


if __name__ == '__main__':
    main()


