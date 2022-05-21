def merge_list(list1, list2):
    result_list = []
    for num in list1:
        if num % 2 != 0:
            result_list.append(num)
    for num in list2:
        if num % 2 == 0:
            result_list.append(num)
    return result_list

list1 = [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]
print("result list:", merge_list(list1, list2))
