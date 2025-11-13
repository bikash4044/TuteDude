try:
    with open("sample.txt", "r") as file:
        content = file.readlines()
        for i in content:
            print(i,end='')
except FileNotFoundError:
    print("The file \'sample.txt\' does not exist")
