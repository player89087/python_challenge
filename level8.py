import bz2 
# we got a picture of a fly that make bzzzz --> bz2 compressed files 
# BZh for bzip2 

# if click on picture input for credentials 
user =  b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084' # b for binary otherwise error
password = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

# decompress them 
print(bz2.decompress(user).decode('utf-8'))
print(bz2.decompress(password).decode('utf-8'))
