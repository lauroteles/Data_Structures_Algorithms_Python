class InsertionSort:
    def __init__(self,my_list):
        self.my_list = my_list

    def insertion_sort(self):
        self.__insertion_sort()
        

    def __insertion_sort(self):
        for i in range(1,len(self.my_list)):
            temp = self.my_list[i]
            j = i-1
            while temp < self.my_list[j] and j > -1:
                self.my_list[j+1] = self.my_list[j]
                self.my_list[j] = temp
                j -= 1




print("Selection Sort")
selection_sort = InsertionSort([5,3,8,6,7,2])
selection_sort.insertion_sort()
print(selection_sort.my_list) # [2,3,5,6,7,8]     