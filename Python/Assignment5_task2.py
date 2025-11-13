lis = [i for i in range(1,11)]
five = lis[:5]
rv = five.copy()
rv.reverse()
print("Original List: ",lis)
print("Extracted first five elements: ",five)
print("Reversed extracted elements : ",rv)