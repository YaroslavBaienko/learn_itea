import numpy as np
import random
from datetime import datetime

# start = datetime.now()
# print(f"Start at {start}")
# a1D = np.array(([num for num in range(100000000)], [num for num in range(10000000)]), dtype=object)
# print("Array created")
# middle = datetime.now() - start
# print(middle)
# collector = {}
# for item in a1D[0]:
#     item = item * 100 / 2 + 434 % 24
#     for symbol in str(item):
#         collector[symbol] = random.randrange(1, 100000000)
# print(collector)
# end = datetime.now() - start
# print(end)
test = np.diag([24, 244, 344])
print(test)
