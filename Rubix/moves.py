
import Rcube

# What relationship does each of the moves have on the faces


def rotateFace(cube,faceColor):
   pass 



def rotateFace(cube,face):
    
    mat = cube.faceList[face].faceNum
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

    adjList = returnAdjFaces(face)
    # at this point in need to rotate all of the surrounding pieces by 90
    # degrees, how do I know the orientation of the cube at this point?

def returnAdjFaces(face):
    face = 'W'
    
    # Might find better way than hardcoding but will also never change
    adjDict = {
        'O': ['G','Y','B','W'],
        'Y':['G','R','B','O'],
        'W':['G','R','Y','O'],
        'G':['W','R','Y','O'],
        'B':['Y','R','W','O'],
        'R':['Y','G','W','B']
    }

            
    return adjDict[face]


