#! python3
from multiprocessing.dummy import Pool


def getrate_jd(url):
    pass
pool = Pool(4)  # 这里的数字表示线程池，如果不写，则列表多长就多少线程
urls = ['']  # 其实这里也可以放个元组为多参数传入函数
pool.map(getrate_jd, urls)
pool.close()
pool.join()
print(ll)
