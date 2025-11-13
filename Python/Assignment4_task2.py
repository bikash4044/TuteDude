content1 = input("Enter text to write to the file:")
with open("output.txt", "w") as f:
    f.write(content1+"\n")
print("Data Successfully written to the output.txt")

content2 = input("Enter text to append to the file:")
with open("output.txt", "a") as f:
    f.write(content2)
print("Data Successfully appended to the output.txt")

print("Final contents of output.txt")
with open("output.txt", "r") as f:
    print(f.read())