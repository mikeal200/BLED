import pexpect
import time 

bulb = '44:A6:E5:1E:0D:F7'

#red, green, blue, off, on
nums = ['545c1df148b649494641', '545cfc10a9a857a8a7a0', '545c20cc7574748b7b7c', '545cf71ba7a3a3a3a3a3', '545c28c4787d7c7c7c7c']

red = list('545c1df148b649494641')

gatt = pexpect.spawn('gatttool -I')

gatt.sendline('connect ' + bulb)
gatt.expect('Connection successful')

charNum = 3

for x in range(16) :
    
    red[charNum] = x 

    if x == 10 :
        red[charNum] = 'A'
    elif x == 11 :
        red[charNum] = 'B'
    elif x == 12 :
        red[charNum] = 'C'
    elif x == 13 :
        red[charNum] = 'D'
    elif x == 14 :
        red[charNum] = 'E'
    elif x == 15 :
        red[charNum] = 'F'
    
    print(red)
    gatt.sendline('char-write-cmd 0x0025 ' + str(red))
    time.sleep(.5)
