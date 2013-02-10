import sys

#line = sys.stdin.readline()
result = []
for line in sys.stdin:
    num1, num2 = (long(num) for num in line.split(" "))

    if num1 > num2:
        result.append(num1 - num2)
    else:
        result.append(num2 - num1)

for i in range(len(result) - 1):
    sys.stdout.write("%d\n" % result[i])

sys.stdout.write("%d" % result[len(result) - 1])
