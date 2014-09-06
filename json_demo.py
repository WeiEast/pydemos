#! python3
import json
aa = {'aa': 'bb'}
with open('xx.json', 'w') as f:
    json.dump(aa, f)

with open('ratetmall_single.json') as f:
        aa = json.load(f)
        print(aa)
