'''
Binary files handles the data in the form of bytes. Hence they can be used to read or write  txt, images, audio
and video files. to open a binary file we can use
rb
ab
rb+
wb
wb+
ab+

'''
f=open("lg6.jpg",'rb')
f1=open("new.jpg",'wb')
by=f.read()
f1.write(by)
f.close()
f1.close()
