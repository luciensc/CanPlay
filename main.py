import numpy as np

# WHISTLES
tin_whistle_D = ["D", "E", "F#", "G", "A", "B", "C", "C#"]

# AUX FUNCTIONS
SCALE = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B",  # sharp
         "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]  # flat


def note_to_numeric(note, transpose=0):
    # transforming notes to numeric allows easy transposing
    # and is a unique melody representation instead of synonymous sharp/flat notes
    return (SCALE.index(note) + transpose) % 12  # allows entering both sharp and flat notation indiscriminately


def numeric_to_note(num, flat=False):
    pos = num
    if flat:
        pos += 12
    return SCALE[pos]

def transpose(melody, delta=0):
    num_melo = [note_to_numeric(note, transpose=delta) for note in melody]
    return [numeric_to_note(num) for num in num_melo]

def melody_playable(melody, whistle, transp_melo=0, verbose=True):
    whistle_num = [note_to_numeric(note) for note in whistle]
    melody_num = [note_to_numeric(note, transpose=transp_melo) for note in melody]

    unplayable = []
    for num in melody_num:
        if not (num in whistle_num):
            unplayable.append(numeric_to_note(num))

    if len(unplayable) > 0:
        if verbose:
            print(f"cannot play {len(unplayable)} notes:\n{unplayable}")
        return False, unplayable
    else:
        return True, unplayable


def transpose_to_playable(melody, whistle):
    for i in range(12):
        print(f"TRANPOSE BY {i} SEMITONE")
        playable, unplayable_ls = melody_playable(melody, whistle, transp_melo=i, verbose=False)
        if playable:
            print("CAN BE PLAYED!")
            print(transpose(melody, delta=i))
        else:
            print(f"cannot be played. following notes are missing: {np.unique(unplayable_ls)}")
        print("-------------\n")


if __name__ == "__main__":
    in_melody = ["C", "C#", "Db", "A#", "Bb"]
    # ["F", "C", "Eb", "C#", "C", "Bb", "G", "Ab"]

    # # transform input melody to numeric (unique mapping, transposable)
    # num_melody = [note_to_numeric(note) for note in in_melody]
    # print(num_melody)

    # # check if a melody is playable on a particular whistle
    # melody_playable(melody=in_melody, whistle=tin_whistle_D)

    transpose_to_playable(melody=in_melody, whistle=tin_whistle_D)

