def on_button_pressed_ab():
    radio.send_string("I love you mama")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    continue
    scrollbit.scroll_text(receivedString, 255, 50)
radio.on_received_string(on_received_string)

scrollbit.clear()
radio.set_group(1)
break