input.onButtonPressed(Button.A, function () {
    radio.sendString("I love you mama")
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
basic.clearScreen()
radio.setGroup(1)
