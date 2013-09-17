#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Zoonibot web api.

Run this script to start the development server.
"""
from flask import Flask, request, json
from astropy import log
import zoonibot

zoonibotapp = Flask('zoonibot', static_url_path='')

@zoonibotapp.route('/')
def root():
    return "Hello bro. I am Zoonibot. Keep calm and classify on."

@zoonibotapp.route('/area', methods=['GET'])
def area():
    ra = request.args.get('RA', default='', type=float)
    dec = request.args.get('DEC', default='', type=float)
    sr = request.args.get('SR', default='0.01', type=float)
    return zoonibot.area_response(ra, dec, sr)

if __name__ == "__main__":
    zoonibotapp.debug = True
    zoonibotapp.run(port=4242, host='0.0.0.0', processes=3)
