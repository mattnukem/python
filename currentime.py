import datetime
import time
from pyowm.owm import OWM
import unicornhathd
import characters3x5

owm = OWM('API KEY GOES HERE')
mgr = owm.weather_manager()
lastupdate = -1

unicornhathd.brightness(0.6)
unicornhathd.rotation(180)

while True:
    unicornhathd.clear()
    thetimeis = datetime.datetime.now()

    hours = thetimeis.strftime("%H")
    hourscolor = 'light red'
    hourysoffset = 1

    minutes = thetimeis.strftime("%M")
    minutescolor = 'cyan'
    minutesyoffset = 9

    tempyoffset = 5

    if lastupdate != int(minutes):
        lastupdate = int(minutes)
        weather = mgr.weather_at_id(4744870).weather
        temp_dict_fahrenheit = weather.temperature('fahrenheit')
        currenttemp = str(int(round(temp_dict_fahrenheit['temp'])))
        print('Updating temperature at ' + minutes + ' minutes. Temperature is ' +
            str(temp_dict_fahrenheit['temp']))

    for i in hours:
        for eachhour in characters3x5.ledlistmaker(i, hourscolor, 0, hourysoffset):
            unicornhathd.set_pixel(eachhour[0], eachhour[1], eachhour[2], eachhour[3], eachhour[4])
        hourysoffset += 4

    for j in minutes:
        for eachminute in characters3x5.ledlistmaker(j, minutescolor, 0, minutesyoffset):
            unicornhathd.set_pixel(eachminute[0], eachminute[1], eachminute[2], eachminute[3], eachminute[4])
        minutesyoffset += 4

    for t in currenttemp:
        for eachdigit in characters3x5.ledlistmaker(t, 'white', 9, tempyoffset):
            unicornhathd.set_pixel(eachdigit[0], eachdigit[1], eachdigit[2], eachdigit[3], eachdigit[4])
        tempyoffset += 4

    unicornhathd.show()
    time.sleep(0.1)
