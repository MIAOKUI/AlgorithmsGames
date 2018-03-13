test1=[49,38,65,97,76,13,27,49,55,4]
test2=[]
test3=[49]


def Buble_sort(array):
    counts = len(array)
    for i in range(counts):
        for j in range(i+1, counts):
            if array[j] < array[i]:
                array[j],array[i] = array[i], array[j]
    return array

def insertSort(array):
    counts = len(array)
    for i in range(counts):
        cur = array[i]
        j = i-1
        while j >=0:
            if cur < array[j]:
                array[j+1] = array[j]
                array[j] = cur
                j -=1
            else:
                break
    return array


def quick_sort(l, begin = 0, end = None):
    if not end:
        end =  len(l) -1
    if len(l) <= 0:
        return l
    def _quick_sort(l, begin, end):
        if begin >= end:
            return
        pivot = _partition(l, begin, end)
        _quick_sort(l, begin, pivot-1)
        _quick_sort(l, pivot+1, end)
        return l
    return _quick_sort(l, begin, end)


def _partition(l, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if l[i] < l[begin]:
            pivot +=1
            l[pivot],l[i] = l[i], l[pivot]
    l[begin],l[pivot] = l[pivot],l[begin]
    return pivot


def merge_sort(l):
    if len(l) <= 1:
        return l
    mid = len(l)//2
    left = merge_sort(l[0:mid])
    right = merge_sort(l[mid:])
    return _merge(left, right)


def _merge(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


# print(Buble_sort(test1))
# print(Buble_sort(test2))
# print(Buble_sort(test3))

# print(insertSort(test1))
# print(insertSort(test2))
# print(insertSort(test3))

# print(quick_sort(test1))
# print(quick_sort(test2))
# print(quick_sort(test3))

print(merge_sort(test1))
print(merge_sort(test2))
print(merge_sort(test3))