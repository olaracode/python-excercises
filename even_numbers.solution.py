def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def even_numbers_only(lst):
    even_lst = []
    for num in lst:
        if is_even(num):
            even_lst.append(num)

    return even_lst
