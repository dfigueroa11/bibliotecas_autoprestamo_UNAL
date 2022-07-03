# demo_ps2io.py -- simple demo of ps2io PS/2 keyboard library
# 2021 @todbot
# Tested on ESP32S2 Saola board and ItsyBitsy M4 running CircuitPython 6.2.0

import board

# ESP32S2 Saola
#kbd = ps2io.Ps2(board.IO33, board.IO34)
# ItsyBitsy M4
ps2_data_pin = board.D7
ps2_clock_pin = board.D9


import time
import ps2io
class PS2Keyboard:
    # helpful: https://www.avrfreaks.net/sites/default/files/PS2%20Keyboard.pdf
    # helpful: https://wiki.osdev.org/PS/2_Keyboard
    scanset2_us = {
        'code': [
            0, 'F9', 0, 'F5', 'F3', 'F1','F2', 'F12', 0, 'F10', 'F8', 'F6', 'F4', 'TAB', '`', 0, # 00-0F
            0, 'LALT', 'LSHIFT', 0, 'LCTRL', 'q', '1', 0, 0, 0, 'z', 's', 'a', 'w', '2', 0, #10-1F
            0, 'c', 'x', 'd', 'e', '4', '3', 0, 0, ' ', 'v', 'f', 't', 'r', '5', 0, #20-2F
            0, 'n', 'b', 'h', 'g', 'y', '6', 0, 0, 0, 'm', 'j', 'u', '7', '8', 0, #30-3F
            0, ',', 'k', 'i', 'o', '0', '9', 0, 0, '.', '/', 'l', ';', 'p', '-', 0, #40-4F
            0, 0, '\'', 0, '[', '=', 0, 0, 'CAPSLOCK', 'RSHIFT', 'ENTER', ']', 0, '\\', 0, 0, # 50-5F
            0, 0, 0, 0, 0, 0, 'BKSP', 0, 0, '1', 0, '4', '7', 0, 0, 0, # 60-6F
            '0', '.', '2', '5', '6', '8', 'ESC', 0, 'F11', '+', '3', '-', '*', '9', 0, 0, # 70-7F
            0, 0, 0, 'F7', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 # 80-8F
        ],
        'ext': {
            0x11:'RALT',
            0x14:'RCTRL',
            0x1f:'LGUI',
            0x27:'RGUI',
            0x2F:'APPS',
            0x4a:'KP/',
            0x5a:'KPENTER',
            0x6b:'LEFT',
            0x74:'RIGHT',
            0x75:'UP',
            0x72:'DOWN',
            0x69:'END',
            0x6c:'HOME',
            0x70:'INSERT',
            0x71:'DELETE',
            0x7a:'PGDN',
            0x7d:'PGUP',
            0x7e:'SCROLLLOCK',
            0x77:'NUMLOCK',
        }
    }
        
    def __init__(self,data_pin, clk_pin, scanset=scanset2_us):
        self._kbd = ps2io.Ps2(data_pin,clk_pin)
        for i in range(len(self._kbd)):
            self._kbd.popleft()  # clear any buffered data            
        self._scanset = scanset

    def set_leds(self, scroll_lock=False,num_lock=False, caps_lock=False):
        arg = (caps_lock << 2) | (num_lock << 1) | (scroll_lock )
        # turn on scroll-lock led  # might fail
        rc = self._kbd.sendcmd(0xED)  # should return 0xFA (ACK)
        #print("rc:%x" % rc)
        rc = self._kbd.sendcmd(arg)  # should return 0xFA (ACK)
        #rc = self._kbd.sendcmd(0x01)  # should return 0xFA (ACK)
        #print("rc:%x" % rc)

    def get_scancodeset_id(self):
        # get scancode set in use by keyboard
        rc = self._kbd.sendcmd(0xF0)  # get/set scancode set
        #print("rc:%x" % rc)
        rc = self._kbd.sendcmd(0x00)  # get scancode subcmd
        #print("rc:%x" % rc)
        while len(self._kbd) is 0: pass
        codeset = self._kbd.popleft()
        return codeset
    
    def key_translate(self,code,code_ext,code_release):
        if code_ext:  # extended scancode
            key = self._scanset['ext'].get(code)
        else:         # normal
            key = self._scanset['code'][code]
        return (key, code_release==0xF0)

    def read_key(self, timeout=5):
        now = time.monotonic()
        code_ext = 0  # is this an extended keycode or not (normally 0xE0)
        code_release = 0 # is this a key-up, rather than a keydown (normally 0xF0)
        while True:
            while len(self._kbd) is 0: pass # timeout not implemented yet
            code = self._kbd.popleft()
            #print("code:%x"%code)
            if code == 0xE0:   # extended scancode
                code_ext = code
            elif code == 0xF0: # release scancode
                code_release = code
            #elif code == 
            elif code < len(self._scanset['code']):
                (key,release) = self.key_translate(code, code_ext, code_release)
                return (key, release, code,code_ext)
            else:
                print("UNKNOWN code", code)

time.sleep(1)
print("ps2io_demo.py hello!")

kbd = PS2Keyboard( ps2_data_pin, ps2_clock_pin )

print("setting keyboard scroll lock LED")
#kbd.set_leds(scroll_lock=True, num_lock=False, caps_lock=True)
kbd.set_leds(scroll_lock=True)

codeset_id = kbd.get_scancodeset_id()
print("keyboard is reporting scancode set:",codeset_id)

while True:
    (key, release, code,code_ext) = kbd.read_key()
    print("key:%s code:%x/%x: release:%x" % (key, code,code_ext,release))
    #print("key:",key)