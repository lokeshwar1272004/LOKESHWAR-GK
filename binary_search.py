
def binary_search(number_list,find_num):
    l = 0
    u = len(number_list) - 1
    mid_index = (l + u) // 2
    mid_number = number_list[mid_index]

    while l <= u:
        mid_index = (l + u) // 2
        mid_number = number_list[mid_index]

        if mid_number == find_num:
            return mid_index
        if mid_number <= find_num: #[1,2,3,4,5,6]
            l = mid_index +1

        else:
            u = mid_index - 1
    return -1



number_list = [1,2,3,4,5]
print("....",len(number_list))
find_num = 5
print(binary_search(number_list,find_num))