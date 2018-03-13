test1=[49,38,65,97,76,13,27,49,55,4]
test2=[]
test3=[49]

def insert_sort(l1):
    if not l1:
        return l1
    for i in range(1, len(l1)):
        j = i -1
        key = l1[i]
        # print(key)
        while j>=0:
            if key <l1[j]:
                l1[j+1] = l1[j]
                l1[j] = key
                # print(l1)
            j -=1
    return l1



print(insert_sort(test1))
print(insert_sort(test2))
print(insert_sort(test3))

