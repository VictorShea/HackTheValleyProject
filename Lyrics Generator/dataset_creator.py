import lyricsgenius as generator


dataset = open("/Users/rahisharora/Desktop/htv/Lyrics Generator/songs.txt", "w")
glyrics = generator.Genius('Iil-cAuuai6ih-Dr_Ggyk_EODU4AiwgUrkWf0dCXaXDrgQXyxcG_TUDWK1wEfouL',
                           skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                           remove_section_headers=True)

singers = ['Ed Sheeran', 'Billie Eilish', 'Ariana Grande', 'Taylor Swift', 'Adele', 'Justin Bieber', 'Dua Lipa', 'Beyonce',
           'Lady Gaga', 'Bruno Mars', 'Celine Dion', 'Shawn Mendes', 'Rihanna', 'Charlie Puth', 'Sam Smith',
           'Miley Cyrus', 'Harry Styles', 'Alicia Keys', 'Selena Gomez', 'John Legend', 'Zayn Malik', 'Olivia Rodrigo',
           'Halsey', 'Jennifer Lopez', 'Katy Perry', 'Shakira', 'Demi Lovato']
i = 0
for name in singers:
    try:
        songs = (glyrics.search_artist(name, max_songs=10, sort='popularity')).songs
        s = [song.lyrics for song in songs]
        dataset.write("\n \n--SEPARATOR--\n \n".join(s))  # Deliminator
        i += 1
        print(f"Songs grabbed:{len(s)}")
    except:
        print(f"some exception at {name}: {i}")
