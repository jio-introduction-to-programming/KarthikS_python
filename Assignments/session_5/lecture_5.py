
#Question 1 
def lst_sum(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]

    return sum

lst_1=[120,240,340,450,560]
sum = lst_sum(lst_1)
print(sum) 

#Question 2
def lst_max(lst):
    max = lst[0]
    for element in lst:
        if element > max:
            max = element
    return max

max_num = lst_max(lst_1)
print(max_num)


#question 3
def reverse_lst(lst):
    reverse = []
    for i in range(len(lst)):
        reverse.insert(0, lst[i]) 
    return reverse


array_1 = [1,2,3,4,5,6,7,8,9]
ulta = reverse_lst(array_1)
print(ulta)

#question 4
test_array = [23,94,55,32,87,2,4,8,23,583,9,7,8,4]

def sort_lst(array):
    for i in range(1,len(array)): # To iterate throught the elements from the unsorted sub array
        key = array[i]
        j = i - 1
        while j>=0 and key<array[j]: # if the key element is smaller than its previous element
            
            array[j], array[j+1]=array[j+1],array[j] # swap the key element with its previous elememt
            j = j - 1
            
        
    print("Sorted array: ", array)

sort_lst(test_array)


#question 5

def statistic(lst):
    mean_1 = sum(lst)/len(lst) 
    mode_1 = []
    for item in lst:
        mode_1[item] = mode_1.get(item, 0) + 1

    mode = max(mode_1, key=mode_1.get)

    return mean_1, mode_1

avearge_1, common_1 = statistic(test_array)
print(mean_1)
print(mode_1)


def sum_matrix():
    lst=[]
    print("please enter minimum 5 numbers")
    lst = input()
    k = int(input("enter a number"))
    a, b = int(input(" please enter 2 more numbers - "))
    for i in range(a,b):
        sum += sum[i]
    return sum

