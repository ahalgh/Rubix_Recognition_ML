
# main file 
# testing for right now

import Rcube
import moves

rubix = Rcube.cube()
rubix.printColors()
rubix.printNums()
#,rubix.faceList[1].faceNum)
print("Rotating...")
face = 2

moves.rotateFaceClockwise(rubix,face)
print("Rotating 2...")
# moves.rotateFace(rubix,face)
# print("Rotating 3...")
# moves.rotateFace(rubix,face)
# print("Rotating 4...")
# moves.rotateFace(rubix,face)

#white_face = Rcube.face('W',1,)
rubix.printColors()

rubix.printNums()
#rint(white_face.color)
#print(white_face.faceNum)
#print(white_face.faceColors)





