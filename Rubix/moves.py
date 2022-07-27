
import Rcube
import numpy as np

# What relationship does each of the moves have on the faces


def rotateFace(cube,faceColor):
   pass 



def rotateFace(cube,face):
    face = cube.faceList[face]
    mat = face.faceNum
    # Always gonna be a 3*3 matrix
    N = 3
    
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = mat[i][j]
            mat[i][j] = mat[N-1-j][i]
            mat[i][j] = mat[N - 1 - j][i]
            mat[N - 1 - j][i] = mat[N - 1 - i][N - 1 - j]
            mat[N - 1 - i][N - 1 - j] = mat[j][N - 1 - i]
            mat[j][N - 1 - i] = temp

    #mat is the easy part, now need to account for other portions of the rotation
    print("Color",face.color)
    
    adjIdx = returnAdjIdx(face.color)
    print(adjIdx)
    
    print("Above Face: ",cube.faceList[adjIdx[0]].faceNum[2,:])
    
    aboveFace = cube.faceList[adjIdx[0]].faceNum
    print("aboveFace",aboveFace)
    rightFace = cube.faceList[adjIdx[1]].faceNum
    print("rightFace",rightFace)
    belowFace = cube.faceList[adjIdx[2]].faceNum
    print("belowFace",belowFace)
    leftFace = cube.faceList[adjIdx[3]].faceNum
    print("leftFace",leftFace)
    # Save the value about to be erased
    
    aboveRotate = aboveFace[2,:]
    
    print("aboveRotate",aboveRotate)
    print(rightFace[:,0])
    rightRotate = rightFace[:,0]
    print("address of rightRotate:", id(rightRotate))
    rightFace[:,0] = aboveRotate
    print("rightFace[:,0]:", id(rightFace[:,0]))
    
    belowRotate = belowFace[0,:].reshape(1,-1)
    print(rightRotate)
    belowFace[0,:] = rightRotate
    
    leftRotate = leftFace[:,2].reshape(1,-1)
    leftFace[:,2] = belowRotate
    
    aboveFace[2,:] = leftRotate
    
    
    
    
    #cube.faceList[adjIdx[0]].faceNum[:,0].reshape(-1,1)
    #print(test)
    
    
    # at this point in need to rotate all of the surrounding pieces by 90
    # degrees, how do I know the orientation of the cube at this point?

# Returns index's of the surrounding faces to a face in clockwise orientation, starting on top
def returnAdjIdx(face):
    face = 'W'
    
    # Might find better way than hardcoding but will also never change
    adjDict = {
        'O': [5,4,3,2],
        'Y':[0,3,5,4],
        'W':[0,3,5,1],
        'G':[0,3,5,2],
        'B':['','R','W','O'],
        'R':[2,3,0,1]
    }

            
    return adjDict[face]


