class Sort:
    def bubblesort(self,arr):
        arr_len = len(arr)
        for i in range(arr_len-1):
            for j in range(arr_len-1-i):
                if arr[j] > arr[j+1]:
                    temp = arr[j+1]
                    arr[j+1] = arr[j]
                    arr[j] = temp
        return arr
    
    def selectionsort(self, arr):
        arr_len = len(arr)
        for i in range(arr_len -1):
            minindex = i
            for j in range(i,arr_len-1):
                if arr[j] < arr[minindex]:
                    minindex = j
            temp = arr[i]
            arr[i] = arr[minindex]
            arr[minindex] = temp
        return arr

    def insertionsort(self, arr):
        arr_len = len(arr)
        for i in range(1,arr_len):
            current = arr[i]
            preindex = i -1
            while arr[preindex] > current and preindex >= 0:
                arr[preindex + 1] = arr[preindex]
                preindex = preindex -1
            arr[preindex+1] = current
        return arr

    def shellsort(self,arr):
        arr_len = len(arr)
        gap = 1
        while (gap < arr_len/3):
            gap = gap * 3 + 1
        while gap > 0:
            for i in range(gap,arr_len):
                temp = arr[i]
                j = i - gap
                while j>0 and arr[j] > temp:
                    arr[j+gap] = arr[j]
                    j = j - gap
                arr[j+gap] = temp
            gap = int(gap/3)
        return arr

    def merge(self, left, right):
        result = []
        while (len(left) > 0 and len(right) > 0):
            if (left[0] > right[0]):
                result.append(right[0])
                right.pop(0)
            else:
                result.append(left[0])
                left.pop(0)
        while(len(left) > 0):
            result.append(left[0])
            left.pop(0)
        while(len(right) > 0 ):
            result.append(right[0])
            right.pop(0)
        return result

    def mergesort(self, arr):
        arr_len = len(arr)
        if (arr_len < 2 ):
            return arr
        middle = int(arr_len/2)
        left = arr[:middle]
        right = arr[middle:]
        return self.merge(self.mergesort(left), self.mergesort(right))


arr = [1,3,2,54,2,2,4,6,7,3]
t = Sort()
# t.bubblesort(arr)
# t.selectionsort(arr)
# t.insertionsort(arr)
# t.shellsort(arr)
t.mergesort(arr)
             