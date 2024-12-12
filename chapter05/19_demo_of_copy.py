import copy

def main():
    ages = [10, [20, 30, 40], 50]

    # Methods to create copies
    # Shallow copies
    ages_slice = ages[:]
    ages_cp = ages.copy()
    ages_list = list(ages)
    # Deep copy
    ages_dcp = copy.deepcopy(ages)

    print("Original list:", ages)
    print("Slicing ages:", ages_slice)
    print("list() ages:", ages_list)
    print("Deep copy:", ages_dcp)

    # Modify the original list
    ages[0] = 100
    ages[1][0] = 200

    print("After modification:")
    print("Original list:", ages)
    print("Slicing ages:", ages_slice)
    print("list() ages:", ages_list)
    print("Deep copy:", ages_dcp)



if __name__ == '__main__':
    main()