import time
import machine
import utime
import st7789
import tft_config
import adafruit_mlx90640
import network as MOD_NETWORK
import ufirebase

tft = tft_config.config(1)
machine.freq(240000000)
mlx = adafruit_mlx90640.MLX90640(machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21), freq=400000))
frame = [0] * 768  # Update the size to accommodate a 32x24 frame
heat_map = []
rect_hig = 6       # Adjust the rectangle height to fit the new frame size
rect_wid = 8

# Connect to Wi-Fi
GLOB_WLAN = MOD_NETWORK.WLAN(MOD_NETWORK.STA_IF)
GLOB_WLAN.active(True)
GLOB_WLAN.connect('IOT-WU', 'iot123456')

# Firebase example
URL = ("https://data-esp32-718d0-default-rtdb.firebaseio.com/")

# Get current time
UTC_OFFSET = +7 * 60 * 60  # '+7' คือ Timezone ของเวลาประเทศไทย
actual_time = time.localtime(time.time() + UTC_OFFSET)

# Set time
rtc = machine.RTC()
rtc.datetime((actual_time[0], actual_time[1], actual_time[2], 0, actual_time[3], actual_time[4], actual_time[5], 0))

def get_current_time():
    t = rtc.datetime()
    return '{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}'.format(t[0], t[1], t[2], t[4], t[5], t[6])

def send_data_to_cloud(currentTime, message):
    try:
        path = "DemoData/" + currentTime + "/"
        ufirebase.put(path, ujson.dumps(message), bg=0)  # Convert message to JSON string
        print("Data sent successfully!\nAt Time:", currentTime)
        print("-" * 50)
    except Exception as e:
        print('Cannot Publish to Firebase...', e)
        machine.reset()

def display_frame_data():
    tft.init()
    tft.fill(st7789.BLACK)

    while True:
        try:
            currentTime = get_current_time()
            mlx.getFrame(frame)
            tft.fill(st7789.BLACK)
            heat_map.clear()
            message = []

            for i in range(24):
                row = []
                for j in range(32):
                    temperature = frame[i * 32 + j]
                    row.append(temperature)
                heat_map.append(row)
                message.append(row)

            for i in range(24):
                for j in range(32):
                    temperature = heat_map[i][j]
                    color = temperature_to_color(temperature)
                    tft.fill_rect(j * rect_wid, i * rect_hig, rect_wid, rect_hig, color)

            print(message)
            # Create the data to be sent to Firebase
            data = {
                'temperatures': message
            }

            send_data_to_cloud(currentTime, data)
            gc.collect()

        except Exception as e:
            print(e)
            machine.reset()

def temperature_to_color(temperature):
    if temperature < 27.99:
        return st7789.color565(2, 2, 196)
    elif temperature < 28.51:
        return st7789.color565(0, 0, 255)
    elif temperature < 28.99:
        return st7789.color565(29, 63, 231)
    elif temperature < 29.51:
        return st7789.color565(52, 83, 235)
    elif temperature < 29.99:
        return st7789.color565(52, 112, 235)
    elif temperature < 30.51:
        return st7789.color565(52, 142, 235)
    elif temperature < 30.99:
        return st7789.color565(52, 177, 235)
    elif temperature < 31.55:
        return st7789.color565(83, 213, 83)
    elif temperature < 31.99:
        return st7789.color565(52, 235, 235)
    elif temperature < 32.55:
        return st7789.color565(52, 235, 191)
    elif temperature < 32.99:
        return st7789.color565(52, 235, 110)
    elif temperature < 33.55:
        return st7789.color565(177, 235, 52)
    elif temperature < 33.99:
        return st7789.color565(187, 235, 52)
    elif temperature < 34.55:
        return st7789.color565(228, 235, 52)
    elif temperature < 34.99:
        return st7789.color565(235, 195, 52)
    elif temperature >= 35.00:
        return st7789.color565(235, 131, 52)


# Main program
display_frame_data()
