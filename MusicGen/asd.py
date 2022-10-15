import json
from sound import convert_sound

asdd = "nsC4s0p25 nsE4s0p25 nsA4s0p25 nsC4s0p25 nsE4s0p25 nsA4s0p25 nsC5s0p25 nsE4s0p25 nsA4s0p25 nsC5s0p25 nsE5s0p25 nsA4s0p25 nsC5s0p25 nsE5s0p25 nsA5s0p25 nsC5s0p25 nsE5s0p25 nsA5s0p25 nsC6s0p25 nsE5s0p25 nsA5s0p25 nsC6s0p25 cs2sA5sE6s0p25 nsC6s0p25 nsE6s0p25 nsA5s0p25 nsC6s0p25 cs3sE6sG5sC6s0p25 nsC5s0p25 nsE5s0p25 nsA5s0p25 nsE5s0p25 nsA5s0p25 nsE5s0p25 nsC5s0p25 nsE5s0p25 nsA5s0p25 nsE5s0p25 nsC5s0p25 nsA4s0p25 nsE4s0p25 nsGw4s0p25 nsB3s0p25 nsB4s0p25 nsE5s0p25 nsGw4s0p25 nsE5s0p25 nsA5s0p25 nsE5s0p25 nsGw4s0p25"
dic = json.load(open("vocab.json"))
asdd = asdd.split(" ")
dic_key = list(dic.keys())
lst = []
for val in asdd:
    print(val)
    d = convert_sound(val)
    if len(d[0]) != 0:
        lst.append(d)

print(lst)
node = {'G9': 127, 'Fw9': 126, 'Gt9': 126, 'F9': 125, 'E9': 124, 'Dw9': 123,
        'Et9': 123, 'D9': 122,
        'Cw9': 121, 'Dt9': 121, 'C9': 120, 'B8': 119, 'Aw8': 118, 'Bt8': 118,
        'A8': 117, 'Gw8': 116,
        'At8': 116, 'G8': 115, 'Fw8': 114, 'Gt8': 114, 'F8': 113, 'E8': 112,
        'Dw8': 111, 'Et8': 111,
        'D8': 110, 'Cw8': 109, 'Dt8': 109, 'C8': 108, 'B7': 107, 'Aw7': 106,
        'Bt7': 106, 'A7': 105,
        'Gw7': 104, 'At7': 104, 'G7': 103, 'Fw7': 102, 'Gt7': 102, 'F7': 101,
        'E7': 100, 'Dw7': 99,
        'Et7': 99, 'D7': 98, 'Cw7': 97, 'Dt7': 97, 'C7': 96, 'B6': 95,
        'Aw6': 94, 'Bt6': 94, 'A6': 93,
        'Gw6': 92, 'At6': 92, 'G6': 91, 'Fw6': 90, 'Gt6': 90, 'F6': 89,
        'E6': 88, 'Dw6': 87, 'Et6': 87,
        'D6': 86, 'Cw6': 85, 'Dt6': 85, 'C6': 84, 'B5': 83, 'Aw5': 82,
        'Bt5': 82, 'A5': 81, 'Gw5': 80,
        'At5': 80, 'G5': 79, 'Fw5': 78, 'Gt5': 78, 'F5': 77, 'E5': 76,
        'Dw5': 75, 'Et5': 75, 'D5': 74,
        'Cw5': 73, 'Dt5': 73, 'C5': 72, 'B4': 71, 'Aw4': 70, 'Bt4': 70,
        'A4': 69, 'Gw4': 68,
        'At4': 68, 'G4': 67, 'Fw4': 66, 'Gt4': 66, 'F4': 65, 'E4': 64,
        'Dw4': 63, 'Et4': 63, 'D4': 62,
        'Cw4': 61, 'Dt4': 61, 'C4': 60, 'B3': 59, 'Aw3': 58, 'Bt3': 58,
        'A3': 57, 'Gw3': 56,
        'At3': 56, 'G3': 55, 'Fw3': 54, 'Gt3': 54, 'F3': 53, 'E3': 52,
        'Dw3': 51, 'Et3': 51, 'D3': 50,
        'Cw3': 49, 'Dt3': 49, 'C3': 48, 'B2': 47, 'Aw2': 46, 'Bt2': 46,
        'A2': 45, 'Gw2': 44, 'At2': 44,
        'G2': 43, 'Fw2': 42, 'Gt2': 42, 'F2': 41, 'E2': 40, 'Dw2': 39,
        'Et2': 39, 'D2': 38, 'Cw2': 37,
        'Dt2': 37, 'C2': 36, 'B1': 35, 'Aw1': 34, 'Bt1': 34, 'A1': 33,
        'Gw1': 32, 'At1': 32, 'G1': 31,
        'Fw1': 30, 'Gt1': 30, 'F1': 29, 'E1': 28, 'Dw1': 27, 'Et1': 27,
        'D1': 26, 'Cw1': 25, 'Dt1': 25,
        'C1': 24, 'B0': 23, 'Aw0': 22, 'Bt0': 22, 'A0': 21}
print(lst)
import midiutil
from IPython.display import Audio
from pretty_midi import PrettyMIDI
from midi2audio import FluidSynth
import time

mf = midiutil.MIDIFile()

track = 0  # Track numbers are zero-origined
channel = 0  # MIDI channel number
time2 = 0  # In beats
volume = 100  # 0-127, 127 being full volume
modifier = 12
mf.addTempo(0, 0, 240 * modifier)

time2 = 0
for nodes in lst:
    beats = nodes[1] * modifier
    print(beats)
    for nod in nodes[0]:
        mf.addNote(track, channel, node[nod], int(time2), int(beats), volume)
    time2 += beats

with open("mymidifile.midi", 'wb') as output_file:
    mf.writeFile(output_file)
