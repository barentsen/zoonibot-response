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
    return """ZooniBot says: "Hello. I am ZooniBot."""

@zoonibotapp.route('/examples')
def examples():
    return zoonibotapp.send_static_file('examples.html')

@zoonibotapp.route('/gz_summary', methods=['GET'])
def gz():
    ra = request.args.get('RA', default='', type=float)
    dec = request.args.get('DEC', default='', type=float)
    sr = request.args.get('SR', default=0.01, type=float)
    return 'ZooniBot says: "'+zoonibot.galaxyzoo_response(ra, dec, sr)+'"'

@zoonibotapp.route('/ph_candidate', methods=['GET'])
def ph():
    ra = request.args.get('RA', default='', type=float)
    dec = request.args.get('DEC', default='', type=float)
    #sr = request.args.get('SR', default=0.01, type=float)
    return 'ZooniBot says: "'+zoonibot.planethunters_response(ra, dec)+'"'

if __name__ == "__main__":
    zoonibotapp.debug = True
    zoonibotapp.run(port=4242, host='0.0.0.0', processes=3)
