import random
import string
def generate_random_name() :
        while True :
            random_string = ''.join(random.choices(string.ascii_letters, k=15))
            yield random_string
gen = generate_random_name()
try:
    for _ in range(9):
        print(next(gen))
except StopIteration:
    print("Генератор исчерпан")