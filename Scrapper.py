import os
from time import sleep
import multiprocessing
import requests
import re

def download(url,x,y):
    if not y: # Sanity check Folder empty
        return
    if not os.path.exists(os.getcwd()+"/"+str(x)): # if folder not exists
        os.makedirs(str(x))
    conn=requests.get(url, stream=True)
    try:
        with open(os.getcwd()+"/"+str(x)+"/"+str(y),"wb") as f:
            try:
                for chunk in conn.iter_content(chunk_size=1024*1024):
                    try:
                        if chunk:
                            f.write(chunk)
                    except:
                        pass
            except:
                pass
    except:
        pass


#inp => re => tool 
# https://www.ict.griffith.edu.au/images/Box/east.gif
num = 1
#url=https://www.ict.griffith.edu.au/images/Box
print("Welcome to Python Downloader 1.0")
print("Enter URL: ")
url=input()
r = requests.get(url)
if r.status_code == 200:
    print('URL is Valid!')
elif r.status_code == 404:
    print('invalid URL')
    exit()
str_to_search = r.text # Source Code text format
pattern1 = re.compile(r'<a [^>]*href="([^"]+)') # tool to extract links
songs1 = pattern1.findall(str_to_search) # List
print(songs1)
print("What is the type of data to be Downloaded?")
print("1) Video","2) Pictures","3) Other",end="\n")
choice=int(input())
print("Download has started")
for x in songs1[6:]:
    rr = requests.get(url+str(x))
    songs2 = pattern1.findall(rr.text)
    if choice == 1:
        data=[(url+str(x)+ str(y),x,y) for y in songs2[1:]]
        for val in data:
            download(*val) # unpack tuple to arguments
    else:
        processes = [multiprocessing.Process(target=download ,args=(url+str(x)+ str(y),x,y)) for y in songs2[6:]]
        [process.start() for process in processes]
        [process.join() for process in processes]

