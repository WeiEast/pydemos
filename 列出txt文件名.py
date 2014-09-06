#! python3
import os
list = [ss for ss in os.listdir() if ss.endswith('.txt')]

print(list)
