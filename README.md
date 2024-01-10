# Universe Simulator
A small python simulator of the universe


Ever wondered what the Universe would look like under certain conditions? This is the program that you were searching for!
I'm glad to present you **Universe Simulator**, a customizable universe-simulation experience!

Download and run the code, just make sure to have at least pygame 2.5.2 installed by typing `pip install pygame==2.5.2` in your terminal.

## You can do 3 things:

### 1. Run the default solar system

![Solar system](https://github.com/Nicrom098195/Universe-Simulator/blob/main/Images/1.png)

by just running in your terminal:

`python writer.py`
`python main.py`

This will automatically show you the solar system, always putting the center of the screen.

### 2. Generate a random universe

![Solar system](https://github.com/Nicrom098195/Universe-Simulator/blob/main/Images/2.png)

by running `python generator.py` in your terminal, and putting in how many planets, stars and black holes you would like to have (You cannot put more than 40 planets, 20 stars and 30 black holes for better rendering. If you don't agree, feel free to modify the code)

Then run `python main.py` to see the simulation

### 3. Write a custom universe

You can also write your dream universe, you just have to play with the **system.json** file!

You need to write every planet, star or black hole like this:

```
"name": {
        "col": (255, 150, 150),
        "rad": 1,
        "grav": 1,
        "pos": [10, 450],
        "vel": [0, 30],
        "type": 0,
        "temp":0
    }
```

Where: 
- Name is the name of the celestial body
- **col** is the color of the body in an RGB value
- **rad** is the radius of the body in pixels
- **grav** is the gravity of the body, 1 is one time the earth's gravity
- **pos** is the position of the celestial body on the screen, in pixels, starting from the top-left corner
- **vel** is the velocity of the celestial body, the first one is the X velocity and the second one is the Y velocity
- **type** is the type of body, as shown on the table below
- **temp** is the temperature of the body. This will stay the same all the time for stars and black holes, and change for planets based on the nearest star

| Type | Number |
| :---: | :---: |
| Solid planet | 0 |
| Gas planet | 1 |
| Small star | 2 |
| Red giant | 3 |
| Black hole | 4 |

Special thanks to Gpopcorn for the original project [AccurateSpaceSimulator](https://github.com/Gpopcorn/AccurateSpaceSimulator)
