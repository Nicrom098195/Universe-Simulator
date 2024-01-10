import json

with open("settings.json", "r") as f:
    st=json.load(f)

fname=st["rf"]

data={
    "sun": {
        "col": (255, 255, 0),
        "rad": 20,
        "grav": 30,
        "pos": [800, 450],
        "vel": [0, 0],
        "type": 2,
        "temp":5500
    },
    "earth": {
        "col": (100, 100, 255),
        "rad": 5,
        "grav": 1,
        "pos": [1100, 450],
        "vel": [0, -8],
        "type": 0,
        "temp":0
    },
    "venus": {
        "col": (255, 50, 50),
        "rad": 5,
        "grav": 0.9,
        "pos": [1000, 450],
        "vel": [0, -6],
        "type": 0,
        "temp":0
    },
    "mars": {
        "col": (255, 0, 0),
        "rad": 3,
        "grav": 0.4,
        "pos": [1200, 450],
        "vel": [0, -10],
        "type": 0,
        "temp":0
    },
    "jupiter": {
        "col": (255, 150, 150),
        "rad": 12,
        "grav": 2.4,
        "pos": [300, 450],
        "vel": [0, 12],
        "type": 1,
        "temp":0
    },
    "saturn": {
        "col": (255, 150, 150),
        "rad": 10,
        "grav": 2.1,
        "pos": [200, 450],
        "vel": [0, 15],
        "type": 1,
        "temp":0
    },
    "neptune": {
        "col": (0, 0, 200),
        "rad": 5,
        "grav": 1.3,
        "pos": [120, 450],
        "vel": [0, 20],
        "type": 1,
        "temp":0
    },
    "uranus": {
        "col": (0, 0, 240),
        "rad": 5,
        "grav": 1.2,
        "pos": [70, 450],
        "vel": [0, 25],
        "type": 1,
        "temp":0
    },
    "pluto": {
        "col": (255, 150, 150),
        "rad": 1,
        "grav": 0.2,
        "pos": [10, 450],
        "vel": [0, 30],
        "type": 0,
        "temp":0
    }
}

with open(fname, "w") as f:
    f.write(json.dumps(data))