import random

def is_prime(a):
    d = 2
    while d*d <= a and a%d != 0:
        d+=1
    return d*d > a

def alg1(s, k):
    ans = 0
    for i in range(0, 499):
        if s[i]==k[0] and s[i+1]==k[1]:
            ans = ans + 1
    return ans

def hash(k):
    index = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 10
    m = 1
    a = index[int(k[0])-1]*x + index[int(k[1])-1]*1
    return a

def rabin_karp(s, k):
    ans = 0
    hash_key = hash(k)
    for i in range(0, 499):
        new_s = s[i]+s[i+1]
        hash_s = hash(new_s)
        if hash_s == hash_key:
            for j in (0,1):
                if new_s[j]!=k[j]:
                    break
                ans = ans + 1
    return ans
    

def boyar_mur(s, k):



s = ""
flag = 0
while flag<500:
    for x in range(1, 100):
        t = random.randint(2, 10000)
        k1 = 3*t - 1
        k2 = 3*t + 1
        l1 = 4*t - 1
        l2 = 4*t + 1
        if is_prime(t):
            l = str(t)
            s = s + l
            flag = flag + 1
        if is_prime(k1):
            k1 = str(k1)
            s = s + k1
            flag = flag + 1
        if is_prime(k2):
            k2 = str(k2)
            s = s + k2
            flag = flag + 1
        if is_prime(l1):
            l1 = str(l1)
            s = s + l1
            flag = flag + 1
        if is_prime(l2):
            l2 = str(l2)
            s = s + l2
            flag = flag + 1
print(s)
array = list(set([(s[i], s[i+1]) for i in range(len(s) - 1)]))
answer = []
iter = []

for i in array:
    if i[0] != '0':
        #print("meow " + i[0])
        key = i[0]+i[1]
        #j = alg1(s, key)
        #j = rabin_karp(s, key)
        iter.append(((key, j)))
        answer.append(j)
max = 0
for i in range(len(answer)):
    answer[i] > max
    max = answer[i]

print(max)
for i in iter:
    if i[1] == max:
        print (i[0])
print(array)