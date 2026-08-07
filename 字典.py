person = {
    "zhangsan":{"sex":"male","age":"18","id":"10010"},
    "lisi":{"sex":"male","age":"21","id":"10011"},
    "wangwu":{"sex":"male","age":"29","id":"10012"},
    "zhaoliu":{"sex":"male","age":"30","id":"10013"},
}
name = input('name')
print(person[name])
if input("Delete the message?(y/n)") == "yes":
    del person[name]
else:
    print("Canceled")
print(person)