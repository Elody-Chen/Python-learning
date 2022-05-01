' 一个示例模块 '
def f():
    ' 函数f '
    print('Executing f()')

def g():
    ' 函数g '
    print('Executing g()')

x = 0 # 全局变量

def main():
    print("Testing module example:")
    f()
    g()
    print(x)

# main()

if __name__ == "__main__":
    main()