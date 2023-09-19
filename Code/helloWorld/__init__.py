import math
# print("hello world")
# num = 10
# print(num)
# print(math.sin(1))

# BMI= 体重/（身高*2）
# weight = input("请输入您的体重")
# print(weight)
# height = input("请输入您的身高")
# print(height)
# BMI =float(height) / (float(weight) ** 2)
# print("您的BMI指数为"+str(BMI))

print_num = input("请输入任意多的数字，当输入q后终止程序：")
total = 0
count = 0
while print_num != "q":
    num = float(print_num)
    total = total + num
    count = count + 1
    print_num = input("请输入任意多的数字，当输入q后终止程序：")

if count == 0:
    result = 0
else:
    result = total / count
print(result)