marks = {
    "Alice":86,
    "Bob":87,
    "Charlie":88,
    "David":89,
    "Eve":90,
    "Frank":91,
    "George":92,
    "Harriet":93,
    "Ilean":94
}
nm = input("Enter student\'s name: ")
mark=marks.get(nm)
if(mark==None):
    print("Student not found")
else:
    print(f"{nm}'s mark : {mark}")