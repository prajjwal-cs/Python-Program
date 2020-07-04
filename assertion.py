try:
    c=int(input())
    assert c>=5 and c<=10
    print(c)
except AssertionError:
    print("Invalid input")
