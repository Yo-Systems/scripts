# Using list comprehension
List = [list_of_words[i:i + 3]
for i in range(len(list_of_words) - 2)]

# printing list
print(List)