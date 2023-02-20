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
def computeMD5hash(my_str):
    message = hashlib.md5()
    message.update(my_str.enocde('utf-8')) #Encode password+salt value concatenation
    return message.hexdigest()

#This function verifies the hash value by extraction given a specific user id and compares this with computed hash value
def verifyHash(hash_str, line):
    #Obtain the hash value stored in database of specific user (user id mapped to that line within Hash.txt)
    hash = linecache.getline("Hash.txt", line)

    #If the computed hash matches the hash in the database, return confirmation
    if hash.strip() == hash_str.strip():
        return "Yes, the input password matches with the hash value in the database."
    else:
        return "No, the input password does not match the hash value in the database."





## RUNNING MAIN FILE FUNCTIONS -----------------------------------------------------
#Verification System -->
concat_txt = fileExtraction()
hash_txt = computeMD5hash(concat_txt)
print("Concatenation: ", concat_txt)
print("Compute: ", hash_txt)
print(verifyHash(hash_txt, 1), "\n")