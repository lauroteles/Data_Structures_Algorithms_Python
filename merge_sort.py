
class Merge_sort:
    
    @staticmethod
    def merge(list1,list2):
        combined = []
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                combined.append(list1[i])
                i += 1
            else:
                combined.append(list2[j])
                j+=1
        while i < len(list1):
            combined.append(list1[i])
            i += 1
        while j < len(list2):
            combined.append(list2[j])
            j += 1
              
        return combined                             
    
    def merge_sort_2(self, my_list):
        if len(my_list) == 1:
            return my_list
        mid_index = int(len(my_list)/2)
        left = self.merge_sort_2(my_list[:mid_index])
        right = self.merge_sort_2(my_list[mid_index:])

        return self.merge(left,right)
    



merge_srt = Merge_sort().merge_sort_2([5,3,8,6,7,2]) # [2,3,5,6,7,8]
print(f'----- Merge Sort 2 \n', merge_srt)

merge_sort = Merge_sort.merge([2,3,5],[6,7,8]) # [2,3,5,6,7,8]
print(f'----- Merge Sort \n', merge_sort)    