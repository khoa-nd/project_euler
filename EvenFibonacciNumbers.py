__author__ = 'NguyenDangKhoa'

result = [1, 1]
n = 2
result.append(result[n - 2] + result[n - 1])
while result[n] <= 4000000:
    n += 1
    result.append(result[n - 2] + result[n - 1])

print n - 1
print result

total = 0
for item in result:
    if item % 2 == 0:
        total += item

print total
