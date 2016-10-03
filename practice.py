"""List Practice

Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.

    For example::

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """
    for item in items:
        print item


def long_words(words):
    """Return words in input list that longer than 4 characters.

    For example::

        >>> long_words(["hello", "a", "b", "hi", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

    (If there are duplicates, show both --- notice "bacon" appears
    twice in output)

    If no words are longer than 4 characters, return an empty list::

        >>> long_words(["all", "are", "tiny"])
        []
    """
    # long_words_list = []

    # for word in words:
    #     if len(word) > 4:
    #         long_words_list.append(word)
    long_words_list = [word for word in words if len(word) > 4]
    return long_words_list


def n_long_words(words, n):
    """Return words in list longer than `n` characters.

    For example::

        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "bacon", "bacon"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'bacon', 'bacon']

        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """

    # n_long_words_list = []

    # for word in words:
    #     if len(word) > n:
    #         n_long_words_list.append(word)
    n_long_words_list = [word for word in words if len(word) > n]
    return n_long_words_list


def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `min()`!

    For example::

        >>> smallest_int([-5, 2, -5, 7])
        -5

        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return `None`::

        >>> smallest_int([]) is None
        True
    """
    smallest_number = None

    for number in numbers:
        if len(numbers) == 0:
            return None
        elif smallest_number is None:
            smallest_number = number
        elif number < smallest_number:
            smallest_number = number
    return smallest_number


def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `max()`!

    For example::

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None::

        >>> largest_int([]) is None
        True
    """
    largest_number = None

    for number in numbers:
        if len(numbers) == 0:
            return None
        elif largest_number is None:
            largest_number = number
        elif number > largest_number:
            largest_number = number
    return largest_number


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.

    For example::

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off
    the half::

        >>> halvesies([1, 5])
        [0.5, 2.5]
    """
    # halvesies_list = []
    # for number in numbers:
    #     floated_number = float(number)
    #     halved_number = floated_number / 2
    #     halvesies_list.append(halved_number)
    halvesies_list = [(float(number) / 2) for number in numbers]
    return halvesies_list


def word_lengths(words):
    """Return the length of words in the input list.

    For example::

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """
    # word_lengths_list = []
    # for word in words:
    #     word_length = len(word)
    #     word_lengths_list.append(word_length)
    word_lengths_list = [len(word) for word in words]
    return word_lengths_list


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.

    For example::

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero::

        >>> sum_numbers([])
        0
    """
    sum_result = 0
    for number in numbers:
        sum_result += number
    return sum_result


def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.

    For example::

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in input, the product is zero::

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::

        >>> mult_numbers([])
        1
    """
    mult_result = 1
    for number in numbers:
        mult_result = mult_result * number
    return mult_result


def join_strings(words):
    """Return a string of all input strings joined together.

    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.

    For example::

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string::

        >>> join_strings([])
        ''
    """
    joint_result = None
    for word in words:
        string_length = len(words)
        if string_length == 0:
            string_joint_result = str(joint_result)
            string_joint_result = "''"
            joint_result = string_joint_result
            #Can't figure out how to return an empty string.
            #Can't figure out how to convert a None type into an empty string
        elif joint_result is None:
            joint_result = word
        else:
            joint_result += word
    return joint_result


def average(numbers):
    """Return the average (mean) of the list of numbers given.

    For example::

        >>> average([2, 4])
        3.0

    This should handle cases where the result isn't an integer::

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.

    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """

    average_sum = None

    for number in numbers:
        if len(numbers) == 0:
            print "The list argument provided is empty."
        elif average_sum is None:
            floated_number = float(number)
            average_sum = float(floated_number)
        else:
            floated_number = float(number)
            average_sum += floated_number
    average_result = average_sum / len(numbers)
    return average_result


def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".

    For example::

        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course::

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """
    joint_string = None

    for word in words:
        if len(words) == 1:
            joint_string = word
        elif joint_string is None:
            joint_string = word
        else:
            joint_string += ', ' + word

    return joint_string


def reverse_list(items):
    """Return the input list, reversed.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    You should do this without changing the original list::

        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """
    reversed_list = []
    for item in items:
        reversed_list.insert(0, item)
    return reversed_list


def reverse_list_in_place(items):
    """Reverse the input list `in place`.

    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]

        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """

    return items[::-1]
    #Couldn't figure this one using a for-loop and index, so I consulted the internet.
    #Actually this would need to be saved in a new list and doesn't return the list in place.


def duplicates(items):
    """Return list of words from input list which were duplicates.

    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.

    For example::

        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']

        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]

    You should do this without changing the original list::

        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']

        >>> orig
        ['apple', 'apple', 'berry']
    """
    items_seen = []
    items_seen_twice = []

    for item in items:
        if item in items_seen and item not in items_seen_twice:
            items_seen_twice.append(item)
        else:
            items_seen.append(item)
    items_seen_twice = sorted(items_seen_twice)
    return items_seen_twice


def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.

    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.

    **DO NOT** use the `list.index()` method.

    For example::

        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]

    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")

    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::

        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]

    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """
    find_letter_result = []
    # for word in words:
    #     if letter not in word:
    #             find_letter_result.append(None)
    #     else:
    #         # index_counter = 0
    #         # for interate_letter in enumerate(word):
    #         #     if interate_letter[index_counter] == letter:
    #         #         find_letter_result.append(index_counter)
    #         #         index_counter += 1
    #         split_word = word.split()
    #         # index_counter = 0
    #         for letter_index, split_word_letter in enumerate(split_word):
    #             if split_word_letter == letter:
    #                 find_letter_result.append(letter_index)
    #                 # index_counter += 1
    # return find_letter_result
    for word in words:
        if letter not in word:
            find_letter_result.append(None)
        else:
            split_word = list(word)
            for letter_index, split_word_letter in enumerate(split_word):
                if split_word_letter == letter:
                    find_letter_result.append(letter_index)
    return find_letter_result

#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
