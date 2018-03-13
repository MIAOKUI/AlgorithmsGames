
def bubble_sort(l):
    counts = len(l)
    for i in range(counts):
        for j in range(i+1, counts):
            if l[j] < l[i]:
                l[i],l[j] = l[j], l[i]
    return l


test1 = [49, 38, 65, 97, 76, 13, 27, 49, 55, 4]
test2 = []
test3 = [49]

print(bubble_sort(test1))
print(bubble_sort(test2))
print(bubble_sort(test3))