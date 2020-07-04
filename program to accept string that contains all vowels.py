def check(string):
    vowels=set("aeiou")
    s=set({})
    for i in string:
        if i in vowels:
            s.add(i)
        else:
            pass

    if len(s)==len(vowels):
        print("Accepted")
    else:
        print("not Accepted")

string=input("enter a word:")
string=string.lower()
check(string)
