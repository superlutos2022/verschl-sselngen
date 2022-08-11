print("Bitte geben sie  den text ein den  sie entschlüsseln wollen")
nachischt_str = input()
print("Bitte  geben sie den  schlüssel ein  mit den  sie  den text enschlüsseln wollen")
Schlüssel_int = int(input())

cipher_str = ""

for ch in nachischt_str:
    if ch >=  "a" and  ch <= "z":
        pos= ord(ch) - ord ("a")
        pos= (pos+Schlüssel_int ) % 26
        cipher_str = cipher_str + chr(pos + ord ("a"))   
 

    elif ch >=  "A" and  ch <= "Z":
       pos= ord(ch) - ord ("A")
       pos= (pos+Schlüssel_int ) % 26
       cipher_str = cipher_str + chr(pos + ord ("A"))
  




    else:
       cipher_str = cipher_str + ch

print("Der entschlüsselte text lautet :  "+ cipher_str)
