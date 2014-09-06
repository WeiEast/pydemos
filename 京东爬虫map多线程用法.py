#! python3
import requests


pid = '967821'


def maxpagenum(pid):
    headers1 = {'GET': '',
                'Host': "club.jd.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': 'http://item.jd.com/{}.html'.format(pid)}

    r1 = requests.get(
        'http://club.jd.com/productpage/p-{}-s-0-t-3-p-{}.html'.format(pid, 0), headers=headers1)
    # 先获取最大页码数
    ss = r1.json()['productCommentSummary']['commentCount'] // 10
    return ss

# print(maxpagenum)


def getrate_jd(pp):
    pid = pp[0]
    pagenum = pp[1]
    '''该函数用来获取商品ID是pid的第pagenum页的评论列表'''
    headers1 = {'GET': '',
                'Host': "club.jd.com",
                'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
                'Referer': 'http://item.jd.com/{}.html'.format(pid)}
    r = requests.get(
        'http://club.jd.com/productpage/p-{}-s-0-t-3-p-{}.html'.format(pid, pagenum), headers=headers1)
    aa = r.json()
    ss = [x['content'] for x in aa['comments']]
    global ll
    if ss != []:
        return ss


def crawl(pid):
    from multiprocessing.dummy import Pool
    urls = []

    pool = Pool(15)
    for i in range(maxpagenum(pid) + 1):
        urls.append((pid, i))
    results = pool.map(getrate_jd, urls)
    pool.close()
    pool.join()
    return results

from time import clock as now
start = now()
print(crawl(pid))
end = now()
print('本次爬虫总耗时：', int(end - start), 's')
