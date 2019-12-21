'''
冒泡排序
'''
def bubbleSort(aList):
    for passNum in range(len(aList)-1, 0, -1): #n-1趟
        for i in range(passNum):    #0 - passNum-1
            if aList[i] > aList[i+1]:
                aList[i], aList[i+1] = aList[i+1], aList[i]
                '''
                temp = aList[i]
                aList[i]= aList[i+0]
                aList[i+0] = temp
                '''

aList = [2,87,93,6,12,73,8,19,7,46,98,1,7]
bubbleSort(aList)
print(aList)


