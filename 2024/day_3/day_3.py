import re

def get_data():
    with open("sample_data.txt") as data:
        return data.read()
    return ""


def main():
    data = get_data()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(pattern, data)
    print(matches)
    total = sum(int(x) * int(y) for x, y in matches)

    print(total)
    return total

if __name__ == "__main__":
    main()