import hal.hal_input_switch as switch
import hal.hal_led as led
import time as time


def read_switch():
    switch.init()
    led.init()
    if switch.read_slide_switch == 1:
        return led.set_output(24,1)
        time.sleep(0.2)
    else:
        return led.set_output(24,0)
    

