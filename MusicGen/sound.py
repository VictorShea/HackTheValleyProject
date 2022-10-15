def convert_sound(sound: str):
    first = sound[0]
    sound = sound.split("s")[1:]
    if (first == "c"):
        tone = sound[1:-1]
    else:
        tone = sound[:-1]
    time = sound[-1]
    time = time.replace("p", ".")
    if "q" in time:
        time = time.split("q")
        time = int(time[0]) / int(time[1])

    return tone, float(time)

import midiutil
from IPython.display import Audio
from pretty_midi import PrettyMIDI
import time

test_list = [(['E5', 'A5', 'E5', 'A5'], 0.25), ([], 0.25), (['E4', 'Cw4'], 0.25), (['E4', 'Cw4'], 0.25),
             (['E4', 'Cw4'], 0.25), (['E3', 'G3'], 0.25), (['Bt3', 'A3'], 0.25), ([], 0.25), (['E4', 'Cw4'], 0.25),
             (['E3', 'G3'], 0.25), (['Bt3', 'A3'], 0.25), ([], 0.25), (['E4', 'Cw4'], 0.25), (['E3', 'G3'], 0.25),
             (['Bt3', 'A3'], 0.25), ([], 0.25), (['E4', 'Cw4'], 0.25), (['E3', 'G3'], 0.25), (['Bt3', 'A3'], 0.25),
             ([], 0.25), (['E4', 'Cw4'], 0.25), (['E4', 'Cw4'], 0.25), (['E4', 'Cw4'], 0.25), (['E4', 'Cw4'], 0.25),
             (['E3', 'G3'], 0.25), (['Bt3', 'A3'], 0.25), ([], 0.25), (['E4', 'Cw4'], 0.25), (['E4', 'Cw4'], 0.25),
             (['E4', 'Cw4'], 0.25)]
notes_to_midi = {'G9': 127, 'Fw9': 126, 'Gt9': 126, 'F9': 125, 'E9': 124, 'Dw9': 123, 'Et9': 123, 'D9': 122,
                 'Cw9': 121, 'Dt9': 121, 'C9': 120, 'B8': 119, 'Aw8': 118, 'Bt8': 118, 'A8': 117, 'Gw8': 116,
                 'At8': 116, 'G8': 115, 'Fw8': 114, 'Gt8': 114, 'F8': 113, 'E8': 112, 'Dw8': 111, 'Et8': 111,
                 'D8': 110, 'Cw8': 109, 'Dt8': 109, 'C8': 108, 'B7': 107, 'Aw7': 106, 'Bt7': 106, 'A7': 105,
                 'Gw7': 104, 'At7': 104, 'G7': 103, 'Fw7': 102, 'Gt7': 102, 'F7': 101, 'E7': 100, 'Dw7': 99,
                 'Et7': 99, 'D7': 98, 'Cw7': 97, 'Dt7': 97, 'C7': 96, 'B6': 95, 'Aw6': 94, 'Bt6': 94, 'A6': 93,
                 'Gw6': 92, 'At6': 92, 'G6': 91, 'Fw6': 90, 'Gt6': 90, 'F6': 89, 'E6': 88, 'Dw6': 87, 'Et6': 87,
                 'D6': 86, 'Cw6': 85, 'Dt6': 85, 'C6': 84, 'B5': 83, 'Aw5': 82, 'Bt5': 82, 'A5': 81, 'Gw': 80,
                 'asâ€™â€™': 80, 'G5': 79, 'Fw5': 78, 'Gt5': 78, 'F5': 77, 'E5': 76, 'Dw5': 75, 'Et5': 75, 'D5': 74,
                 'Cw5': 73, 'Dt5': 73, 'C5': 72, 'B4': 71, 'Aw4': 70, 'Bt4': 70, 'A4': 69, 'Gw4': 68,
                 'At4': 68, 'G4': 67, 'Fw4': 66, 'Gt4': 66, 'F4': 65, 'E4': 64, 'Dw4': 63, 'Et4': 63, 'D4': 62,
                 'Cw4': 61, 'Dt4': 61, 'C4': 60, 'B3': 59, 'Aw3': 58, 'Bt3': 58, 'A3': 57, 'Gw3': 56,
                 'At3': 56, 'G3': 55, 'Fw3': 54, 'Gt3': 54, 'F3': 53, 'E3': 52, 'Dw3': 51, 'Et3': 51, 'D3': 50,
                 'Cw3': 49, 'Dt3': 49, 'C3': 48, 'B2': 47, 'Aw2': 46, 'Bt2': 46, 'A2': 45, 'Gw2': 44, 'At2': 44,
                 'G2': 43, 'Fw2': 42, 'Gt2': 42, 'F2': 41, 'E2': 40, 'Dw2': 39, 'Et2': 39, 'D2': 38, 'Cw2': 37,
                 'Dt2': 37, 'C2': 36, 'B1': 35, 'Aw1': 34, 'Bt1': 34, 'A1': 33, 'Gw1': 32, 'At1': 32, 'G1': 31,
                 'Fw1': 30, 'Gt1': 30, 'F1': 29, 'E1': 28, 'Dw1': 27, 'Et1': 27, 'D1': 26, 'Cw1': 25, 'Dt1': 25,
                 'C1': 24, 'B0': 23, 'Aw0': 22, 'Bt0': 22, 'A0': 21}




def create_midi(degrees: dict, song: list):
    mf = midiutil.MIDIFile()

    track    = 0   # Track numbers are zero-origined
    channel  = 0   # MIDI channel number
    pitch    = 60  # MIDI note number
    time2     = 0   # In beats
    duration = 1   # In beats
    volume   = 100 # 0-127, 127 being full volume
    start = 0
    mf.addTempo(0, 0, 120)
    for section in song:
        for chord in section[0]:
            mf.addNote(track, channel, degrees[chord], start, section[1], volume)
        start += section[1]

    with open("mymidifile2.midi", "wb") as output_file:
        mf.writeFile(output_file)

