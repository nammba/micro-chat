def on_button_pressed_ab():
    radio.send_string("I love you mama")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

basic.clear_screen()
radio.set_group(1)