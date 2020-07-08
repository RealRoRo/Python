
class BinarySearch:

    def __init__(self, a: list, ele):
        a = list.sort(a)
        self.a = a
        self.ele = ele
        first = 0
        last = int(len(a))
        mid = int((first + last) / 2)
        self.search(a, ele, first, last, mid)

    def search(a: list, ele, first, last, mid):
        if a[mid] == ele:
            return True
        if first > last:
            return False
        mid = int((first + last) / 2)
        if mid > ele:
            return search(a, ele, first, last -1, mid)
        elif mid < ele:
            return search(a, ele, first+1, last, mid)

        # list.sort(a)
        # first = 0
        # last = len(a)
        # while first < last:
        #     mid: int = int((first + last) / 2)
        #     if a[mid] == ele:
        #         return True
        #     elif mid > ele:
        #         last = mid - 1
        #     elif mid < ele:
        #         first = mid + 1
        # return False
