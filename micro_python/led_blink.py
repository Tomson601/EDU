import machine, utime


led_onboard = machine.Pin("LED", machine.Pin.OUT)

while True:
    led_onboard.toggle()
    print(led_onboard.value())
    input("STOP")
    utime.sleep(0.175)
