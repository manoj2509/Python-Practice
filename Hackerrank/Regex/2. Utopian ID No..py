__author__ = 'Mj'

Regex_Pattern = r'^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}$'

import re
n = int(input().strip())
for i in range(n):
    Test_String = input()
    match = re.search(Regex_Pattern, Test_String)
    if match:
        print("VALID")
    else:
        print("INVALID")