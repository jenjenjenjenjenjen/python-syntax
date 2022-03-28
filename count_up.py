from tracemalloc import stop


def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    new_stop = stop + 1
    new_range = range(start, new_stop)
    for num in new_range:
        print(num)



count_up(5, 7)        
