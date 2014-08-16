

from multiprocessing.dummy import Pool

pool = Pool(4)
urls = ['']  # 其实这里可以放多个元组作为参数传入函数
pool.map(getrate_jd, urls)
pool.close()
pool.join()
print(ll)
