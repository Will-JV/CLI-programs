#GAUSS-SEIDEL METHOD with python

n = int(input('Number of variables: '))			#Order of matrix
print('\n')

A = []
x = []
b = []
for i in range(0,n):							#Taking input of matrix
	A.append([])
	for j in range(0,n):
		A[i].append(float(input(f'A{i+1}{j+1}: ')))
	b.append(float(input(f'b{i+1}: ')))

for i in range(0,n):							#Initializing variable values
	x.append(float(input(f'x{i+1}: ')))
print('\n')

truecounter = 0
repetitions = 0
e = 0.000001
with open('graph.dat','w+') as f:				#Opening data file
	while truecounter != n:
		truecounter = 0
		maxmargin = 0
		for i in range(0,n):
			before = x[i]
			x[i] = b[i]
			for j in range(0,n):
				if i!=j:
					x[i] -= A[i][j]*x[j]
			x[i] /= A[i][i]
			if before!=0:
				margin = abs(x[i]-before)/abs(before)
				if margin < e:
					truecounter += 1
				if margin > maxmargin:
					maxmargin = margin
		repetitions += 1
		f.write(f'{repetitions}\t')
		f.write(f'{maxmargin}\n')
f.close()

for i in range(0,n):
	print(f'x{i+1} = {x[i]}')
print(f'Repetitions = {repetitions}')
		

	
