#Group Anagrams:
from collections import defaultdict
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = defaultdict(list)
for s in strs:
    sorted_str = ''.join(sorted(s))
    anagrams[sorted_str].append(s)
grouped_anagrams = list(anagrams.values())
print(grouped_anagrams)  
