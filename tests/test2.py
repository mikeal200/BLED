import pexpect
import time 

bulb = '44:A6:E5:1E:0D:F7'

#red, green, blue, off, on
#nums = ['545c1df148b649494641', '545cfc10a9a857a8a7a0', '545c20cc7574748b7b7c', '545cf71ba7a3a3a3a3a3', '545c28c4787d7c7c7c7c']

gatt = pexpect.spawn('gatttool -I')

gatt.sendline('connect ' + bulb)
gatt.expect('Connection successful')

gatt.sendline('char-write-cmd 0x0025 545c1df148b649494641')
#                                    545c1df148b649494641
