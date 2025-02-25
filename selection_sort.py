class SelectionSort:
    def __init__(self,my_list):
        self.my_list = my_list

    def selection_sort(self):
        self.__selection_sort()
        

    def __selection_sort(self):
        for i in range(len(self.my_list)-1):
            min_index = i
            for j in range(i+1, len(self.my_list)):
                if self.my_list[j] < self.my_list[min_index]:
                    min_index = j
            if i != min_index:
                temp = self.my_list[i]
                self.my_list[i] = self.my_list[min_index]
                self.my_list[min_index] = temp 
        return self.my_list     

print("Selection Sort")
selection_sort = SelectionSort([5,3,8,6,7,2])
selection_sort.selection_sort()
print(selection_sort.my_list) # [2,3,5,6,7,8]                  