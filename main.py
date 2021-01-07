import pexpect
import time 
import colors

bulb = '44:A6:E5:1E:0D:F7'

#red, green, blue, pink, purple, orange, yellow, lime, light blue, off, on
nums = [
    RED,
    GREEN,
    BLUE,
    PINK,
    ORANGE,
    YELLOW,
    LIME,
    LIGHT_BLUE
]

gatt = pexpect.spawn('gatttool -I')

gatt.sendline('connect ' + bulb)
gatt.expect('Connection successful')

while True :
    for i in nums :
        gatt.sendline('char-write-cmd 0x0025 ' + i)
        time.sleep(.01)




