
import Rcube
import numpy as np
import copy

# What relationship does each of the moves have on the faces


def rotateFaceCounterClockwise(cube,faceColor):
   pass 



def rotateFaceClockwise(cube,face):

    face = cube.faceList[face]
    mat = face.faceNum
    
    # Rotating a 3*3 matrix counterclockwise
    for i in range(0, 2):
        temp = mat[0][i]
        mat[0][i] = mat[2-i][0]
        mat[2-i][0] = mat[2][2-i]
        mat[2][2-i] = mat[i][2]
        mat[i][2] = temp

    # mat is the easy part, now need to account for other portions of the rotation
    # print("Color",face.color)
    
    # Returns indexs necessary for counterclockwise rotation, wont be the same, just need to split off into functions 
    # Should I use different functions? 
    
    adjDict = {
        'O': rotateOside(face.color),
        'Y': rotateYside(face.color),
        'W': rotateWside(face.color),
        'G': rotateGside(face.color),
        'B': rotateBside(face.color),
        'R': rotateRside(face.color),
    }
   
    adjIdx = returnAdjIdx(face.color)
    print(adjIdx)
    
    print("Above Face: ",cube.faceList[adjIdx[0]].faceNum[2,:])
    def rotateWside(face.color):
       aboveFace = cube.faceList[adjIdx[0]].faceNum
       print("aboveFace",aboveFace)
       rightFace = cube.faceList[adjIdx[1]].faceNum
       print("rightFace",rightFace)
       belowFace = cube.faceList[adjIdx[2]].faceNum
       print("belowFace",belowFace)
       leftFace = cube.faceList[adjIdx[3]].faceNum
       print("leftFace",leftFace)
       # Save the value about to be erased
       print("######################################")

       # Copy Right side of matrix
       rightRotate = copy.copy(rightFace[:,0])

       # Overwrite Right with Above
       rightFace[:,0] = aboveFace[2,:]

       # Copy Bottom side of matrix
       belowRotate = copy.copy(belowFace[0,:].reshape(1,-1))

       # Overwrite bottom with Right
       belowFace[0,:] = np.flip(rightRotate)

       # Copy left side of matrix
       leftRotate = copy.copy(leftFace[:,2])

       # Overwrite left with bottom
       leftFace[:,2] = belowRotate

       # Overwrite top with left
       aboveFace[2,:] = np.flip(leftRotate)
    
    
    
    
    #cube.faceList[adjIdx[0]].faceNum[:,0].reshape(-1,1)
    #print(test)
    
    
    # at this point in need to rotate all of the surrounding pieces by 90
    # degrees, how do I know the orientation of the cube at this point?

# Returns index's of the surrounding faces to a face in clockwise orientation, starting on top
def returnAdjIdx(face):
    face = 'W'
    
    # Might find better way than hardcoding but will also never change
    adjDict = {
        'O': [5,3,2,1],
        'Y':[0,2,5,4],
        'W':[0,3,5,1],
        'G':[0,4,5,2],
        'B':[0,1,5,3],
        'R':[2,3,0,1]
    }

    # 6 different rotation types, how to account        
    return adjDict[face]


