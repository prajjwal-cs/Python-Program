'''
With statement
it can be used while opening a file. The advantage of with statemant that
it will take care of closing a file. Hence wi not need to close a file.
syntax
with open("filename",'mode') as f:
'''
with open("yt.txt",'w') as f:
    f.write("i am learning python")
