def letter_counter(letter,string):
    count=0
    for i in string:
        if letter==i:
            count+=1
    return count
def greeting(name):
    print('Hello,',name)