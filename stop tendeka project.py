from machine import Pin, I2C
import ssd1306

# Initialize OLED display
i2c = I2C(-1, Pin(22), Pin(21))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

# Initialize input pins for sensors
sensor_enter = Pin(14, Pin.IN)
sensor_exit = Pin(12, Pin.IN)

# Initialize output pin for LED
led = Pin(13, Pin.OUT)

# Initialize counter variable
people_inside = 0

# Function to update display and LED
def update_display_and_led():
    # Update OLED display
    oled.fill(0)
    oled.text(" STOP TENDEKA:", 2, 0)
    oled.text("+______________+", 0, 6)
    oled.text(" ABARIMO :", 2, 18)
    oled.text(str(people_inside), 100, 18)
    oled.show()
    
    # Update LED and you can enter number of car what it car
    if people_inside > 10:
        led.on()
    else:
        led.off()

# Loop to continuously read sensors and update counter
while True:
    # Check if someone enters
    if sensor_enter.value() == 1:
        people_inside += 1
        update_display_and_led()
    
    # Check if someone exits
    if sensor_exit.value() == 1:
        people_inside = max(0, people_inside - 1)  # ensure people_inside >= 0
        update_display_and_led()
