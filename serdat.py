import pydirectinput
import keyboard
from PIL import ImageGrab
from colorama import Fore, Style
import time
import winsound

def is_renk_tonu(x, y, width, height, r_range, g_range, b_range):
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    pixels = screenshot.getdata()
    for r, g, b in pixels:
        if (r in range(r_range[0], r_range[1]+1) and g in range(g_range[0], g_range[1]+1) and b in range(b_range[0], b_range[1]+1)):
            return True
    return False

def press_key(key, duration=0.010):
    pydirectinput.keyDown(key)
    time.sleep(duration)
    pydirectinput.keyUp(key)

def colorful_text(text, color):
    return f"{color}{text}{Style.RESET_ALL}"

def yazdir_with_interval(yazi, aralik_saniye):
    for harf in yazi:
        print(harf, end='', flush=True)
        time.sleep(aralik_saniye)

def create_color_menu():
    while True:
        print("Color Choice")
        print("1 - Yellow")
        print("2 - Red")
        print("3 - Purple")
        color_choice = input("Make your choice (1/2/3): ")

        if color_choice == "1":
            return "yellow"
        elif color_choice == "2":
            return "red"
        elif color_choice == "3":
            return "purple"
        else:
            print("Try Again, Invaild Number")

red_text = colorful_text("Getting Ready  ...", Fore.RED)
reder_text = colorful_text("Ready", Fore.RED)
green_text = colorful_text("Made by nitrogencfg", Fore.GREEN)
blue_text = colorful_text("Press Left Alt to activate", Fore.BLUE)
cyan_text = colorful_text("Bind 'J' key to fire", Fore.CYAN)
hazir_text = colorful_text("Balkans on top  ( ͡° ͜ʖ ͡°)", Fore.MAGENTA)
info_text = colorful_text("for questions =====> https://nitrogencfg.vercel.app/", Fore.MAGENTA)
saru_tex = colorful_text("Strafe protected trigger bot", Fore.YELLOW)

yazdir_with_interval(red_text, 0.05)
print()

try:
    square_size = int(input("Input the square size in pixels:"))
except ValueError:
    print("Invaild pixels, using default size (9px) ")
    square_size = 9

width, height = square_size, square_size
print()
selected_color = create_color_menu()
print()
print(f"{selected_color.capitalize()} color is going to be searched.")
print()
yazdir_with_interval(reder_text, 0.02)
print()
print()
print(green_text)
print()
print(blue_text) 
print()
print(cyan_text)
print()
print(saru_tex)
print()
print()
yazdir_with_interval(hazir_text, 0.01)
print() 
yazdir_with_interval(info_text, 0.01) 
print()
print()

def any_keys_pressed(keys_list):
    return any(keyboard.is_pressed(key) for key in keys_list)

def beep(frequency, duration):
    winsound.Beep(frequency, duration)

script_active = False
j_pressed_time = 0

try:
    while True:
        if keyboard.is_pressed('left alt'):
            while keyboard.is_pressed('left alt'):
                time.sleep(0.1)

            script_active = not script_active
            
            if script_active:
                print("Activated")
                beep(400, 150)
            else:
                print("Deactivated")
                beep(800, 150)

        if script_active:
            if keyboard.is_pressed('j') and j_pressed_time == 0:
                j_pressed_time = time.time()
                press_key('j', duration=0.328)
            elif not keyboard.is_pressed('j'):
                j_pressed_time = 0

            current_time = time.time()
            if current_time - j_pressed_time >= 0.24:
                if not any_keys_pressed(['w', 'a', 's', 'd']):
                    ekran_genislik, ekran_yukseklik = pydirectinput.size()
                    orta_x = ekran_genislik // 2 - width // 2
                    orta_y = ekran_yukseklik // 2 - height // 2

                    if selected_color == "yellow":
                        r_range = (160, 255)
                        g_range = (140, 255)
                        b_range = (0, 55)
                    elif selected_color == "red":
                        r_range = (170, 255)
                        g_range = (0, 65)
                        b_range = (0, 40)
                    elif selected_color == "purple":
                        r_range = (140, 255)
                        g_range = (0, 125)
                        b_range = (140, 255)
                    else:  # Mor renk varsayılan
                        r_range = (120, 253)
                        g_range = (1, 105)
                        b_range = (120, 253)

                    if is_renk_tonu(orta_x, orta_y, width, height, r_range, g_range, b_range):
                        press_key('j')
        else:
            if any_keys_pressed(['w', 'a', 's', 'd']):
                j_pressed_time = time.time()

        time.sleep(0.008)

except KeyboardInterrupt:
    print("Stopping")


