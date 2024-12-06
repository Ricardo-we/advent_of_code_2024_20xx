def get_data():
    with open('sample_data.txt', 'r') as f:
        return f.readlines()
    return []
    
def main():
    data = get_data()
    print(data)


if __name__ == '__main__':
    main()


