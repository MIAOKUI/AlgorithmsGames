test1=[49,38,65,97,76,13,27,49,55,4]
test2=[]
test3=[49]
test4=list(range(10))[::-1]

def partition(l, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if l[i] < l[begin]:
            pivot +=1
            l[i],l[pivot] = l[pivot],l[i]
    l[begin],l[pivot] = l[pivot],l[begin]
    return pivot

def quick_sort(l, begin=0, end=None):
    if len(l) <=1:
        return l
    if not end:
        end = len(l)-1
    def _quick_sort(l, begin, end):
        if begin >= end:
            return
        pivot = partition(l, begin, end)
        _quick_sort(l, begin, pivot-1)
        _quick_sort(l, pivot+1, end)
        return l
    return _quick_sort(l, begin, end)


print(quick_sort(test1, 0, None))
print(quick_sort(test2, 0, None))
print(quick_sort(test3, 0, None))
print(quick_sort(test4, 0, None))






# def quick_sort(l, begin = 0, end = None):
#     if not end:
#         end = len(l)-1
#     if begin >= end:
#         return
#     pivot = _partition(array, begin, end)

#
# def _partition(array, begin, end):
#
