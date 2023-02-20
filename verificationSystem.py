## IMPORTS -------------------------------------------------------
import hashlib
import linecache

##VERIFICATION SYSTEM FUNCTIONS -----------------------------------
#This function opens the password.txt and salt.txt files to read the first lines to obtain salt and password values
#per assignment requirements
def fileExtraction():
    #Obtain first password for user id 1
    pw_file = open("Password.txt", "r")
    password = pw_file.readline()
    pw_file.close()

    #Obtain first salt value for user id 1
    salt_file = open("Salt.txt", "r")
    salt = salt_file.readline()
    salt_file.close()

    #Strip the password and salt of any new lines/spaces and return concatenation
    concat_txt = password.strip() + salt.strip()
    return concat_txt

#This function computes the hash value of a concatenated combination of a given password and salt value
def computeMD5hash():
    return

#This function verifies the hash value by extraction given a specific user id and compares this with computed hash value
def verifyHash():
    return

