directions = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}
rotate_right = { 
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}


def get_data():
    with open("./sample_data.txt") as data:
        return [list(line.replace('\n', "")) for line in data.readlines()]

def is_in_map(map_data, x, y):
    return len(map_data) - 1 > y and len(map_data[0]) - 1 > x

def move_guard():
    pass
    

def main():
    visited = set()
    current_direction = ">"
    current_position = (0, 0)
    data = get_data()

    for row in data:
        for col in data:
            
    
    

if __name__ == "__main__":
    main()