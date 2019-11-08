def swapPositions(list,pos1,pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def bubble_sort(array):
    counter=-1
    length = len(array)
    while counter!=0:
        counter=0
        for i in range(0,length-1):
            if array[i]>array[i+1]:
                swapPositions(array,i,i+1)
            counter+=1
        length-=1
    return array
print(bubble_sort( [25,15,17,1,-32,7,8,33,9] ))