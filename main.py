def on_received_number(receivedNumber):
    global Serial, Match, Player_index, Found, Temp
    Serialnumber = 0
    Serial = radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
    Match = Tool == receivedNumber
    Player_index = Players.index_of(Serialnumber)
    Found = Player_index >= 0
    if Match and not (Found):
        Players.append(Serialnumber)
    if not (Match) and Found:
        Temp = Players.remove_at(Player_index)
radio.on_received_number(on_received_number)

def on_gesture_shake():
    global Players, Tool
    Players = [0]
    Tool = randint(1, 3)
    radio.send_number(Tool)
    if Tool == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
        music.set_built_in_speaker_enabled(True)
    if Tool == 2:
        basic.show_icon(IconNames.SQUARE)
    if Tool == 3:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Temp = 0
Found = False
Player_index = 0
Tool = 0
Match = False
Serial = 0
Players: List[number] = []
radio.set_group(10)
radio.set_transmit_serial_number(True)
Players = [0]

def on_forever():
    basic.show_number(len(Players))
basic.forever(on_forever)
