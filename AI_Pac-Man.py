from random import randint as R
from random import *
import time
M=[]
V=[]
def dispboard():
	for i in range(10):
		print "".join(M[i])
	print "\n"*1
	time.sleep(1)
def init():
	for i in range(10):
		M.append(["."]*10)
		V.append([50]*10)
	M[0][0]="P"
	M[R(2,9)][R(2,9)]="F"
def valid(x,y):
	return 0<=x<10 and 0<=y<10
def neighbours(x,y):
	L=[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
	LL=[]
	for i in L:
		if valid(i[0],i[1]):
			LL.append(i)
	return LL
def nextmove(curx,cury):
	LL=[]
	neigh=neighbours(curx,cury)
	for i in neigh:
		LL+=[i]*V[i[0]][i[1]]
	shuffle(LL)
	return LL[0]
def iterate(N):
	stx=0
	sty=0
	Store=[(stx,sty)]
	for i in range(N):
		stx,sty=nextmove(stx,sty)
		Store.append((stx,sty) )
		if M[stx][sty]=="F":
			ind=0
			for places in Store:
				V[places[0]][places[1]]+=ind
				ind+=1
			break
def ke(l):
	return -V[l[0]][l[1]]
vis=set()
def nextbestmove(curx,cury):	
	vis.add((curx,cury))
	neigh=neighbours(curx,cury)
	neigh=sorted(neigh,key=ke)
	for i in neigh:
		if i not in vis:
			return i
	return neigh[0]
def follow():
	stx=0
	sty=0	
	dispboard()
	for i in range(1000):
		M[stx][sty]="."
		stx,sty=nextbestmove(stx,sty)
		if M[stx][sty]=="F":			
			break
		M[stx][sty]="P"
		dispboard()					
	print "Eaten"
def main():
	print 'training...'
	init()
	for i in range(63):
		iterate(100)	
	dispboard()	
	follow()
main()




