
# Rcube.py 
# Purpose: will create the rubix cube object, another module will handle the
# moves, another module will handle implementing the solving algorithm. 
#
# Multiple scrambling algorithms possible, implement one first
# 
# Goal: Create Rubix cube object that can be randomly scrambled and solved using
# project best practice... once complete implement the cnn to recognize the
# cube.
# 
# How is the rotation going to work? 
# I have a face object made up of 9 cube objects
# Should it be face or should the entire cube
# ######              
#                  ### # ### #              
#                  # #   # #       
#                  ### # ### # 
#                     
# this
#                  123 9  111213 19
#                  4 5    14  15
#                  678 10 161718 20
#Becomes
#                  13191 2 3911 12 
# Probably too complex to come up with a general rule
# Would be better to switch the cube objects of each of the faces 
# There will be copies at the cost of easier rotations
# Copies of that object will already be in 
#       
#   create a look up face function
#
# How do these pieces interact with each other
#
#       With any given rotation the top row moves by 3 
#       so that 
#
#
#And those cover for everything in the cube
# For app or web, use django to learn framework. 
#
import numpy as np

class face:
    def __init__(self, color, face_num):
        self.color = color
        self.faceNum = np.zeros((3,3),dtype=int)
        count = (face_num * 9) + 1 

        for i in range(0,3):
            for j in range(0,3):
                self.faceNum[i,j] = count
                count += 1

        self.faceColors = np.full((3,3),color,dtype=str)
        

class cube:
    def __init__(self):
        self.faceList = []
        self.colorList = ['O','Y','W','G','B','R']
        for i in range(0,6):
            #print(self.colorList)
            self.faceList.append(face(self.colorList[i],i))


        #self.cubeMat = np.array((3,3,3),color,dtype=str)


    def printNums(self):
        print("Printing current number state of the cube...")
        
        for j in range(3):
            print("         ",end="")
            for k in range(3):
                    print(self.faceList[0].faceNum[j,k],end=" ")
            print()     

        for j in range(3):
            for i in range(1,5):
                for k in range(3):
                    print(self.faceList[i].faceNum[j,k],end=" ")
            print()

        for j in range(3):
            print("         ",end="")
            for k in range(3):
                    print(self.faceList[5].faceNum[j,k],end=" ")
            print()     
        

    def printColors(self):
        print("Printing current color state of the cube...")
        
        for j in range(3):
            print("      ",end="")
            for k in range(3):
                    print(self.faceList[0].faceColors[j,k],end=" ")
            print()     

        for j in range(3):
            for i in range(1,5):
                for k in range(3):
                    print(self.faceList[i].faceColors[j,k],end=" ")
            print()

        for j in range(3):
            print("      ",end="")
            for k in range(3):
                    print(self.faceList[5].faceColors[j,k],end=" ")
            print()     
        

        



