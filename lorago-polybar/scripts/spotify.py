import dbus
from datetime import datetime

try:
    max_length = 30
    speed_multiplier = 5

    session_bus = dbus.SessionBus()
    spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
                                         "/org/mpris/MediaPlayer2")

    spotify_properties = dbus.Interface(spotify_bus,
                                        "org.freedesktop.DBus.Properties")

    metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")

    song = metadata["xesam:title"]
    artist = metadata["xesam:artist"]

    artist_string = ""

    for part in artist:
        artist_string += str(part)

    text = artist_string + " - " + song

    length = len(text)

    time = length

    current_time = int((datetime.now().time().second + datetime.now().time().microsecond / 1000000) * speed_multiplier)

    move = current_time % (time - max_length + 1)

    move_comparison = current_time % ((time - max_length + 1) * 2)

    if move - move_comparison != 0:
        move = time - max_length - move

    if length > max_length:
        text = text[move:max_length+move:]

    # To list all key-value-pairs:
    #for key, value in metadata.items():
    #    print("(" + str(key) + " - " + str(value) + ")")

    status = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "PlaybackStatus")

    icon = ""
    if status == "Playing":
        icon = ""

    print(icon + " " + text)
except:
    print()
