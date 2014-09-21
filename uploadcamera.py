import os
import stat
import string
import sys
import time

#cameraDir = 'H:\\'
cameraDir = 'k:\\'
#destDir = 'C:\\Documents and Settings\\Kevin\\My Documents\\My Pictures\\photos'
destDir = 'P:\\media\\photos\\photos2011'

def copyFile(ffn, destDir):
    fn = os.path.split(ffn)[1]
    dt = time.localtime(os.stat(ffn)[stat.ST_MTIME])
    if not os.path.isdir(os.path.join(destDir, '%04d_%02d_%02d' % dt[:3])):
        os.mkdir('%s' % os.path.join(destDir, '%04d_%02d_%02d' % dt[:3]))
        print "mkdir('%s')" % os.path.join(destDir, '%04d_%02d_%02d' % dt[:3])
    destFile = os.path.join(destDir, '%04d_%02d_%02d' % dt[:3])
    if os.path.exists(os.path.join(destFile, fn)):
        #print "destFile='%s'" % os.path.join(destFile, fn)
        print "Copy of file: '%s' skipped; destination exists." % ffn
    else:
        print "os.system( \"COPY /V \"%s\" \"%s\"\"" % (ffn, destFile), ")"
        os.system( "COPY /V \"%s\" \"%s\"" % (ffn, destFile) )
    #os.unlink(ffn)

def main(cameraDir, destDir):
    for root, dirs, files in os.walk(cameraDir):
        for name in files:
            ext = string.lower( os.path.splitext(name)[1] )
            if ext in ['.tif', '.gif', '.jpg', '.avi', '.mpg', '.mov']:
                copyFile( os.path.join(root, name), destDir )
            else:
                print "Skipping file:", os.path.join(root, name)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        cameraDir = sys.argv[1]
        if len(sys.argv) > 2:
            destDir = sys.argv[2]
    main( cameraDir, destDir )
