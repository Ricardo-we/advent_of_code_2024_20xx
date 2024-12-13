
def get_data():
    with open("./sample_data.txt") as data:
        lines = data.readlines()
        for line in lines:
            result = line.split(":")[0]
            numbers = line.split()
    return []
    

def main():
    pass

if __name__ == "__main__":
    main()    