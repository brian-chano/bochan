import os, re

if __name__ == '__main__':
    directory = raw_input("Enter name of directory with Naruto mp4 files for renaming: ")

    try:
        os.chdir(directory)

    except:
        print "Cannot continue. Full direcotry name required."
        exit(1)

    for vid in os.listdir(os.curdir)[1:]:
        episode = re.split(r'(\d{1,3})(.*)', vid, re.M|re.I)[1]
        new_name = episode + '.mp4'
        print "Renaming %s to %s" %(vid, new_name)
        os.rename(vid, new_name)

    print "Done renaming files."
