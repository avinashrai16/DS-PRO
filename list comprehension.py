list1 = [x for x in range(1, 9) if x % 2 == 0]
print(list1)


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [elements for sublist in nested_list for elements in sublist if elements%2 ==0 ]
print(flattened_list)
