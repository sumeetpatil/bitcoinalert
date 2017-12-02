#!/bin/python
# -*- coding: utf-8 -*-
"""
Alert on bitcoin price Put this script in cron job
and earn some coins for you :)
"""
import os
import json
import requests

PRICEDIFF = 20000
TMPFILE = "tmpbuy"


def write_data(data):
    """Write data to a file """
    _file = open(TMPFILE, "w+")
    _file.write(str(data))
    _file.close()


def read_data():
    """Read data from file"""
    if not os.path.isfile(TMPFILE):
        write_data("0")
    _file = open(TMPFILE, "r")
    return _file.read()


def sendmessage(message):
    """
    Send Message
    :param message: alert message
    """
    if message != "":
        print(message)
        # make a sms api call or rest call to alert


def bitcoin_alert():
    """Bitcoin alert"""
    request = requests.get(
        "https://www.zebapi.com/api/v1/market/ticker/btc/inr"
    )
    data = json.loads(request.content.decode('utf-8'))
    newprice = data["buy"]
    oldprice = read_data()
    oldprice = float(oldprice)
    message = ""
    if oldprice - newprice > PRICEDIFF:
        message = "London bridge is falling down! :D. Current price is  {0}INR\
                and Old Price is {1}INR. {2}INR Diff Set\
                ".format(newprice, oldprice, PRICEDIFF)
        oldprice = newprice

    if newprice - oldprice > PRICEDIFF:
        message = "Boom Boom!!. Current price is {0}INR and Old Price is \
{1}INR. {2}INR Diff Set".format(newprice, oldprice, PRICEDIFF)
        oldprice = newprice

    write_data(newprice)
    sendmessage(message)


bitcoin_alert()
