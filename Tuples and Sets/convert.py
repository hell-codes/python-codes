#Program to conver list into tuples and tuples into list.
list_data = [1, 2, 3, 4, 5]
tuple_data = (6, 7, 8, 9, 10)
converted_to_tuple = tuple(list_data)
converted_to_list = list(tuple_data)
print(f"List converted to Tuple: {converted_to_tuple}")
print(f"Tuple converted to list: {converted_to_list}")
