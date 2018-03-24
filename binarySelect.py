def binary_search(list,item):
    low = 0   #low 和 high用于跟踪要在其中查找的列表部分
    high = len(list)-1

    while low <= high:
        mid=(low+high)//2
        guess = list[mid]
        if guess == item:   #如果找到了元素
            return mid
        if guess > item:    #猜的数字大了
            high = mid - 1
        else:               #猜的数字小了
            low = mid + 1
    return None             #没有指定元素
if __name__=='__main__':
    my_list=[1,3,5,7,9,11,13,15,17]
    print(binary_search(my_list,13))
    print(binary_search(my_list,-1))
    print("修改了一些，用git找出")


