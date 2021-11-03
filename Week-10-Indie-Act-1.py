# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, nor tolerate those who do"
#   "I have not given or received any unauthorized aid on this assignment"
#
# Names: 	Daniel La Cour
# Section: 557
# Assignment: Lab10Indie Act 1
# Date: 1 November 2021
import os

def count(array): # counts the intsances of items in an array, returns them as a dictionary
    seenvalues = {} # dictionary that holds the extension and the number of occurrences
    for i in array:
        if i in seenvalues.keys(): # if the extension has been seen before
            seenvalues[i] += 1 # increments the extensions seen count
        else:
            seenvalues[i] = 1 # initialize extension in dict
    return seenvalues # returns the dictionary

def sizes(array):
    totalusage = 0 # starts at 0 bytes
    fileswithsizes = {} # dictionary containing the file path and it's size
    for file in array:
        totalusage += os.path.getsize(file) # adds file's size to total
        fileswithsizes[file] = os.path.getsize(file) # assign's the file to its size in the dict
    return totalusage, fileswithsizes # return both total and dict

def percents(total, table):
    percenttable = {} # same as above, but with percents basically
    for value in table.keys():
        percenttable[value] = (table[value]/total)*100
    return percenttable

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

filelist, extensionlist, fullnamelist = getfiles(input("Input full path of directory to scan:")) # gets the data from getfiles

extensions = count(extensionlist)
filesizes = sizes(fullnamelist) # runs previously defined funcs
filepercents = percents(*sizes(fullnamelist))
with open("analysis-results.txt", 'w+') as results: # opens a file to write analysis results
    #each of the below writes the data as it should, with respect to each analysis option.
    results.write("Extension counts:")
    for key in extensions.keys():
        results.write('\n\t'+key+": "+str(extensions[key]))
    results.write("\nFile sizes:")
    for key in filesizes[1]:
        results.write('\n\t'+key+": "+str(filesizes[1][key]))
    results.write("\nFile percents:")
    for key in filepercents.keys():
        results.write('\n\t'+key+": "+str(filepercents[key])+"%")
print('Done')