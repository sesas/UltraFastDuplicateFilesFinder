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
##        print(par, ':', cd)
        if cd.startswith('.') and not cd == '.':
            return True
        if not par or os.path.ismount(par):
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
        inp = print("which folder would you like to find the duplicates in?")
##        inp = print("(make sure the path you insert has double \\ in between folders.")
        inp = input()
        if not inp: # mainly for debugging
            global testPath
            inp = testPath
            break
        if os.path.isdir( inp ):
            break
    return inp


def delete_duplicates(hashlist, interactive=True, verbose=True):
    for fl in hashlist.values():
        if len(fl) > 1:
            print('keeping:', fl[0])
        for filename in fl[1:]:
            print('duplicate:', filename)
            if interactive:
                inp = input('?').strip()
                if not inp in ['yes', 'y', 'ya']:
                    continue
            print('deleting:', filename)
            os.remove(filename)
        pass
    pass

def main(dirName=None):
    root = getDirName(dirName)
    walker = os.walk(root)
    walker = walkerAdapter(walker)
    hashlist = ff.main(walker)
    inp = input('would you like to remove all duplicates?\n').strip()
    if inp in ['int', 'yi']:
        delete_duplicates(hashlist, True)
    elif inp in ['yes', 'y', 'ya']:
        delete_duplicates(hashlist)
    else:
        print('no file was deleted')
##    for j in hashlist.items():
##        if len(j[1]) >1:
##            print(j)

if __name__ == '__main__':
    main()
