class SnapshotArray:

    def __init__(self, length: int):
        # (list of list) for histories in a list of input length 
        self.histories = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0
        

    def set(self, index: int, val: int) -> None:
        self.histories[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        left, right = 0, len(self.histories[index]) - 1
        pos = -1

        while left <= right:
            mid = (left + right) // 2
            if self.histories[index][mid][0] <= snap_id:
                pos = mid
                left = mid + 1
            else:
                right = mid - 1
        return self.histories[index][pos][1]



# class SnapshotArray:

#     def __init__(self, length: int):
#         self.length=length
#         self.data=[{0:0} for _ in range(length)]
#         self.snap_id=0
        

#     def set(self, index: int, val: int) -> None:
#         self.data[index][self.snap_id]=val
        

#     def snap(self) -> int:
#         self.snap_id+=1
#         return self.snap_id-1
        

#     def get(self, index: int, snap_id: int) -> int:
#         while snap_id >= 0 and snap_id not in self.data[index]:
#             snap_id -= 1
#         return self.data[index][snap_id]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
