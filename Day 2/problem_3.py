sentence=input("Enter the sentence")
words_list=sentence.split()
words_tuple=tuple(word.upper() for word in words_list)

file_name='sentence_data.txt'
with open(file_name,'w') as writer:
    writer.write(f'List:{words_list} \n')
    writer.write(f'Tuple : {words_tuple}\n')

with open(file_name,'r') as reader:
    content=reader.read()

print("\nData Read from file")
print(content)