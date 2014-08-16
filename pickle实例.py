import pickle

numlist = {13250252420: 871205, 18200704872: 871205, 15521176784:
           871205, 13428525085: 871205, 13760823168: 4431939}

with open('a.data', 'wb') as f:
    pickle.dump(numlist, f)
with open('a.data', 'rb') as f:
    aa = pickle.load(f)

print(aa)
