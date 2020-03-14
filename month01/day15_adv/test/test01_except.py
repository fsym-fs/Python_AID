def get_score():
    n = input("请输入成绩:")
    try:
        return int(n)
    except ValueError:
        print("请输入正确的成绩!")
        return 0
print(get_score())