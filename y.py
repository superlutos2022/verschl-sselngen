alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


msg = input('enter your msg: ')
key = input('enter your key: ')

encrypt_msg = ""


for x in msg:


    if x in alpha:
       new_index = int(alpha.index(x)) + int(key)


       if (new_index > 25):
        new_index = new_index - 26
       new_letter = alpha[new_index]
       encrypt_msg = encrypt_msg + str(new_letter) 


    else:
        new_letter = " "
        encrypt_msg = encrypt_msg + str(new_letter)  


print("Your decrypt msg = " + msg)
print("Your encrypt msg = " + encrypt_msg)
print("the key you used = " + key)