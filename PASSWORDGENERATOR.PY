				PASSWORDGENERATOR
importsecrets
import string
defcreate_pw(pw_length=12):
letters=string.ascii_letters
digits = string.digits
special_chars=string.punctuation
alphabet=letters+digits+special_chars pwd
= ''
pw_strong=False
whilenotpw_strong:
pwd = ''
fori inrange(pw_length):
pwd+=''.join(secrets.choice(alphabet))
if(any(charinspecial_charsforcharinpwd)and sum(char
in digits for char in pwd) >= 2):
pw_strong=True
return pwd
if name =='main':
print(create_pw())
