# Merge Sort

def merge_sort(list_of_data, start_index, mid_index):
    lhs = list_of_data[start_index:mid_index+1]
    rhs = list_of_data[mid_index+1:]
    print(lhs, rhs)
    lhs_out = lhs
    rhs_out = rhs
    if len(lhs) > 1:
        lhs_out = merge_sort(lhs, 0, int(len(lhs)/2)-1)
    if len(rhs) > 1:
        rhs_out = merge_sort(rhs, 0, int(len(rhs)/2)-1)

    output = []
    while (len(lhs_out) > 0 or len(rhs_out) > 0):
        l0 = 0
        if (len(lhs_out) > 0):
            l0 = lhs_out[0]
            lhs_out = lhs_out[1:]

if __name__ == "__main__":
    print("Merge Sort")

    #        0, 1, 2, 3,  4,  5,  6, 7
    data = [42, 9, 8, 1, 12, 40, 32, 2]
    print(data)

    merge_sort(data, 0, 3)