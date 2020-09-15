l1=[10,50,66,25,44,78]
print("List 1: ",l1)

l1.sort()#it will sort the elements of list1
print("sorted list 1",l1)

def search_l1():
    i = int(input("Enter element to search in the list:"))
    if i in l1:
        print("The element is in the list")
    else:
        print("The element is not in the list")
        
search_l1()

def reverse_list():
    print("Reversing the list1: ",l1[::-1])
    
reverse_list()

l2 = ["car", "pen", "book", "crayons"]
print("List 2: ",l2)

l2.sort() # it will sort the elements of list2
print("sorted list 2 :", l2)

def merge_list():
    l3 = l1 + l2
    print("Merging both the lists: ", l3)

merge_list()
