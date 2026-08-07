# water_level=10
# stone=0
# while water_level<100:
#     stone=stone+1
#     water_level=water_level+10
# print("在投入第",stone,"块石头时水位满了")

password = '114514'
while input('请输入密码：') != password:
    print("密码错误,请重新输入")
print("密码正确")

person = {
    "张三":{"性别":"男","年龄":"18","id":"10010"},
    "李四":{"性别":"女","年龄":"21","id":"10011"},
    "王五":{"性别":"男","年龄":"29","id":"10012"},
    "赵六":{"性别":"女","年龄":"30","id":"10013"},
}
name = input('输入姓名')
print(person[name])
if input("删除信息?(y/n)") == "yes":
    del person[name]
else:
    print("已取消")
print("已完成")