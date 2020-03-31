def findLargestLength(m):
	lengths=[]
	for i in range(m[0]):
		j=i
		sum=0
		cnt=0
		while (sum<=m[1]) and (j<m[0]):
			if m[2][j]=='1':
				sum+=1
			cnt+=1
			j+=1
		lengths.append(cnt)
	print(max(lengths)-1)
	
l=[]
n=int(input())
for _ in range(n):
	l.append([int(input()),int(input()),input()])
	
for i in l:
	findLargestLength(i)
