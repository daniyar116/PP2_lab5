def all_true_elements(tuple_values):
    return all(tuple_values)

tuple_values = (True, True, False, True)
if all_true_elements(tuple_values):
    print(f"All elements in the tuple are True.")
else:
    print(f"Not all elements in the tuple are True.")