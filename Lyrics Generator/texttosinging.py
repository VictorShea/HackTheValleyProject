def create_mp3(lyrics: str):
    from gtts import gTTS
    broken = lyrics.split()
    for i, item in enumerate(broken):
        singing = gTTS(text= item, lang= 'en', slow=False)
        singing.save(f"singing{i}.mp3")
    return len(broken)


def change_pitch(broken: int):
    from pydub import AudioSegment
    import random
    for i in range(4, broken):
        piece = AudioSegment.from_file(f"singing{i}.mp3", format="mp3")
        change = random.uniform(-0.1, 0.2)
        change_in_speed = int(piece.frame_rate * (2.0 ** change))
        new_sound = piece._spawn(piece.raw_data, overrides={'frame_rate': change_in_speed})
        new_sound.export(f"final{i}.mp3", format="mp3")


def add_audios(broken: int):
    from pydub import AudioSegment
    voice = AudioSegment.from_mp3("final4.mp3")
    for i in range(4, broken):
        voice += AudioSegment.from_mp3(f"final{i}.mp3")
    voice.export("voice.mp3", format="mp3")


def mp3_to_wav():
    from pydub import AudioSegment

    edit = AudioSegment.from_mp3("voice.mp3")
    edit.export("voice.wav", format="wav")


def remove_silence():
    from pydub.silence import split_on_silence
    from pydub import AudioSegment, effects
    from scipy.io.wavfile import read, write
    import numpy as np

    timer, sound = read("voice.wav")
    result = AudioSegment(sound.tobytes(), frame_rate=timer, sample_width=sound.dtype.itemsize, channels=1)
    pieces = split_on_silence(result, min_silence_len=10, silence_thresh=-100, keep_silence=10,)
    final = sum(pieces)
    final = np.array(final.get_array_of_samples())

