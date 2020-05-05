#Tsewang Stanzin
import numpy as np
import matplotlib
import astroplan
from astropy import units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord
from astropy.coordinates import EarthLocation
from astroplan import Observer, FixedTarget
from astropy.utils import iers
from astropy.coordinates import get_sun, get_moon, get_body
from astroplan import moon_illumination
import matplotlib.pyplot as plt
from astroplan.plots import plot_sky, plot_airmass

import socket
from ctypes._aix import get_version
import serial
### StellaCam routines
class StellaCam:

    def __init__(self, ser_port):
        self.ser_port = ser_port
        self.video_rates = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.ser_open()

    def ser_open(self):
        # Serail(port_name,baudrate,databits,parity,stopbit,time_out)
        self.port = serial.Serial(self.ser_port, 9600, 8, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout=3)

    # send a command off to the StellaCam
    def command(self, string):
        self.port.write(string.encode())

    # send command to get the stellacam's firmware version.
    # used this to kick a misbehaving stellacam into shape.
    def get_version(self):
        self.command("?V")
        result = self.port.read(6)
        print(result)
        return result

    def part_pack(self, num):
        if (num >= 0):
            num = num & 255
        else:
            num = 256 - (abs(num) & 255)
        return num

    # configure stella_cam
    def configure(self, gain, frame, gamma, iris):
        if (gain < 1 or gain > 127):
            gain = 127

        if (frame >= 0 and frame < 10):
            rate = self.video_rates[frame]
        else:
            rate = 10

        if (gamma < 0 or gamma > 2):
            gamma = 2

        if (iris < 0 or iris > 1):
            iris = 0
        # put the commands into the appropriate bytes using bitwise operators
        data1 = 1 + (gain << 1)
        data2 = 1 + (gamma << 2) + (rate << 4)
        control = 1 + (0 << 1) + (0 << 2) + (1 << 3) + (iris << 4) + (0 << 5) + (0 << 6) + (0 << 7)
        # print control
        data1 = self.part_pack(data1)
        data2 = self.part_pack(data2)
        control = self.part_pack(control)
        command_str = "SC2" + "S%(dt1)c%(dt2)c%(ctl)c" % {'dt1': data1, 'dt2': data2, 'ctl': control}  # .pack("CCC")
        self.command(command_str)
        out = self.port.read(7)
        self.dtr(0)
        self.rts(0)
        # puts "config = #{out}"

    # Have not tested this function. Mostly you need to change this function before using it
    def signals(self):
        self.port.signals

    def rts(self, flag):
        self.port.setRTS(flag)

    def dtr(self, flag):
        self.port.setDTR(flag)

    # Have not tested this function. Mostly you need to change this function before using it because this function is using
    def dec2bin(self, num):
        array = [num]
        str = array.pack("N").unpack("B32")
        return str[0]

    def close(self):
        self.dtr(0)
        self.rts(0)
        self.port.close
        self.port = nil

class Automation:
    def iers(self):
        astroplan.get_IERS_A_or_workaround()
        iers.conf.auto_download = False
        iers.conf.auto_max_age = None
        now = Time.now()

        longitude = '78d57m53s'
        latitude = '32d46m44s'
        elevation = 4500 * u.m
        location = EarthLocation.from_geodetic(longitude, latitude, elevation)
        iaohanle = Observer(location=location, timezone='Asia/Kolkata',name="IAO", description="IAO Hanle telescopes")
        iaohanle
        # Calculating the sunset, midnight and sunrise times for our observatory
        sunset_iao = iaohanle.sun_set_time(now, which='nearest')
        eve_twil_iao = iaohanle.twilight_evening_astronomical(now, which='nearest')
        midnight_iao = iaohanle.midnight(now, which='next')
        morn_twil_iao = iaohanle.twilight_morning_astronomical(now, which='next')
        sunrise_iao = iaohanle.sun_rise_time(now, which='next')

        moon_rise = iaohanle.moon_rise_time(now)
        moon_set = iaohanle.moon_set_time(now)
        moon_alt = iaohanle.moon_altaz(now).alt
        moon_az = iaohanle.moon_altaz(now).az
        print("Current Time (Please note all time should be in UTC)   ",now)
        print("Sunset at IAO will be at {0.iso} UTC  ".format(sunset_iao))
        print("Astronomical evening twilight at IAO will be at {0.iso} UTC  ".format(eve_twil_iao))
        #print("Midnight at IAO will be at {0.iso} UTC   ".format(midnight_iao))
        print("Astronomical morning twilight at IAO will be at {0.iso} UTC  ".format(morn_twil_iao))
        print("Sunrise at IAO will be at {0.iso} UTC   ".format(sunrise_iao))

        print("Moon's Illumination Strength Tonight  ", moon_illumination(midnight_iao))
        print("Moon Rise at IAO will be at {0.iso} UTC   ".format(moon_rise))
        print("Moon Set at IAO will be at {0.iso} UTC  ".format(moon_set))

        observing_time = (morn_twil_iao - eve_twil_iao).to(u.h)
        print("Total Night hours at IAO tonight  {0:.1f}  ".format(observing_time))
        flag=0
        if(morn_twil_iao==now):
            print("Changing the parameters for morning twilight")
        elif(eve_twil_iao<=now):
            print("Changing the parameters for Evening twilight")
        elif(sunset_iao<=now):
            flag=1
            print("Sunsssssssssssssssseeeeeeeeeeeeeeeet ,,, changeeeeeeeeee", flag)
        else:
            print("Keeping the current parameters")


#stella=StellaCam('/dev/ttyUSB0')
#stella.get_version()
auto=Automation()
auto.iers()

#print("Sunset", sunset_iao)

gain_set=int(30)
frame_set = int(0)
gamma_set = int(0)
iris_set=int(1)
#stella.configure(gain_set,frame_set,gamma_set,iris_set)
