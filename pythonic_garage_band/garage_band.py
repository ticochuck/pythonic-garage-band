class Musician:
    """
    Super class Musician

    Arguments: 

    """
    def __init__(self, instrument, solo):
        self.instrument = instrument
        self.solo = solo
    
    def __repr__(self):
        return {'Instrument':{self.instrument}, 'Solo':{self.solo}}

    def __str__(self):
        return f'Instrument(Instrumenr={self.instrument} Solo={self.solo})'

    def instruments(self, instrument):
        self.instrument =  instrument
        return self.instrument

    def play_solo(self, solo):
        self.solo = solo
        return self.solo

class Band(Musician):
    """
    [summary]

    Args:
        Musician ([type]): [description]
    """

    def __init__(self, name, members):
        self.name = name
        self.members = members
        
    def __repr__(self):
        return {'name':{self.name}, 'members':{self.members}}

    def __str__(self):
        return f'Band(name={self.name} members={self.members}'
    
    def play_solos(self):
        for member in self.members:
            member.play_solo()

class Guitarist(Musician):
    def __repr__(self):
        return {'Instrument':{self.instrument}, 'Solo':{self.solo}, }

    def __str__(self):
        return f'Guitarist(Instrument={self.instrument} Solo={self.solo}'

    def play_solo(self):
        print(self.solo)
        return self.solo

    def get_instrument(self):
        return self.instrument

class Bassist(Musician):  
    def __repr__(self):
            return {'Instrument':{self.instrument}, 'Solo':{self.solo}, }

    def __str__(self):
        return f'Guitarist(Instrument={self.instrument} Solo={self.solo}'
    
    def play_solo(self):
        print(self.solo)
        return self.solo

    def get_instrument(self, instrument):
        return self.instrument

class Drummer(Musician):
    def __repr__(self):
        return {'Instrument':{self.instrument}, 'Solo':{self.solo}, }

    def __str__(self):
        return f'Guitarist(Instrument={self.instrument} Solo={self.solo}'

    def play_solo(self):
        print(self.solo)
        return self.solo
    
    def get_instrument(self, instrument):
        self.instrument = 'drumms'
        return self.instrument


musician1 = Guitarist('guitar', 'we are the champions')
musician2 = Drummer('Drum', 'YES')
musician3 = Bassist('Bass', 'NO')
queen = Band('Queen', [musician1, musician2, musician3])
queen.play_solos()

musician1 = Guitarist('guitar', 'sweet child of mine')
musician2 = Drummer('Drum', 'November Rain')
musician3 = Bassist('Bass', 'YES and No')
guns_n_roses= Band('Guns n Roses', [musician1, musician2, musician3])
guns_n_roses.play_solos()
