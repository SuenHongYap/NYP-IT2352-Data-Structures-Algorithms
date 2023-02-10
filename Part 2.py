import collections
numbers_list = [1, 2, 3, 3, 4, 4, 4, 10, 10, 10]
count=0

occurrences= collections.Counter(numbers_list)
for key in occurrences:
    if occurrences[key] > 1:
        extra_occurrence=occurrences[key]-1
        no_of_time_occur = extra_occurrence*(extra_occurrence+1)/2
        for u in range(int(no_of_time_occur)):
            print("X=%s,"%key, "Y=%s"%key)
            count+=1


print("Total match is %s. "%count)
