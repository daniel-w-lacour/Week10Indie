# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, nor tolerate those who do"
#   "I have not given or received any unauthorized aid on this assignment"
#
# Names: 	Daniel La Cour
# Section: 557
# Assignment: Lab10Indie Act 2
# Date: 1 November 2021
import os
def sizes(array):
    totalusage = 0 # starts at 0 bytes
    fileswithsizes = {} # dictionary containing the file path and it's size
    for file in array:
        totalusage += os.path.getsize(file) # adds file's size to total
        fileswithsizes[file] = os.path.getsize(file) # assign's the file to its size in the dict
    return totalusage, fileswithsizes # return both total and dict

def getfiles(pathz): # gets all the files in a SINGLE directory (___NOT___ including subdirectories)
    extensions = [] # list of extensions
    fullnames = [] # list of full paths
    files = [] # lits of file names wihtout extensions
    for (_, _, filenames) in os.walk(pathz): # gets only the filenames w/ extension.
        for file in filenames:
            fullnames.append(pathz+file) # adds the path + filename to the array
            name, file_extension = os.path.splitext(pathz+file)  #splits the filename and extension
            files.append(name)
            extensions.append(file_extension)
        break
    return files, extensions, fullnames

maliciousfiles = {'hack.exe': 1337, 'rshell.pwn': 8888, 'totallysafeinstaller.msi': 99, 'firefox.exe': 500} # list of "malicious" files along with the expected size.
scanpath = input("input the full path to scan: ")
_,_,fullnames = getfiles(scanpath) # gets full names of each file in current directory
breaker = 0 # breaker to let us know if a malicious file was detected.
for file in fullnames:
    if file.split('/')[-1] in maliciousfiles.keys() and os.path.getsize(file) == maliciousfiles[file.split('/')[-1]]: #if the full filename is a key in the malicious file dict, and the size ofthe file matches the known value
        print("Malicious file found:",file.split('/')[-1]) # prints the malicious file's name
        breaker = 1 #trips the breaker
if breaker == 0:
    print("Scan yielded no results. Always scan using multiple solutions.")
