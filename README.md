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

## Important

With both of the 2 first methods shown before, for all the time that's possible will be centered the last star or black hole created. If it collides with another body, it could be eliminated and not be centered anymore, showing the X0 Y0 coordinates at the center.
With the third method the center will automatically be X0 Y0, if you want to center your favorite celestial body, in all the three methods you can modify the **center** element in the file *settings.json*, by just putting in the name of the boty that you prefer.

Special thanks to Gpopcorn for the original project [AccurateSpaceSimulator](https://github.com/Gpopcorn/AccurateSpaceSimulator)

## settings.json info

There are so much settings on this simulator, so I decided to make an entire part of the README just for this:

- **rf**: is just the name of the file that contains all the info about the universe that you are running
- **mtemps**: The maximum temperatures that can be reached from the different types of celestial bodies
- **btypes**: The names of the different celestial bodies based on the table shown before
- **center**: The name of the body that's kept at the center of the screen
- **kmperpx**: The entire simulator is based on pixel distances, but for calculating temperatures and the data shown on the top-left of the screen, we need km, so this value is multiplied for the number of pixel to get an accurate value
- **title**: Just the title of the window
- **winSize**: The size of the window
- **showAnything**: Shows every celestial body on the screen. This can be a bit useless in most cases, but if you want to see all the simulation in one time in may be helpful.
