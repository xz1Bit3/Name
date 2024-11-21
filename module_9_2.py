first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
first_result = [len(x) for x in first_strings if len(x) > 5]
print(first_result)

second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
second_result =[(x,y) for x in second_strings for y in second_strings if len(x)==len(y)]
print(second_result)

third_result = {x:len(x) for x in first_strings + second_result if not len(x) %2}
print(third_result)