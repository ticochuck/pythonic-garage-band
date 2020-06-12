class Musician:
    """
    Super class Musician

    Arguments: Instrument, Solo

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
    This is the Band sub-Class. A Band is made up of Guitarists, Bassists, Drummers.

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


musician1 = Guitarist('guitar', 'We are the champions')
musician2 = Drummer('Drum', 'Somebody to love')
musician3 = Bassist('Bass', 'We will rock you')
queen = Band('Queen', [musician1, musician2, musician3])
queen.play_solos()


musician4 = Guitarist('guitar', 'Sweet child of mine')
musician5 = Drummer('Drum', 'November Rain')
musician6 = Bassist('Bass', 'Paradise City')
guns_n_roses= Band('Guns n Roses', [musician4, musician5, musician6])
guns_n_roses.play_solos()

