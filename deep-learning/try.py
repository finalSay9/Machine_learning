
input0 = [1,2,3,4,5]
input1 = [1,3,4,6,9]
sum = 0
for i in zip(input0, input1):
    result = input0[i] * input1[i]
    sum += result
print(sum)