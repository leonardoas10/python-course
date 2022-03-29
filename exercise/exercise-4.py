import random
import datetime

random_between_zero_one = random.randrange(0,2)
random_between_one_ten = random.randrange(1,11)

date_between_zero_one = datetime.time(random_between_zero_one)
date_between_one_ten = datetime.time(random_between_one_ten)

print(date_between_zero_one, date_between_one_ten)