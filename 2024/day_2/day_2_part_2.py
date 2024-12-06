
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
        bad_levels = 0

        while left < right:
            if right >= len(row):
                if bad_levels <= 1: count += 1
                break

            if row[left] > row[right]:
                is_decrease = True
            elif row[left] < row[right]:
                is_add = True
            
            is_bad_level = (is_decrease and is_add) or abs(row[left] - row[right]) > 3

            if is_bad_level and bad_levels > 1:
                break
            elif is_bad_level:
                bad_levels += 1
                left += 1
                right += 1
                continue

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
