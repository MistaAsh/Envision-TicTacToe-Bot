import itertools
import random
def check_winner(p):
 t=0
 if((p[0][0]==1 and p[1][1]==1 and p[2][2]==1) or (p[2][0]==1 and p[1][1]==1 and p[0][2]==1)):
  t=1
 elif((p[0][0]==1 and p[1][0]==1 and p[2][0]==1) or (p[0][1]==1 and p[1][1]==1 and p[2][1]==1) or (p[0][2]==1 and p[1][2]==1 and p[2][2]==1)):
  t=1
 elif((p[0][0]==1 and p[0][1]==1 and p[0][2]==1) or (p[1][0]==1 and p[1][1]==1 and p[1][2]==1) or (p[2][0]==1 and p[2][1]==1 and p[2][2]==1)):
  t=1
 elif((p[0][0]==0 and p[1][1]==0 and p[2][2]==0) or (p[2][0]==0 and p[1][1]==0 and p[0][2]==0)):
  t=-1
 elif((p[0][0]==0 and p[1][0]==0 and p[2][0]==0) or (p[0][1]==0 and p[1][1]==0 and p[2][1]==0) or (p[0][2]==0 and p[1][2]==0 and p[2][2]==0)):
  t=-1
 elif((p[0][0]==0 and p[0][1]==0 and p[0][2]==0) or (p[1][0]==0 and p[1][1]==0 and p[1][2]==0) or (p[2][0]==0 and p[2][1]==0 and p[2][2]==0)):
  t=-1
 if(t==1):
  print("Congratulations!You Won!")
 if(t==-1):
  print("Sorry!Computer Won!")
 if(t!=0):
  return 0
 else:
  return 1
def cur_win_rate_calculate(p):
 d=[sum(p[0]),sum(p[1]),sum(p[2])]
 e=[p[0][0]+p[1][0]+p[2][0],p[0][1]+p[1][1]+p[2][1],p[0][2]+p[1][2]+p[2][2]]
 f=[p[0][0]+p[1][1]+p[2][2],p[2][0]+p[1][1]+p[0][2]]
 if((0 in d) or (0 in e) or (0 in f)):
  return 1
 else:
  return 0
def cur_defeat_rate_calculate(p):
 d=[sum(p[0]),sum(p[1]),sum(p[2])]
 e=[p[0][0]+p[1][0]+p[2][0],p[0][1]+p[1][1]+p[2][1],p[0][2]+p[1][2]+p[2][2]]
 f=[p[0][0]+p[1][1]+p[2][2],p[2][0]+p[1][1]+p[0][2]]
 if((7 in d) or (7 in e) or (7 in f)):
  return 1
 else:
  return 0
def win_rate_calculator101(p):#p is 3x3 matrix,user plays first
 d=[sum(p[0]),sum(p[1]),sum(p[2])]
 e=[p[0][0]+p[1][0]+p[2][0],p[0][1]+p[1][1]+p[2][1],p[0][2]+p[1][2]+p[2][2]]
 f=[p[0][0]+p[1][1]+p[2][2],p[2][0]+p[1][1]+p[0][2]]
 if((3 in d) or (3 in e) or (3 in f)):
  return -1
 elif((0 in d) or (0 in e) or (0 in f)):
  return 1
 else:
  return 0
def equivalent_board(b,p):#b is board list ,p is a list in p2
 l=1
 for i in range(3):
  if(l==0):
   break
  for j in range(3):
   if(b[i][j]==5):
    continue
   else:
    if(b[i][j]!=p[i][j]):
     l=0
     break
 return l
def board_turn_calculator101(b1,p,q):#q is p2,p is [i,j],b is board list
 b=b1+[]
 b[p[0]][p[1]]=0
 sum1=cur_win_rate_calculate(b)*10000-cur_defeat_rate_calculate(b)*1000
 for e in q:
  if(equivalent_board(b,e)==1):
   #print(p)
   #conv_to_board(e)
   #print(win_rate_calculator101(e))
   #print(" ")
   sum1+=win_rate_calculator101(e)
  else:
   continue
 return sum1
def conv_to_board(q1):#converts 3x3 matrix to a board
 p=[['','',''],['','',''],['','','']]
 for h in range(3):
  for j in range(3):
   if(int(q1[h][j])==1):
    p[h][j]='X'
   if(int(q1[h][j])==0):
    p[h][j]='O'
   if(int(q1[h][j])==5):
    p[h][j]=' '
 q=[[p[0][0],'**',p[0][1],'**',p[0][2]],['*******'],[p[1][0],'**',p[1][1],'**',p[1][2]],['*******'],[p[2][0],'**',p[2][1],'**',p[2][2]]]
 for i in range(5):
  print(*q[i],sep='')
#
#
#
print("-------------------------------------------------------------Tic-Tac-Toe----------------------------------------------------------------")
y=int(input("Will you start first?(1-yes/0-no)"))
if(y==1):
 #X-1,O-0,null-2
 m=1
 p1=itertools.permutations([0,0,0,0,1,1,1,1,1])
 p1=list(set(p1))
 p1=[list(x) for x in p1]
 p2=[]
 for y1 in range(len(p1)):
  q11=[[],[],[]]
  for i in range(9):
   if(i<3):
    q11[0].append(p1[y1][i])
   elif(i<6):
    q11[1].append(p1[y1][i])
   elif(i<9):
    q11[2].append(p1[y1][i])
  i=0
  p2.append(q11)
 #conv_to_board(p2[0])
 board=[[5,5,5],[5,5,5],[5,5,5]]
 m1=input("Player is 'X' and Computer is 'O',press Enter")
 turn1=1
 while(turn1<=5):
  print("Enter the row and column to put your X")
  e,d=map(int,input().split())
  if(board[e][d]==5):
   board[e][d]=1
   turn1+=1
  else:
   print("Invalid move!")
   continue
  print("board after your turn")
  conv_to_board(board)
  print("Computer playing its turn.........")
  i=0
  w=[]
  win1=[]
  for i in range(3):
   for j in range(3):
    #print(board)
    if(board[i][j]!=5):
     continue
    else:
     f11=[i,j]
     w.append(f11)
     w1=board[0]+[]
     w2=board[1]+[]
     w3=board[2]+[]
     w4=[w1,w2,w3]
     win1.append(board_turn_calculator101(w4,f11,p2))
  if(len(win1)!=0):
   d=win1.index(max(win1)) 
   #print(win1)
   f12=w[d]+[]
   board[w[d][0]][w[d][1]]=0
   print("board after computer's turn")
   conv_to_board(board)
  else:
   print("board after computer's turn")
   conv_to_board(board)
   print("Tie!")
  if(check_winner(board)==0):
   break 
elif(y==0):
 m=1 
 p1=itertools.permutations([0,0,0,0,0,1,1,1,1])
 p1=list(set(p1))
 p1=[list(x) for x in p1]
 p2=[]
 for y1 in range(len(p1)):
  q11=[[],[],[]]
  for i in range(9):
   if(i<3):
    q11[0].append(p1[y1][i])
   elif(i<6):
    q11[1].append(p1[y1][i])
   elif(i<9):
    q11[2].append(p1[y1][i])
  i=0
  p2.append(q11)
 #conv_to_board(p2[0])
 t110=[[[0,5,5],[5,5,5],[5,5,5]],[[5,5,0],[5,5,5],[5,5,5]],[[5,5,5],[5,0,5],[5,5,5]],[[5,5,5],[5,5,5],[5,5,0]],[[5,5,5],[5,5,5],[0,5,5]]]
 r110=random.randint(0,4)
 board=t110[r110]
 m1=input("Player is 'X' and Computer is 'O',press Enter")
 print("Computer playing its turn.........")
 print("board after computer's turn")
 conv_to_board(board)
 turn1=1
 while(turn1<=4):
  print("Enter the row and column to put your X")
  e,d=map(int,input().split())
  if(board[e][d]==5):
   board[e][d]=1
   turn1+=1
  else:
   print("Invalid move!")
   continue
  print("board after your turn")
  conv_to_board(board)
  print("Computer playing its turn.........")
  i=0
  w=[]
  win1=[]
  for i in range(3):
   for j in range(3):
    #print(board)
    if(board[i][j]!=5):
     continue
    else:
     f11=[i,j]
     w.append(f11)
     w1=board[0]+[]
     w2=board[1]+[]
     w3=board[2]+[]
     w4=[w1,w2,w3]
     win1.append(board_turn_calculator101(w4,f11,p2))
  if(len(win1)!=0):
   d=win1.index(max(win1)) 
   #print(win1)
   f12=w[d]+[]
   board[w[d][0]][w[d][1]]=0
   print("board after computer's turn")
   conv_to_board(board)
  else:
   print("board after computer's turn")
   conv_to_board(board)
   print("Tie")
  if(check_winner(board)==0):
   m=0
   break 
 if(turn1==5 and m==1):
  print("Tie!")