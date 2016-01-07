__author__ = 'Mj'
import sys
count_max = 0
team_count = 0
n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
sum = []
topic_i = 0
for topic_i in range(n):
   topic_t = str(input().strip())
   topic.append('1' + topic_t)
for i in range(n):
    for j in range(i+1, n):
        sum = str(int(topic[i]) + int(topic[j]))
        count = sum.count('1') + sum.count('2') - 1

        if(count_max == count):
            count_max = count
            team_count += 1
        elif(count_max < count):
            team_count = 1
            count_max = count
print(count_max)
print(team_count)
