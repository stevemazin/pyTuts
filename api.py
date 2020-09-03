import json
import requests
import turtle


def move_iss(lat, long):
    global iss
    iss.penup()
    iss.goto(long, lat)
    iss.pendown()


# create a screen instance
screen = turtle.Screen()
screen.setup(1000, 500)
screen.bgpic('earth.gif')
screen.setworldcoordinates(-180, -90, 180, 90)

iss = turtle.Turtle()
turtle.register_shape("iss.gif")
iss.shape("iss.gif")

url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url)

if response.status_code == 200:
    response_dictionary = json.loads(response.text)
    # print(response.text)
    position = response_dictionary['iss_position']
    print('International Space Station at ' + position['latitude'] + ', ' + position['longitude'])

    lat = float(position['latitude'])
    long = float(position['longitude'])
    move_iss(lat, long)
else:
    print("Houston, we have a problem:", response.status_code)

turtle.mainloop()
