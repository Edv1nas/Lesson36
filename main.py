# import sys

# nums_square_lc = [num**2 for num in range(10000)]
# nums_square_gc = (num**2 for num in range(10000))

# print(f"List mem size is: {sys.getsizeof(nums_square_lc)}")
# print(f"Generator mem size is: {sys.getsizeof(nums_square_gc)}")

"""1. Create a generator function that takes a positive integer n as input and generates all the even numbers up to and including n."""

# import sys
# from collections.abc import Iterator

# def generate_even_numbers(num: int) -> Iterator[int]:
#     for number in range(2, num+1, 2):
#         yield number

# for even_numbers in generate_even_numbers(100):
#     print(even_numbers)

# print(f"Generator mem size is: {sys.getsizeof(generate_even_numbers)}") #check size of function

"""2. Create a generator function that would pick word from a generator and/list of generated random words (should be > 10000) and would stop itterating
until the word longer than 7 lettters is found.
Compare sizes of list and generator. Calculate performance per both executions (time to complete in ms) """

from collections.abc import Iterator
from py_random_words import RandomWords
import time

random_words = RandomWords()

def generate_random_words() -> int:
    random_words_list=[]
    for items in range(30000):
        items = random_words.get_word()
        random_words_list.append(items)
        sorted_list = " ".join(sorted(random_words_list))
    return sorted_list

rand_w = generate_random_words()


def generate_random_words_list() -> Iterator[str]:
    for value in rand_w:
        if len(value) > 7:
            yield value


start_gen = time.time()
random_word_list_gen = generate_random_words_list()
stop_gen = time.time()

start_list = time.time()
random_word_list = [word for word in rand_w if len(word) > 7]
stop_list = time.time()


print(f"Generator time taken: {stop_gen - start_gen:.4f} seconds")
print(f"List time taken: {stop_list - start_list:.4f} seconds")