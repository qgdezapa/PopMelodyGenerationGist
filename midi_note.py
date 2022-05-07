class MIDINote:

    def __init__(self, note, duration_type, length):
        self.note = note
        self.duration_type = duration_type
        self.length = length
        self.as_map = {
            "note": note,
            "duration_type": duration_type,
            "length": length
        }

    def __repr__(self):
        return "{note: {}. duration_type: {}, length: {}}".format(self.note, self.duration_type, self.length)

    def __str__(self):
        return "{note: {}. duration_type: {}, length: {}}".format(self.note, self.duration_type, self.length)
