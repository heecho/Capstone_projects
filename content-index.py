import string
import os

"""

Notes:

Look into array .extend() method
Look into string module , and .punctuation
Look into the set() builtin data type

"""
dirname = "."
#find all text files in current directory, return array of file names
def recursive_find(dirname):
    file_list = []
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isdir(path):
            file_list.extend(recursive_find(path))
        else:
            file_list.append(name)
    return file_list

stop_words = ['a','an','and','i']

#reads text in file, returns string of text
def read_data(filename):
    with open(filename,"r") as f:
        return f.read()

#token is output of read_data, strips punctuation from text
def strip_punctuation(token):
    return ''.join(ch for ch in token if ch not in string.punctuation)
    
#converts string to array of words and strips stops words.
#set removes duplicates in array
def index_file(filename):
    """Index one file return a cleaned array of words"""
    file_content = []
    lines = strip_punctuation(read_data(filename))
    lines = lines.lower()
    lines.replace("\n",' ')
    file_content.extend(lines.split())
    for word in file_content:
        if word in stop_words:
            file_content.remove(word)
    clean_index = set(file_content)
    return clean_index

index = {}
#adds each word to hash, and associated filename to array
#index = {'word': [associated filenames]}
def add_to_index(words,filename,index):
    """takes a set of words for a filename and adds it to the index"""
    for word in index_file(filename):
        if index.has_key(word):
            index[word].append(filename)
        else:
            index[word] = []
            index[word].append(filename)
    return index

#build out index has for all filenames found
def index_all_files(file_list,index):
    """go through the list of files and add a file's words to the index"""
    for filename in file_list:
        add_to_index(index_file(filename),filename,index)
    return index

#index_all_files(recursive_find(dirname),index)

def find_files_with(index,keywords):
    """takes a list of keywords, and return a list of files with those keywords"""
    for word in keywords:
        index_all_files(recursive_find(dirname),index)
        if index.has_key(word):
                print index[word]

find_files_with(index,["cats","mango","ski"])

      

        

