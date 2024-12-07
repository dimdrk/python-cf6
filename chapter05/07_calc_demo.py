import functools
# from functools import reduce

def calculate(args):
    def plus():
        return functools.reduce(lambda x, y: x + y, args)

    def minus():
        return functools.reduce(lambda x, y: x - y, args, 0)

    def mul():
        return functools.reduce(lambda x, y: x * y, args)

    def div():
        # if not 0 in args[1:]      <-- alternative senario
        if sum(args[1:]) != 0:
            return args[0] / sum(args[1:])

    return plus, minus, mul, div

def main():
    ints_list = [1, 2, 3, 4, 5]

    add_func, minus_fun, mul_func, dic_func = calculate(ints_list)

    print("add_func:", add_func())
    print("minus_fun:", minus_fun())
    print("mul_func:", mul_func())
    print("dic_func:", dic_func())

    # print("add_func:", plus)

if __name__ == "__main__":
    main()