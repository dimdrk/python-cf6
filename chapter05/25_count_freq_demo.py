from collections import Counter

def count_with_dict_compr(my_list):
    freq_dict = { item : my_list.count(item) for item in set(my_list) }
    print("Count with dict compr:", freq_dict)

def count_with_manual_loop(my_list):
    freq_dict = {}
    for item in my_list:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    print("Count with manual loop:", freq_dict)

def count_with_get_method(my_list):
    freq_dict = {}
    for item in my_list:
        freq_dict[item] = freq_dict.get(item, 0) + 1
    print("Count with get method:", freq_dict)

def count_with_counter(my_list):
    freq_dict = Counter(my_list)
    print("Count with Counter:", freq_dict)

    sorted_by_freq = freq_dict.most_common()
    print("Sorted dict:", sorted_by_freq)


def main():
    my_list = ["apple", "banana", "kiwi", "apple", "orange", "banana", "apple", "kiwi", "melon", "kiwi", "kiwi"]

    count_with_dict_compr(my_list)

    count_with_manual_loop(my_list)

    count_with_get_method(my_list)

    count_with_counter(my_list)
    

if __name__ == '__main__':
    main()