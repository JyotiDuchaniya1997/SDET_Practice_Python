def pair_equals_sum_target(list1, exp_sum):
    pairs=[]
    for i in range(1, len(list1)):
        if list1[i]+list1[i-1] == exp_sum:
            pairs.append([list1[i-1], list[i]])
    return pairs

list=[3,5,6,4,7,3]
pairs1= pair_equals_sum_target(list, 10)
print(pairs1)