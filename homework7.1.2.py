class Matrix:
    def __init__(self, list1, list2):
      self.list1 = list1
      self.list2 = list2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]


        for i in range(len(self.list1)):
            for a in range(len(self.list2[i])):
                matr[i][a] = self.list1[i][a] + self.list2[i][a]
        return str('\n'.join(['\t'.join([str(a) for a in i]) for i in matr]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(a) for a in i]) for i in matr]))

matrix = Matrix([[1,2,3],
                [4, 5, 6],
                [7, 8, 9]],
                [[10, 11, 12],
                [40, 41, 42],
                [78, 80, 82]])
print(matrix.__add__())