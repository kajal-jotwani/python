#  long long ago, in a galaxy far far away, the empire was getting 
# decadent and oppressive. the people were suffering and decided 
# to rrebel. under the leadership of princess leia and the resistance took form.

freq = {}
for ch in s:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1
    print(freq)

from collections import defaultdict as ddict

freq2 = ddict(int)
for ch in s:
    freq2[ch] += 1
print(freq2)

from collections import Counter
freq3 = Counter(s)
print(freq3.most_ocommon(6))