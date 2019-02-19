import random
from datetime import datetime

import os.path


def generate_numbers(size_of_numbers):
    file = '../numbers' + str(size_of_numbers) + '.txt'
    if os.path.exists(file):
        return 1
    else:
        print("Start generating %d numbers..." % size_of_numbers)
        random.seed(datetime.now())
        numbers = [random.randint(1, size_of_numbers ** 2) for i in range(1, size_of_numbers + 1)]
        # print(numbers)
        with open(file, 'w') as f:
            for i in numbers:
                f.write("%i\n" % i)
        print("File is ready")
