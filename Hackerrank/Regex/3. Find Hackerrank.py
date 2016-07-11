__author__ = 'Mj'

Regex_Pattern = r'^(hackerrank)'
Regex_Pattern2 = r'(hackerrank)$'

import re

n = int(input().strip())
for i in range(n):
    Test_String = input()
    match = re.search(Regex_Pattern, Test_String)
    match2 = re.search(Regex_Pattern2, Test_String)
    if match and match2:
        print(0)
    elif match:
        print(1)
    elif match2:
        print(2)
    else:
        print(-1)