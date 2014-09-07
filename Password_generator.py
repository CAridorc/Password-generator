# -*- coding: UTF-8 -*-
#######################################################################
# This programme creates a random password for you                    #
# respecting the parametres you set at the start                      #
# License : GNU CC 3.0                                                #
# Author : Caridorc Tergilti                                          #
#######################################################################


#### PARAMETRES ####
LENGTH = 16         # How many characters do you want in your password?

TYPES = ['digits-0-9','alphabet','alphabet and digits',
        'alphabet with uppercase and digits','all characters']

TYPE = 'alphabet'  # Chose the type of your password
                   # IMPORTANT: It must be in the list TYPES
                   # If you want a random type write TYPE = ''
                   
START = ''         # What should your password start with?
                   # Leave '' for random
                   
END = ''           # What should your password end with?
                   # Leave '' for random
#### END OF PARAMETRES ####

#######################################################################
#######################################################################
### If you modify something after this comment block                ###
### the programme may stop working or get weird bugs,               ###
### modify it only if you know what you are doing !                 ###
#######################################################################
#######################################################################

import random
digits = '0123456789'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_with_uppercase = '''abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
digits_and_alphabet = digits + alphabet
all_characters = '''\1234567890'ìqwertyuiopè+asdfghjklòàù
<zxcvbnm,.-!"£$%&/()=?^QWERTYUIOPé*ASDFGHJKL°§ZXCVBNM;:_[]@#`·{}×'''

if TYPE == 'digits-0-9' : TYPE = digits
if TYPE == 'alphabet' : TYPE = alphabet
if TYPE == 'alphabet and digits' : TYPE = digits_and_alphabet
if TYPE == 'alphabet with uppercase and digits' : TYPE = alphabet_with_uppercase
if TYPE == 'all characters' : TYPE = all_characters

password = START
while len(password) < (LENGTH - len(END)):
	password = password + random.choice(TYPE)
	
password = password + END

print(password)
