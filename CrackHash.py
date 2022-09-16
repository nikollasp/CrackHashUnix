#Master0z0 22-09
import passlib
from passlib.hash import bcrypt

Hash = "$2b$10$nOUIs5kJ7naTuTFkBy1veuK0kSxUFXfuaOKdOKf9xYT0KKIGSJwFa" #HASH COLLECTED TO MATCH
with open('/FILE/PATH/wordlist.txt','r') as arq: #WORDLIST WITH THE PASSWORD POSSIBLE, OPEN AND READ THE FILE
     wordlist = arq.readlines()
for word in wordlist:
    word = word.strip('\n') #OPTIONAL - STRING TREATMENT
    hashMatched = bcrypt.hash(word,salt='nOUIs5kJ7naTuTFkBy1veu',rounds=5) #GENERATE HASH OF WORDS INCLUDED IN HASH ABOVE, SALT IS INCLUDED IN HASH ABOVE(FIRST 22 CHARS AFTER THIR"$")
    if hashMatched == Hash:
        print("\n\nIt Matches! :)")
        print("Hash: ",hashMatched)
        print("Password cleartext:",word)
        break
    else:
        print("It Does not Match :(")
        print("hashed: ",hashMatched)

