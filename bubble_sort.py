def swap(my_list,i,j):
    temp=my_list[i]
    my_list[i]=my_list[j]
    my_list[j]=temp
    return my_list
    
    
def bubble_sort(my_list):
    itr=len(my_list)-1
    for i in range(itr+1):
        for j in range(itr+1):
            if (my_list[i]<my_list[j]):
                my_list=swap(my_list,i,j)
    return my_list
    
    
my_list=[7,5,8,3,9,10,1]
print(bubble_sort(my_list))



