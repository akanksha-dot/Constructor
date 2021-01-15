## COUNT NUMBER OF WORDS IN A TEXT FILE

#### file2.txt file going to be created  in file handling folder
f=open('file2.txt','w')
data=["File is a collection of data"]### created a list containing group of characters
f.writelines(data)### using write mode it will write content of data in file2.txt file
for line in data:
    print(line)
    
## using read mode ,reading content of existing file and mean while it will count numbers of words
f=open('file2.txt','r')
call=f.read()
words=call.split()
word=len(words)
print(call)
print("number of words:",word)
f.close()

##COUNT NUMBER OF CHARACTERS

g=open('file2.txt','r')

call=g.read()

characters=len(call)

print(call)

g.close()

print("number of characters:",characters)
