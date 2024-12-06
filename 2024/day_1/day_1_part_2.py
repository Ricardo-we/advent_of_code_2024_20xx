
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
    results = []
    left_data, right_data = get_data()
    already_used_nums = {}
    
    for right in right_data:
        if not right in already_used_nums:
            already_used_nums[right] = 1 
            continue
        already_used_nums[right] += 1
        
    for left in left_data:
        results.append(left * already_used_nums[left] if left in already_used_nums else 0)
        
    return sum(results)


if __name__ == "__main__":
    result = main()
    print(result)
    