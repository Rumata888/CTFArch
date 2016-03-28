#!/usr/bin/python
from time import sleep
import sys
import socket
def ConvertMaze(mazestring):
    mazestrings=mazestring.split('\n')
    for z in mazestrings:
        print z
    current_level=-1
    i=0
    maze_levels=[]
    for maze_level in mazestrings:
        wall_str=False
        place_str=False
        walls=[]
        if len(maze_level)==0:
            continue
        if i%2==0:
            wall_str=True

            

            cur_str=maze_level
            if cur_str[0]=='+':
                wall_level=['W']
            else:
                wall_level=['U']
            k=0

            while len(cur_str)>1:
                cur_str=cur_str[1:]
                if cur_str[0]=='-':
                    wall_level.append('W')
                elif cur_str[0]==' ':
                    wall_level.append('E')
                else:
                    wall_level.append('U')
                wall_level.append('W')
                cur_str=cur_str[3:]
        else:
            place_str=True

            cur_str=maze_level
            if cur_str[0]=='|':
                wall_level=['W']
            elif cur_str[0]==' ':
                wall_level=['E']
            else:
                wall_level=['U']
            k=0

            cur_str=cur_str[1:]
            if cur_str[:3].find('*')!=-1:
                wall_level.append('*')
            elif cur_str[:3].find('#')!=-1:
                wall_level.append('U')
            else:
                wall_level.append('E')
            cur_str=cur_str[3:]
            while len(cur_str)>1:
                if cur_str[0]=='|':
                    wall_level.append('W')
                elif cur_str[0]==' ':
                    wall_level.append('E')
                else:
                    wall_level.append('U')
                if cur_str[:3].find('*')!=-1:
                    wall_level.append('*')
                elif cur_str[:3].find('#')!=-1:
                    wall_level.append('U')
                else:
                    wall_level.append('E')
                

                cur_str=cur_str[4:]
                
            if cur_str[0]=='|':
                wall_level.append('W')
            elif cur_str[0]==' ':
                wall_level.append('E')
            else:
                wall_level.append('U')
        i+=1       
        maze_levels.append(wall_level)

    return maze_levels





def FindMe(maze_levels):
    i=1
    while i<len(maze_levels):
        j=1
        while j<len(maze_levels[i]):
            if maze_levels[i][j]=='*':
                return (i,j)
            j+=2
        i+=2

def MakeDecision(maze_levels):
    places_left=[]
    current_possible=[]
    (y,x)=FindMe(maze_levels)
    current_possible.append((x,y,''))
    while True:
        c_p=[]
        
        x,y,base_h=current_possible[0]
        if maze_levels[y][x-1] in ['E','U']:
            c_p.append((x-2,y,base_h+'l'))
        if maze_levels[y][x+1] in ['E','U']:
            c_p.append((x+2,y,base_h+'r'))
        if maze_levels[y-1][x] in ['E','U']:
            c_p.append((x,y-2,base_h+'u'))
        if maze_levels[y+1][x] in ['E','U']:
            c_p.append((x,y+2,base_h+'d'))
        c_p_checked=[]
       
        for (x1,y1,h1) in c_p:
            
            if (x1,y1) not in places_left:
                c_p_checked.append((x1,y1,h1))
            if (x1>=len(maze_levels[0]))or(x1<0)or(y1<0)or(y1>=len(maze_levels)):
                return h1
      
 
            if maze_levels[y1][x1]=='U':
                return h1



        places_left.append((x,y))
        current_possible=c_p_checked+current_possible[1:]
                       

def netcat(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((hostname, port))
    data=''
    while 1:
        try:
            data = s.recv(8192)
        except:
            print '\n'
        if data.find('Round')!=-1:
            break
    print 'Starting'
    
    data_saved=''
    file
    while 1:
        try:
            data = s.recv(8192)
            print data
        except:
            print '\n'
        with open("result.txt", "a+") as myfile:
                myfile.write(data)
        if (data.find('|')!=-1)and(data_saved==''):
            
           
            data_saved=data
        else:
            data_saved=data_saved+data
        if len(data_saved)>=(150*40):
            print data_saved
            while data_saved[-1]=='\n':
                data_saved=data_saved[:-1]
            if data_saved.find('Round')!=-1:
                indexor=data_saved.find('Round')
                data_saved=data_saved[indexor:]
                indexor=data_saved.find('\n')
                data_saved=data_saved[indexor+1:]
            print data_saved
            s.sendall(MakeDecision(ConvertMaze(data_saved))+'\n')
            data_saved=''
       
        data=""
    print "Received:", repr(data)
    print "Connection closed."
    s.close()


        
if __name__=="__main__":
        netcat(sys.argv[1],int(sys.argv[2]))
