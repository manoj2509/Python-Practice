__author__ = 'Mj'

Regex_Pattern = r'(HackerRank)\b'

import re
count = 0
n = int(input().strip())
for i in range(n):
    Test_String = input()
    match = re.search(Regex_Pattern, Test_String, re.I)
    if match:

        count += 1
print(count)