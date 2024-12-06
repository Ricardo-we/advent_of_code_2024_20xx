
def get_data():
    with open("./data.txt") as data:
        left = []
        right = []
        
        for line in data.read().splitlines():
            left_num, right_num = line.split("   ")
            left.append(int(left_num))
            right.append(int(right_num))
        left.sort()
        right.sort() 

        return left, right
    return [], []


def main():
    # left = 0 
    # right = 0
    results = []
    left_data, right_data = get_data()
    for i in range(len(left_data)):
        results.append(abs(left_data[i] - right_data[i]))
        
    return sum(results)


if __name__ == "__main__":
    result = main()
    print(result)
    