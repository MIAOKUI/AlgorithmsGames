test1=[49,38,65,97,76,13,27,49,55,4]
test2=[]
test3=[49]

def simple_selection_sort(l):
    length = len(l)
    if length <=1:
        return l
    for i in range(length):
        min_idx = i
        for j in range(i+1, length):
            if l[j] < l[min_idx]:
                min_idx = j
        l[min_idx],l[i] = l[i], l[min_idx]
    return l

print(simple_selection_sort(test1))
print(simple_selection_sort(test2))
print(simple_selection_sort(test3))
