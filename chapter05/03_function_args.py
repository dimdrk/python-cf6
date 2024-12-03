def test_args_func(pos_arg1, pos_arg2, opt_arg1=None, opt_arg2=None, *args, **kwargs):
    """
    Function demonstrates the usage of positional, optional, additional positional args (*args)
    and additional keyword arguments (**kwargs).

    Parameters:
        pos_arg1: The first positional argument.
        pos_arg2: The second positional argument.
        opt_arg1: The first optional argument.
        opt_arg2: The second optional argument.
        *args: VarArgs.
        **kwargs: Keyword arguments.
    """
    # printing positional arguments
    print(f"pos_arg1: {pos_arg1}")
    print(f"pos_arg1: {pos_arg2}")
    
    # printing optional arguments
    print(f"opt_arg1: {opt_arg1}")
    print(f"opt_arg2: {opt_arg2}")

    # printing the *args
    if args:
        print("Additional positional arguments")
        for arg in args:
            print(arg)

    # printing additional keyword arguments
    if kwargs:
        print("Additional keyword arguments")
        for key, value in kwargs.items():
            print(f"{key}: {value}")

def main():
    test_args_func("Hello", "CF6", opt_arg1=100, opt_arg2=200)

    print("--------------------")
    test_args_func("Hello", "CF6", opt_arg1=10, keyw_arg1="Python", keyw_arg2="Android")

    print("--------------------")
    test_args_func(
        "Hello", "CF6",                             # pos_arg1, pos_arg2
        100, 200,                                    # opt_arg1, opt_arg2
        300, 400,                                    # *args
        keyw_arg1="Python", keyw_arg2="Android"     # **kwargs
    )

if __name__ == "__main__":
    main()