#!/usr/bin/env python

import logging
log = logging.getLogger(__name__)

logging.getLogger().level = logging.DEBUG

import serial

from django.contrib.auth.models import User
from django.conf import settings
from profile.models import UserProfile

TTY = settings.DOOR_UNLOCKER_DEVICE

def check_rfid(rfid):
  results = UserProfile.objects.filter(rfid=rfid)[:1]
  return None if len(results) < 1 else results[0].user

with serial.Serial(TTY, 9600) as device:
  last_data = None
  while True:

    line = device.readline()
    data = [int(x[-2:], 16) for x in line.split()]
    if len(data) == 0:
      continue

    # Strip AA, BB and checksum
    data = data[1:-2]

    if data == last_data:
      continue
    last_data = data

    if data[1] == 6 and data[3] == 0:
      card = data[4:8]
      card = ''.join([format(x, '02x') for x in card]).upper()

      user = check_rfid(card)
      if user:
        log.info('User {0} opened the door'.format(user.username))
        device.write('D')
        device.flush()
      else:
        log.debug('RFID {0} not recognised'.format(card))




 
