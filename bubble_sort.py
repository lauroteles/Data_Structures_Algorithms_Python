def bubble_sort(my_list):
        for i in range(len(my_list) -1, 0,-1):
            for j in range(i):
                if my_list[j] > my_list[j+1]:
                    temp = my_list[j]
                    my_list[j] = my_list[j+1]
                    my_list[j+1] = temp
        return my_list               


print(bubble_sort([5,3,8,6,7,2])) # [2,3,5,6,7,8]