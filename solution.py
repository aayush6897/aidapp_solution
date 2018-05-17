import numpy as np
with open('input.txt') as file:
	list_m=map(int,file.read().split("\n"))

N=int(list_m[0])

min_health=0
max_injury=1000000

temp_health=2000
temp_injury=1

max_number_sofar=0

i=1
j=1
li=[]
for j in range(1,N):
	tempx=temp_health-list_m[j]
	tempy=temp_injury*list_m[j]
	if (tempx<1) or (tempy>max_injury):
		li.append(j-i)
		max_number_sofar=max(j-i,max_number_sofar)			
		temp_injury/=list_m[i]
		temp_health-=list_m[i]
		j-=1
		i+=1
	else:
		temp_health=tempx
		temp_injury=tempy	
print(max_number_sofar)
print(min(li))
li=np.asarray(li)
d = np.unique(li, return_counts=True)
print(d)