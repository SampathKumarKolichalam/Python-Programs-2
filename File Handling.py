#Opening a file:-"r"
o=open("Loops.py","r")
#print(o.read())

#Writing into a file:-"w","a"
w=open("ABC","w")
#w.write("Hello Sampath Kumar")
#w.write("How are you?")

#Writing/Copying one file data into another file:-
for data in o:
    w.write(data)

