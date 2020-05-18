# Check for IERS timings, talk to camera serially.

import numpy as np
import matplotlib
import astroplan
from astropy import units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord
from astropy.coordinates import EarthLocation
from astroplan import Observer, FixedTarget
from astropy.utils import iers
from astroplan.utils import IERS_A_in_cache
from astropy.coordinates import get_sun, get_moon, get_body
from astroplan import moon_illumination
import matplotlib.pyplot as plt
from astroplan.plots import plot_sky, plot_airmass
import socket
# from ctypes._aix import get_version
import serial
from PIL import Image, ImageDraw, ImageFont

# from astropy import log
# log.disable_warnings_logging()
# log.setLevel('CRITICAL')
### StellaCam routines
# from plan import moon_rise


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

        rate = frame
        # put the commands into the appropriate bytes using bitwise operators
        data1 = 1 + (gain << 1)
        data2 = 1 + (gamma << 2) + (rate << 4)
        control = 1 + (0 << 1) + (0 << 2) + (1 << 3) + (iris << 4) + (0 << 5) + (0 << 6) + (0 << 7)
        data1 = self.part_pack(data1)
        data2 = self.part_pack(data2)
        control = self.part_pack(control)
        command_str = "SC2" + "S%(dt1)c%(dt2)c%(ctl)c" % {'dt1': data1, 'dt2': data2, 'ctl': control}  # .pack("CCC")
        self.command(command_str)
        out = self.port.read(7)
        self.dtr(0)
        self.rts(0)
        # puts "config = #{out}"

    def signals(self):
        self.port.signals

    def rts(self, flag):
        self.port.setRTS(flag)

    def dtr(self, flag):
        self.port.setDTR(flag)

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
    eve_twilight_flag = 0
    mor_twilight_flag = 0
    moon_setting_flag = 0
    moon_strength = 0

    def eop(self):

        IERS_A_in_cache()
        # astroplan.get_IERS_A_or_workaround()
        iers.conf.auto_download = False
        iers.conf.auto_max_age = None
        now = Time.now()

        longitude = '78d57m53s'
        latitude = '32d46m44s'
        elevation = 4500 * u.m
        location = EarthLocation.from_geodetic(longitude, latitude, elevation)
        iaohanle = Observer(location=location, timezone='Asia/Kolkata', name="IAO", description="IAO Hanle telescopes")
        iaohanle
        # Calculating the sunset, midnight and sunrise times for our observatory
        sunset_iao = iaohanle.sun_set_time(now, which='nearest')
        eve_twil_iao = iaohanle.twilight_evening_astronomical(now, which='nearest')
        midnight_iao = iaohanle.midnight(now, which='next')
        morn_twil_iao = iaohanle.twilight_morning_astronomical(now, which='next')
        sunrise_iao = iaohanle.sun_rise_time(now, which='next')
        moon_rise = iaohanle.moon_rise_time(eve_twil_iao, which='nearest')
        moon_set = iaohanle.moon_set_time(now ,which='nearest')
        # moon_alt = iaohanle.moon_altaz(now).alt
        # moon_az = iaohanle.moon_altaz(now).az
        #lst_now = iaohanle.local_sidereal_time(now)
        #lst_mid = iaohanle.local_sidereal_time(midnight_iao)
        #print("LST at IAO now is {0:.2f}".format(lst_now))
        #print("LST at IAO at local midnight will be {0:.2f}".format(lst_mid))

        Automation.moon_strength = moon_illumination(midnight_iao)

        observing_time = (morn_twil_iao - eve_twil_iao).to(u.h)
        #print("Total Night hours at IAO tonight  {0:.1f}  ".format(observing_time))

        img = Image.new('RGB', (850, 320), color=(0, 0, 0))
        fnt = ImageFont.truetype('/var/lib/defoma/gs.d/dirs/fonts/DejaVuSerif.ttf', 15)
        d = ImageDraw.Draw(img)
        d.text((10, 11), "IAO Hanle Coordinates:   " + str(iaohanle), font=fnt, fill=(255, 255, 255))

        d.text((10, 71), "Moon Illumination Strength          : " + str(moon_illumination(midnight_iao)), font=fnt,
               fill=(255, 255, 255))
        d.text((10, 101),
               "Sunset                                       : " + Time(sunset_iao, out_subfmt='date_hms').iso + " UTC",
               font=fnt, fill=(255, 255, 255))
        d.text((10, 131), "Astronomical evening twilight : " + Time(eve_twil_iao, out_subfmt='date_hms').iso + " UTC",
               font=fnt, fill=(255, 255, 255))
        d.text((10, 161), "Astronomical morning twilight : " + Time(morn_twil_iao, out_subfmt='date_hms').iso + " UTC",
               font=fnt, fill=(255, 255, 255))
        d.text((10, 191),
               "Sunrise                                   : " + Time(sunrise_iao, out_subfmt='date_hms').iso + " UTC",
               font=fnt, fill=(255, 255, 255))
        d.text((10, 221), "Moon Rise                    : " + Time(moon_rise, out_subfmt='date_hms').iso + " UTC", font=fnt, fill=(255, 255, 255))

        d.text((10, 251), "Moon Set                    : " + Time(moon_set, out_subfmt='date_hms').iso + " UTC", font=fnt, fill=(255, 255, 255))
        d.text((10, 281), "Total Astronomical hours tonight                    : " + str(observing_time) ,
               font=fnt, fill=(255, 255, 255))
        img.save('tonight.png')
        img.close()

        t_start = eve_twil_iao
        t_end = morn_twil_iao

        # We can turn solar system objects into 'pseudo-fixed' targets to plan observations
        mercury_midnight = FixedTarget(name='Mercury', coord=get_body('mercury', midnight_iao))
        mercury_midnight.coord
        venus_midnight = FixedTarget(name='Venus', coord=get_body('venus', midnight_iao))
        venus_midnight.coord

        uranus_midnight = FixedTarget(name='Uranus', coord=get_body('uranus', midnight_iao))
        uranus_midnight.coord
        neptune_midnight = FixedTarget(name='Neptune', coord=get_body('neptune', midnight_iao))
        neptune_midnight.coord

        saturn_midnight = FixedTarget(name='Saturn', coord=get_body('saturn', midnight_iao))
        saturn_midnight.coord

        jupiter_midnight = FixedTarget(name='Jupiter', coord=get_body('jupiter', midnight_iao))
        jupiter_midnight.coord

        mars_midnight = FixedTarget(name='Mars', coord=get_body('mars', midnight_iao))
        mars_midnight.coord

        targets = [mercury_midnight, venus_midnight, mars_midnight, jupiter_midnight, saturn_midnight, uranus_midnight,
                   neptune_midnight]
        targets

        #for target in targets:
            #print(iaohanle.target_rise_time(now, target, which='next', horizon=10 * u.deg).iso)

        # iaohanle.altaz(now, targets[0])

        # print(iaohanle.target_rise_time(now, target, which='next', horizon=10 * u.deg).iso)

        # iaohanle.altaz(now, targets[0])

        times = (t_start - 0.5 * u.h) + (t_end - t_start + 1 * u.h) * np.linspace(0.0, 1.0, 20)
        for target in targets:
            plot_sky(target, iaohanle, times)
        plt.legend(loc=[1.0, 0])
        plt.xlabel('Planets motion tonight')

        # plt.ylim(4,0.5)
        # plt.legend()
        plt.savefig('planets_motion.png')
        plt.close()

        # plt.legend(loc=[1.1,0])

        coords1 = SkyCoord('15h58m3s', '-18d10m0.0s', frame='icrs')  # coordinates of Andromeda Galaxy (M32)
        tt1 = FixedTarget(name='Moon', coord=coords1)

        tt1.coord
        t_observe = t_start + (t_end - t_start) * np.linspace(0.0, 1.0, 20)
        plot_sky(tt1, iaohanle, t_observe)
        plt.xlabel('Moon motion tonight')
        plt.savefig('moon_motion.png')
        plt.close()

        if (eve_twil_iao <= now):
            Automation.eve_twilight_flag = 1
            Automation.mor_twilight_flag = 0
            Automation.moon_setting_flag = 0
        elif (morn_twil_iao <= now):
            Automation.eve_twilight_flag = 0
            Automation.mor_twilight_flag = 1
            Automation.moon_setting_flag = 0
        elif (Automation.moon_strength > 0.30):
            if (moon_rise <= now):
                Automation.eve_twilight_flag = 0
                Automation.mor_twilight_flag = 0
                Automation.moon_setting_flag = 1
            elif (moon_set <= now):
                Automation.eve_twilight_flag = 1
                Automation.mor_twilight_flag = 0
                Automation.moon_setting_flag = 0


auto = Automation()
auto.eop()
stella = StellaCam('/dev/ttyS0')
stella.get_version()
stella.configure(int(0), int(0), int(0), int(1))
if (auto.eve_twilight_flag == 1):
    print("Changing to night parameter")
    stella.get_version()
    stella.configure(int(70), int(7), int(0), int(1))
elif (auto.mor_twilight_flag == 1):
    print("Changing to day parameter")
    stella.get_version()
    stella.configure(int(1), int(0), int(0), int(1))
elif (auto.moon_setting_flag == 1):
    print("Moon Stregth:   ", auto.moon_strength)
    print("Changing to mooon parameter")
    stella.get_version()
    stella.configure(int(60), int(5), int(0), int(1))

