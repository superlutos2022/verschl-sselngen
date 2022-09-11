Alpapet = ["a", "b" ,"c", "d", "e" ,"f" , "g", "h", "i","j", "k" ,"l" , "m", "n" ,"o" ,"p", "q","r" ,"s" ,"t" , "u" ,"v", "w", "x" ,"y" ,"z"]


msg = input("Enter you Msg   >>>")
key = input("Enter your key   >>>")


final = ""

for x in msg:

    if x in Alpapet:
        z = Alpapet.index(x)
        letter = (Alpapet[z+int(key)])
        final = final + letter
        
    else:
        False

print("Your decrypt msg = " + msg)
print("Your encrypt msg = " + final)
print("the key you used = " + key)