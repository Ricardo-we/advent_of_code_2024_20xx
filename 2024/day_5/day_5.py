from collections import defaultdict, deque

def get_data():
    with open("./data.txt") as data:
        rules = [tuple(map(int, line.split("|"))) for line in data.readlines()]

    with open("./bottom_data.txt") as data:
        updates = [tuple(map(int, line.split(','))) for line in data.readlines()]
        
    return rules, updates

def valid_update(rules, update):
    for x,y in rules:
        if x in update and y in update:
            if(update.index(x) > update.index(y)):
                return  False
    return True


def find_middle_page(update):
    update_len = len(update)
    return update[update_len // 2]

def main():
    rules, updates = get_data()
    print(rules)
    result = 0
    # if x in updates 
    for update in updates:
        if valid_update(rules, update):
            middle_page = find_middle_page(update)
            result += middle_page
            
    print(result)
    return result

if __name__ == "__main__":
    main()