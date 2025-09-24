
def check(temperature):
    print("欢迎来到黑马程序员！请出示你的核酸证明，并配合检查")
    if temperature<=37.5:
        print(f"体温测量中，您的体温是:{temperature}度，体温正常，请进！")
    else:
        print(f"体温测量中，您的体温是:{temperature}度，体温不正常，需要隔离！")

check(37.6)