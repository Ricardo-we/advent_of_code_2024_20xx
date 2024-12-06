
def get_data():
    with open('data.txt', 'r') as f:
        data: str = f.readlines()
        return [[int(col) for col in line.split(" ")] for line in data] 
    return []


def main():
    data = get_data()
    count = 0

    for row in data:
        is_decrease = False
        is_add = False
        left, right = 0, 1

        while left < right:
            if right >= len(row):
                count += 1
                break

            if row[left] > row[right]:
                is_decrease = True
            if row[left] < row[right]:
                is_add = True
            
            if (is_decrease and is_add) or abs(row[left] - row[right]) > 3:
                break
            
            if is_decrease and row[left] > row[right]:
                left += 1
                right += 1
                continue
            elif is_add and row[left] < row[right]:
                left += 1
                right += 1
                continue
            else:
                break


    print(count)
    return count


if __name__ == "__main__":
    main()
