__author__ = 'gabriel'

import requests
from horoscope import Horoscope
import datetime

class SignParser:

    def __init__(self):
        self.zodiacs = [(120, 'capricorn'), (218, 'aquarius'), (320, 'pisces'), (420, 'aries'), (521, 'taurus'),
           (621, 'gemini'), (722, 'cancer'), (823, 'leo'), (923, 'virgo'), (1023, 'libra'),
           (1122, 'scorpio'), (1222, 'sagittarius'), (1231, 'capricorn')]


    @staticmethod
    def isDob(str):
        if str[3] == '-' and str[6] == '-':
            return True

        return False

    @staticmethod
    def isValidDob(date_string):
        try:
            datetime.datetime.strptime(date_string, '%d-%m-%Y')
            return True
        except ValueError:
            return False

    def isSign(self,sign):
        for z in self.zodiacs:
            if sign == z[1]:
                return True

        return False

    #18-02-1988 - preferred date format
    def getSignFromDob(self,dob):
        ds = dob.split('-')
        date_number = ds[1]+ds[0]
        for z in self.zodiacs:
            if int(date_number) <= z[0]:
                return z[1]


    @staticmethod
    def weekHoroscope(sign):
        return dict(Horoscope.get_weekly_horoscope(sign))







