import pyautogui
import time

print("Monitorando posição do mouse. Pressione Ctrl+C para parar.\n")

try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x:4d}  Y: {y:4d}", end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nMonitoramento encerrado.")
