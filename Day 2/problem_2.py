integers_str=input("Enter integers, separated by spaces: ")
integers=list(map(int,integers_str.split()))
print(integers)
sum =sum(integers)
print(f"Sum: {sum}")
average=sum/len(integers)
print(f"Average: {average}")

file_name="numbers_data.txt"

with open(file_name,'w') as writer:
    writer.write(f"SUM: {sum}\n")
    writer.write(f"Average: {average}")

with open(file_name,'r') as reader:
    line_sum= reader.readline()
    line_average=reader.readline()
    print(line_sum)
    print(line_average)