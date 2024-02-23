import csv
import time
from simple_colors import *

print(blue('\nPLEASE CHOOSE LANGUAGE\n言語をお選べください\n\t1: English\n\t2: 日本語\n','bold'))
choice = int(input('Language: '))
lang = {1:['\nDISCLAIMER: This program only reads .dat file\nIf simple_colors module not downloaded: run (pip3 install simple-colors) in terminal','Name of element\'s file: ','Name of node\'s file: ','Name of temperature file to write into: ','How many nodes do you wish to set to 0°C? : ','Node number: ','How many nodes do you wish to set to 100°C? : ','Read .dat Files: ','Initializing Matrices: ','Coefficient Matrix Calculation: ','Setting Boundary Conditions: ','Computation of T[]: ','               CALCULATION TIME','Name of .vtk file to write into: ','This program automatically creates a vtk mesh file\n'],2:['\n注意：このプログラムは.datファイルしか読み取らない\nsimple_colorsのモジュールが入っていなければ、ターミナルで(pip3 install simple-colors)を実行してください','要素ファイル名：','節点ファイル名：','書き込む温度ファイル名：','0°Cにする節点の数：','節点の番号：','100°Cにする節点の数：','.datファイルの読み込み：','行列の初期化：','全体要素係数行列の計算：','初期条件の設定：','温度行列T[]の計算：','　　　　　　　計算時間','書き込む.vtkファイル名: ','このプログラムは自動的にメッシュのvtkファイルを作成する\n']}
print(red(lang[choice][0],'bold'))
print(blue(lang[choice][14],'bright'))

#Initializing lists
cells = []                     #cells = 要素
nodes = []                     #nodes = 点
x = [0,0,0]
y = [0,0,0]
a = [0,0,0]
b = [0,0,0]
K = []
T = []
R = []
temp = []
el = input(lang[choice][1])
nd = input(lang[choice][2])
tem = input(lang[choice][3])
vtk = input(lang[choice][13])
ls0 = []
ls100 = []
zero = int(input(lang[choice][4]))
while zero>0:
    ls0.append(int(input(lang[choice][5])))
    zero -= 1
hun  = int(input(lang[choice][6]))
while hun>0:
    ls100.append(int(input(lang[choice][5])))
    hun -= 1

#Read .dat files
start = time.time()
with open(el,'r') as f:                                      #element.dat
    counter = 0
    freader = csv.reader(f, delimiter=' ')
    for line in freader:
        cells.append([])
        cells[counter].append(int(line[1]))
        cells[counter].append(int(line[2]))
        cells[counter].append(int(line[3]))
        counter += 1
f.close()

with open(nd,'r') as f:                                         #node.dat
    counter = 0
    freader = csv.reader(f, delimiter=' ')
    for line in freader:
        nodes.append([])
        nodes[counter].append(float(line[0]))
        nodes[counter].append(float(line[1]))
        counter += 1
f.close()
end = time.time()
print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(red(lang[choice][12],['bold','bright']))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
print(lang[choice][7] + f'{end - start} s')

#Initializing Overall_Coefficient_Matrix_(K)  |  Temperature_Matrix_(T)  |   Right_Hand_Side_Matrix_(R)  |  Temp[]
start = time.time()
n = len(nodes)															#Order of Matrix
for row in range(n):
	K.append([])
	T.append(0)
	R.append(0)
	temp.append(0)														#Both T[] and R[] have been initialized to be 0
	for column in range(n):
		K[row].append(0)
end = time.time()
print(lang[choice][8] + f'{end-start} s')
	
#Addition of Individual_Coefficient_Matrices_(k) into Overall_Coefficient_Matrix_(K)
start = time.time()    
for cell in cells:
    for i in range(3):
        x[i] = nodes[cell[i]][0]
        y[i] = nodes[cell[i]][1]
        
    s = (x[0]*(y[1]-y[2]) + x[1]*(y[2]-y[0]) + x[2]*(y[0]-y[1]))/2		# s = area of triangle
    
    a[0] = y[1]-y[2]
    a[1] = y[2]-y[0]
    a[2] = y[0]-y[1]
    b[0] = x[2]-x[1]
    b[1] = x[0]-x[2]
    b[2] = x[1]-x[0]
    
    for i in range(3):													#Individual_Coefficient_Matrix calculation
    	for j in range(3):
    		K[cell[i]][cell[j]] += (a[i]*a[j]+b[i]*b[j])/(4*s)
end = time.time()
print(lang[choice][9] + f'{end-start} s')
    
#Tempering with K and R to Set Boundary Conditions  |  Node ?: 0°C  Node ?: 100°C
start = time.time()
for e in ls0:
	for i in range(n):
		K[e][i] = 0
	K[e][e] = 1
for e in ls100:
	for i in range(n):
		K[e][i] = 0
	K[e][e] = 1
	R[e] = 100
end = time.time()
print(lang[choice][10] + f'{end-start} s')

#Computation of T[] using LU DECOMPOSITION METHOD in the form of KT=R
start = time.time()
with open(tem,'w+') as f:					#Opening data file
    for i in range(n-1):
        for j in range(i+1,n):
            m = K[j][i]/K[i][i]
            for k in range(i+1,n):
                K[j][k] -= m*K[i][k]
            K[j][i] = m
			
    for j in range(n):									#Forward substitution
        sum = 0
        for k in range(j):
            sum += K[j][k]*temp[k]
        temp[j] = R[j]-sum

    for j in range(n-1,-1,-1):							#Backward substitution
        sum = 0
        for k in range(j+1,n):
            sum += K[j][k]*T[k]
        T[j] = (temp[j]-sum)/K[j][j]

    for i in range(n):									#Writing into .dat file
        f.write(f'{T[i]}\n')
f.close()
end = time.time()
print(lang[choice][11] + f'{end-start} s')
    
#creating .vtk file
with open(vtk,'w+') as f:
    f.write(f'# vtk DataFile Version 2.0\n{vtk[0:-4]}\nASCII\nDATASET UNSTRUCTURED_GRID\nPOINTS {n} float\n')
    for i in range(n):
        f.write(f'{nodes[i][0]} {nodes[i][1]} 0.0\n')
    f.write(f'CELLS {len(cells)} {len(cells)*4}\n')
    for i in range(len(cells)):
        f.write(f'3 {cells[i][0]} {cells[i][1]} {cells[i][2]}\n')
    f.write(f'CELL_TYPES {len(cells)}\n')
    for i in range(len(cells)):
        f.write('5\n')
    f.write(f'POINT_DATA {n}\nSCALARS point_scalars float\nLOOKUP_TABLE default\n')
    for i in range(n):
        f.write(f'{T[i]}\n')
f.close()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
