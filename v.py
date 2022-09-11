print("Enter you msg   >>>")
nachischt = input()
print("Enter your key   >>>")
Schlüssel = int(input())

cipher = ""

for ch in nachischt:
    if ch >=  "a" and  ch <= "z":
        pos= ord(ch) - ord ("a")
        pos= (pos+Schlüssel ) % 26
        cipher = cipher + chr(pos + ord ("a"))   
 

    elif ch >=  "A" and  ch <= "Z":
       pos= ord(ch) - ord ("A")
       pos= (pos+Schlüssel ) % 26
       cipher = cipher + chr(pos + ord ("A"))
  

    else:
       cipher = cipher + ch

print( "Your encrypt msg"+ nachischt )

print("Your decrypt msg  "+ cipher)
