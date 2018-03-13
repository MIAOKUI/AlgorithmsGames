def merge(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(l):
    if len(l) <=1:
        return l
    mid = len(l)//2
    left = merge_sort(l[0:mid])
    right = merge_sort(l[mid:])
    sorted = merge(left, right)
    return sorted


test1 = [49, 38, 65, 97, 76, 13, 27, 49, 55, 4]
test2 = []
test3 = [49]

print(merge_sort(test1))
print(merge_sort(test2))
print(merge_sort(test3))