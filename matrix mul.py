class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def multiply(self, other):
        result = []

        for i in range(len(self.mat)):
            row = []
            for j in range(len(other.mat[0])):
                sum = 0
                for k in range(len(other.mat)):
                    sum = sum + self.mat[i][k] * other.mat[k][j]
                row.append(sum)
            result.append(row)

        return result


m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

res = m1.multiply(m2)

print("Result:")
for r in res:
    print(r)

