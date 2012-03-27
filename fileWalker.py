import os, sys
import UltraFastDuplicateFilesFinder as ff

testPath = os.path.join( os.path.curdir )







def getDirName(dirName=None):
    if dirName:
        if os.path.isdir( os.path.normpath( dirName )):
            return dirName
    if sys.argv[1:]:
        out = sys.argv[1]
        if os.path.isdir( os.path.normpath( out )):
            return out
    
    while 1:
        inp = input("which folder would you like to find the duplicates in?\n")
        if not inp: # mainly for debugging
            global testPath
            inp = testPath
            break
        if os.path.isdir( os.path.normpath( inp )):
            break
    return inp
    

def main(dirName=None):
    root = getDirName(dirName)
    walker = os.walk(root)

    for j in walker:
        print(j)

if __name__ == '__main__':
    main()
