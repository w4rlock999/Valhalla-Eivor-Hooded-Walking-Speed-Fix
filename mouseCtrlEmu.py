import vgamepad as vg
from pynput import mouse

def on_scroll(x, y, dx, dy):
    global Speed
    if dy > 0:
        Speed = min(1.0, Speed + 0.1)  # Increase Speed, capped at 1.0
    else:
        Speed = max(0.7, Speed - 0.1)  # Decrease Speed, minimum 0.7

def on_click(x, y, button, pressed):
    global Speed, stopped
    if button == mouse.Button.x2:
        if pressed:
            if stopped:
                Speed = 0.7  # Restart at 0.7 speed if stopped
                stopped = False
            else:
                stopped = True
                Speed = 0  # Set speed to stop (0.5) if not stopped
                print("should stop now?")

def main():
    global Speed, stopped
    Speed = 0.7  # Initial speed value
    stopped = False  # Flag to track whether the virtual joystick is stopped

    gamepad = vg.VX360Gamepad()

    with mouse.Listener(on_scroll=on_scroll, on_click=on_click) as listener:
        try:
            print("Listening for mouse events. Press Ctrl+C to stop.")
            while True:
                # Read the y-value from the mouse scroll and apply speed multiplier
                y_value = int(Speed * 32767)

                # Set the left joystick's x and y values (values between -32768 and 32767)
                gamepad.left_joystick(x_value=0, y_value=y_value)

                # Update the virtual gamepad to apply the changes
                gamepad.update()

        except KeyboardInterrupt:
            print("Mouse event listener stopped.")

if __name__ == "__main__":
    main()
