# Garage-band

[Link to Latest PR]()

## Description
- Use Python classes to model a Band made up of different kinds of musicians.

- Start with Guitarist,Bassist, and Drummer.

- Make use of a Musician base class to handle common functionality which particular kinds of musicians will inherit.


## User Acceptance Tests

### Band Tests

- A Band instance should have a name attribute which is a string.
- A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
- A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
- A Band instance should have appropriate __str__ and __repr__ methods.
- A Band should have a class method to_list which returns a list of previously created Band instances

### Musician Subclass Tests

- Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
- Each kind of Musician instance should have a get_instrument method that returns string.
- Each kind of Musician instance should have a play_solo method that returns string.

### Stretch
- A Band should have a static method create_from_data which takes a collection of formatted data and returns a created Band instance.
    - The Band instance should have its members be set to musicians based on info from the input.
    - The formatted data should be in a file
    - The exact formatting is up to you.


## Usage

Start by creating some musicians:
```
musician4 = Guitarist('guitar', 'Sweet child of mine')
musician5 = Drummer('Drum', 'November Rain')
musician6 = Bassist('Bass', 'Paradise City')
```

Then you can create a Band, passing the band name as a string and the musicians as a list:
```
guns_n_roses= Band('Guns n Roses', [musician4, musician5, musician6])
```

Then do this to see the solos of each Musician:

```
guns_n_roses.play_solos()
```

returns:
Sweet child of mine
November Rain
Paradise City

## Challenges

It was very difficult to understand the requirenments for this lab. I was not sure how to start or what the end result should look like. With Roger's and Merry's help, I was able to create Musicians and create a Band wth them.


## References

- https://www.youtube.com/watch?v=ZDa-Z5JzLYM


## Lab04 - Classes and Fixtures

[Canvas Assignment](https://canvas.instructure.com/courses/2045906/assignments/15160027)

## Author

[Chuck Li Villalobos](https://github.com/ticochuck)