#Program to create tuples of tuples and compute sum of all inner values.
tuples_of_tuples = ((1, 2), (3, 4), (5, 6))
total_sum = 0
for inner_tuple in tuples_of_tuples:
    total_sum += sum(inner_tuple)
    print(f"Sum of {inner_tuple} is {sum(inner_tuple)}")
    print(f"Total sum is {total_sum}")
    