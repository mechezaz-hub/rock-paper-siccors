radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    let Serialnumber = 0
    Serial = radio.receivedPacket(RadioPacketProperty.SerialNumber)
    Match = Tool == receivedNumber
    Player_index = Players.indexOf(Serialnumber)
    Found = Player_index >= 0
    if (Match && !Found) {
        Players.push(Serialnumber)
    }
    
    if (!Match && Found) {
        Temp = Players.removeAt(Player_index)
    }
    
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    Players = [0]
    Tool = randint(1, 3)
    radio.sendNumber(Tool)
    if (Tool == 1) {
        basic.showIcon(IconNames.SmallSquare)
        music.setBuiltInSpeakerEnabled(true)
    }
    
    if (Tool == 2) {
        basic.showIcon(IconNames.Square)
    }
    
    if (Tool == 3) {
        basic.showIcon(IconNames.Scissors)
    }
    
})
let Temp = 0
let Found = false
let Player_index = 0
let Tool = 0
let Match = false
let Serial = 0
let Players : number[] = []
radio.setGroup(10)
radio.setTransmitSerialNumber(true)
Players = [0]
basic.forever(function on_forever() {
    basic.showNumber(Players.length)
})
