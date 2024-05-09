# Merge Sort

def merge_sort(list_of_data, start_index, mid_index):
    """
    An implementation of Merge Sort
    
    Parameters
    ----------
    `list_of_data` : `Any[]`
        A list of data.
    `start_index` : `int`
        The index of list_of_data to start sorting from.
    `mid_index` : `int`
        The middle index of list_of_data.
    
    Returns
    -------
    `Any[]`
        A sorted list containing the same data as `list_of_data` but sorted
        in ascending numerical order.
    """
    # Split the data list into halves.
    lhs = list_of_data[start_index:mid_index+1]
    rhs = list_of_data[mid_index+1:]
    print(lhs, rhs, end=", ")

    # Give default values to the result of merge-sorting the halves
    # in case they are too short to be sorted.
    lhs_out = lhs
    rhs_out = rhs

    # Merge-sort the halves, if they have enough elements.
    if len(lhs) > 1:
        lhs_out = merge_sort(lhs, 0, int(len(lhs)/2)-1)
    if len(rhs) > 1:
        rhs_out = merge_sort(rhs, 0, int(len(rhs)/2)-1)

    # Create a blank output.
    output = []

    # Whilst either of the sorted halves have values
    while (len(lhs_out) > 0 or len(rhs_out) > 0):
        if (len(lhs_out) <= 0):
            # Remove the first value of the right half and add it to the output.
            output.append(rhs_out.pop(0))
            continue
        if (len(rhs_out) <= 0):
            # Remove the first value of the left half and add it to the output.
            output.append(lhs_out.pop(0))
            continue

        if (lhs_out[0] < rhs_out[0]):
            output.append(lhs_out.pop(0))
        else:
            output.append(rhs_out.pop(0))
    print(output)
    # Return the complete output list.
    return output

if __name__ == "__main__":
    print("Merge Sort")

    #        0, 1, 2, 3,  4,  5,  6, 7
    data = [42, 9, 8, 1, 12, 40, 32, 2]
    print(data)

    print(merge_sort(data, 0, 3))