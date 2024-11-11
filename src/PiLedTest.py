import hal.hal_input_switch as switch
import hal.hal_led as led
import time as time
def main():
    switch.init()
    led.init()
    led_state= False
    start_time=0
    elaspsed_time=0

    while True:
        if switch.read_slide_switch():
            led.set_output(0,led_state)
            led_state=not led_state
            print(led_state)
            time.sleep(0.2)
            start_time=0
            elaspsed_time=0
        else:
            if start_time==0:
                start_time=time.time()
            if elaspsed_time < 5:
                led.set_output(0,led_state)
                led_state= not led_state

                time.sleep(0.1)

                elaspsed_time=time.time() - start_time
                print(elaspsed_time)
            else:
                led.set_output(0,0)

if __name__ == "__main__":
    main()
