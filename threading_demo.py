# -*- coding: utf-8 -*-

import threading

treads = []

for i in range(1, getmaxrate(pid) // 20 + 2):
    treads.append(threading.Thread(target=函数, args=(pid, i)))
for t in treads:
    t.start()
for t in treads:
    t.join()
