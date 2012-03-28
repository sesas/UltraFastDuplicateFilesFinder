import os, sys
import UltraFastDuplicateFilesFinder as ff

testPath = os.path.join( os.path.curdir )



def walkerAdapter(walker, hiddenFolders=False):
    for curDir, dirList, fileList in walker:
        for filename in fileList:
            filepath = os.path.join( curDir, filename )
            if not hiddenFolders and folderIsHidden(filepath):
                continue
            yield filepath

def folderIsHidden(filepath):
    par = filepath
    while 1:
        par, cd = os.path.split(par)
        if cd.startswith('.') and not cd == '.':
            return True
        if not par:
            break

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


def delete_duplicates(hashlist):
    
    pass

def main(dirName=None):
    root = getDirName(dirName)
    walker = os.walk(root)
    walker = walkerAdapter(walker)
    hashlist = ff.main(walker)
    inp = input('would you like to remove all duplicates?\n')
    if inp.strip() in ['yes', 'y', 'ya']:
        delete_duplicates(hashlist)
##    for j in hashlist.items():
##        if len(j[1]) >1:
##            print(j)

if __name__ == '__main__':
    main()
