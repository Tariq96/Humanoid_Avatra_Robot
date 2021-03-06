import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import time 
import matplotlib.animation as animation

import math 
from threading import Thread
#-------custom---------------
from angleEngine import vector ,angle


_CONNECTION = [
        [0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [0, 7], [7, 8],
        [8, 9], [9, 10], [8, 11], [11, 12], [12, 13], [8, 14], [14, 15],
        [15, 16]]
join_name={0:"crotch",1:"l_hip",2:"l_knee",3:"left_feet",
           4:"r_hip",5:"r_knee",6:"r_feet",7:"chest",
           8:"lower_neck",9:"upper_neck",10:"head",11:"r_shoulder",
           12:"r_elbow",13:"r_hand",14:"l_shoulder",15:"l_elbow",
           16:"left_hand"}
join_num={"crotch":0     ,"l_hip":1      ,"l_knee":2      ,"left_feet":3,
          "r_hip":4      ,"r_knee":5     ,"r_feet":6      ,"chest":7,
          "lower_neck":8 ,"upper_neck":9 ,"head":10       ,"r_shoulder":11,
          "r_elbow":12   ,"r_hand":13    ,"l_shoulder":14 ,"l_elbow":15,
          "left_hand":16}
angles=[join_num["l_hip"],join_num["l_knee"],
        join_num["r_hip"],join_num["r_knee"],
        join_num["l_shoulder"],join_num["l_elbow"],
        join_num["r_shoulder"],join_num["r_elbow"]]


pose_3d=[
      [  12.82940148, -100.30240881,  -76.33411549 , -47.88706816 , 110.3646784,
     48.91913072 ,  59.16321995 ,  34.49412725 ,   4.28411421 , -46.74678603,
     -6.64194842 , 145.38996323 , 182.89336095 , 192.82483483 , -98.40667486,
   -161.45959738 ,-252.80748916],
   [  15.84084216 , 110.35759376   ,42.04545833  , 94.35015712  ,-78.67589366
  , -141.17304027 , -78.40770241  , 38.45974914  , 14.86075975 , -52.56037457
    ,-17.41718882 , -74.59002275 ,-152.16434207 ,-229.41350331 , 122.70442207,
    227.80423991 , 157.79090981],
  [ -61.98052206  ,-49.34881459 ,-463.7183776  ,-879.84092204  ,-23.44218217
   ,-462.13092401 ,-879.08603031 , 196.70130871 , 490.59708566 , 549.9238213
    ,700.9287918  , 466.23076523 , 206.04579191  , -2.33349679 , 465.88806215
    ,203.59293852  ,-41.8707693 ]]
pose_3d=np.array(pose_3d)


class joint ():
    def __init__ (self,j,posee):
        self.j=j
        self.joint=[
                    [posee[0, angles[j]], posee[1, angles[j]],posee[2, angles[j]]],
                    [posee[0, angles[j]+1], posee[1, angles[j]+1],posee[2, angles[j]+1]],
                    [posee[0, angles[j]-1], posee[2, angles[j]-1],posee[2, angles[j]-1]]
                    ]
        self.orgin=(self.joint[0])
        self.p1=(self.joint[1])
        self.p2=(self.joint[2])
        self.vector1=vector(p1=self.orgin,p2=self.p1)
        self.vector2=vector(self.orgin,self.p2)
        self.joint_angle=angle().get_angle(self.vector1,self.vector2)


    def update(self,posee):
        """
        Usage
        Debug
        knee=joint(1,pose)
        print(knee.joint_angle)

        changing the angle of the join in question 

        pose[0][2]=15 
        pose[1][2]=15
        pose[2][2]=15

        knee.update(pose)
        print(knee.joint_angle)

        """


        self.joint=[
                    [posee[0, angles[self.j]], posee[1, angles[self.j]],posee[2, angles[self.j]]],
                    [posee[0, angles[self.j]+1], posee[1, angles[self.j]+1],posee[2, angles[self.j]+1]],
                    [posee[0, angles[self.j]-1], posee[2, angles[self.j]-1],posee[2, angles[self.j]-1]]
                    ]
        self.orgin=(self.joint[0])
        self.p1=(self.joint[1])
        self.p2=(self.joint[2])
        self.vector1.update(self.orgin,self.p1)
        self.vector2.update(self.orgin,self.p2)
        self.joint_angle=angle().get_angle(self.vector1,self.vector2)
"""
knee=joint(1,pose)
print(knee.joint_angle) 
knee.update(pose)       
"""
# used in definig graph size
"""
smallest = k.min()
largest = k.max()
"""
#defining the graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


"""
Debuging
linex=0

def data():
    global linex 
    while True:
        x=input()
        if x== "c":
            linex +=1
            if linex==16:
                linex=0

data_thread=Thread(target=data)
data_thread.start()
"""
def body_plotting(pose):
    smallest = pose.min()
    largest = pose.max()
    #print(pose)
    
    
    
    



    ax.clear()
    for c in _CONNECTION:
            
            
            ax.plot([pose[0, c[0]], pose[0, c[1]]],
                    [pose[1, c[0]], pose[1, c[1]]],
                    [pose[2, c[0]], pose[2, c[1]]], color='black')
    
            print(pose[0, c[0]])
            """
            Debuging
            ax.plot(
            
            [pose[0, _CONNECTION[linex][0]] , pose[0, _CONNECTION[linex]][1]],
            [pose[1, _CONNECTION[linex][0]] , pose[1, _CONNECTION[linex]][1]],
            [pose[2, _CONNECTION[linex][0]] , pose[2, _CONNECTION[linex]][1]])
            """

    for i in range(16):
        ax.scatter(pose[0][i], pose[1][i],pose[2][i], color='black')
    #-debuging-ax.text(pose[0][linex], pose[1][linex],pose[2][linex], "piont",fontsize=4,color='red')
    """
    ax.plot([pose[0, join_num["r_shoulder"]]-300,pose[0,join_num["r_shoulder"]]],[pose[1,join_num["r_shoulder"]]-300,pose[1,join_num["r_shoulder"]]],[pose[2,11],pose[2,join_num["r_shoulder"]]],color='darkblue')
    ax.plot([pose[0,join_num["r_elbow"]],pose[0,join_num["r_shoulder"]]],[pose[1,join_num["r_elbow"]],pose[1,join_num["r_shoulder"]]],[pose[2,join_num["r_elbow"]],pose[2,join_num["r_shoulder"]]],color='darkblue')
    ax.scatter(pose[0,join_num["r_shoulder"]]-300, pose[1,join_num["r_shoulder"]]-300,pose[2,join_num["r_shoulder"]],color='darkblue')
    """
    
    
    ax.plot([pose[0,join_num["r_hip"]],pose[0,join_num["r_hip"]]],[pose[1,join_num["r_hip"]],pose[1,join_num["r_hip"]]],[pose[2,join_num["r_hip"]],pose[2,join_num["r_hip"]]-300],color='red')
    ax.plot([pose[0,join_num["r_hip"]]+250,pose[0,join_num["r_hip"]]],[pose[1,join_num["r_hip"]]-250,pose[1,join_num["r_hip"]]],[pose[2,join_num["r_hip"]],pose[2,join_num["r_hip"]]],color='green')
    ax.plot([pose[0,join_num["r_hip"]]-250,pose[0,join_num["r_hip"]]],[pose[1,join_num["r_hip"]]-250,pose[1,join_num["r_hip"]]],[pose[2,join_num["r_hip"]],pose[2,join_num["r_hip"]]],color='blue')
    ax.scatter(pose[0,join_num["r_hip"]], pose[1,join_num["r_hip"]],pose[2,join_num["r_hip"]],color='Peru')
    ax.plot([pose[0,join_num["r_hip"]],pose[0,join_num["r_knee"]]],[pose[1,join_num["r_hip"]],pose[1,join_num["r_knee"]]],[pose[2,join_num["r_hip"]],pose[2,join_num["r_knee"]]],color='yellow')
    #ax.plot([pose[0,join_num["l_shoulder"]],pose[0,join_num["lower_neck"]]],[pose[1,join_num["l_shoulder"]],pose[1,join_num["lower_neck"]]],[pose[2,join_num["l_shoulder"]],pose[2,join_num["lower_neck"]]],color='yellow')

    
    
    """
    #normal joints
    #ax.scatter(pose[0,join_num["r_feet"]], pose[1,join_num["r_feet"]],pose[2,join_num["r_feet"]],color='green')
    ax.scatter(pose[0,join_num["r_elbow"]], pose[1,join_num["r_elbow"]],pose[2,join_num["r_elbow"]],color='yellow')
    ax.plot([pose[0, join_num["r_hand"]],pose[0,join_num["r_elbow"]]],[pose[1,join_num["r_hand"]],pose[1,join_num["r_elbow"]]],[pose[2,join_num["r_hand"]],pose[2,join_num["r_elbow"]]],color='red')
    ax.plot([pose[0, join_num["r_shoulder"]],pose[0,join_num["r_elbow"]]],[pose[1,join_num["r_shoulder"]],pose[1,join_num["r_elbow"]]],[pose[2,join_num["r_shoulder"]],pose[2,join_num["r_elbow"]]],color='blue')
    """
    ax.set_xlim3d(smallest, largest)
    ax.set_ylim3d(smallest, largest)
    ax.set_zlim3d(smallest, largest)
    
    
    



print("the piony is "+ str( pose_3d[0,15]))

#ch_thread=Thread(target=changing)
#ch_thread.start()
print("thread started")
#ai=animation.FuncAnimation(fig, body_plotting,fargs=(pose_3d,), interval=1000)
body_plotting(pose_3d)
plt.show()
    
    
