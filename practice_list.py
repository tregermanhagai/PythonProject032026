kids_list = ["Alice", "Bob", "Charlie", "Alice"]
kids_list.append("David")
kids_list.append("David")

for kid in kids_list:
    print(kid) # Alice, Bob, Charlie, Alice, David
    
print("Total number of kids:", len(kids_list)) # Total number of kids: 5
print(kids_list)

kids_list.sort()
print(kids_list)
kids_list.reverse()
print(kids_list)