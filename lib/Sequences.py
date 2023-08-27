def remove_duplicates(sequence):
    unique_elements = []
    seen = set()

    for item in sequence:
        if item not in seen:
            unique_elements.append(item)
            seen.add(item)

    return unique_elements

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5,12 ,15, 22, 23, ]
result = remove_duplicates(input_sequence)
print(result)  

