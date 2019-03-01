from gpiozero import LED, Button
from signal import pause

led = LED(22)
button = Button(4)

button.when_pressed = led.on
button.when_released = led.off

pause()
