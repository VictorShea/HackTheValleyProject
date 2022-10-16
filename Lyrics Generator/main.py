#Creates a random set of lyrics

from lyrics_generator import generator
import texttosinging

words = generator()
print(words)
x = texttosinging.create_mp3(words)
texttosinging.change_pitch(x)
texttosinging.add_audios(x)

