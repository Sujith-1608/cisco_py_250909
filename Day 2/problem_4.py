sentence=input("Enter names: ")
names_list=sentence.split()
names_list.sort()
print(names_list)
names_tuple=tuple(names_list)

file_name="names_data.txt"
with open(file_name,'w') as writer:
    writer.write(f"Sorted_list: {names_list}\n")
    writer.write(f"Sorted_tuple: {names_tuple}")


with open(file_name,'r') as reader:
    content=reader.read()

print("\nData Read from file")
print(content)