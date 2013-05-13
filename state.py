#!/usr/bin/env python
# -*- coding: utf-8 -*-

# state.py
# This file is part of tango-ds (http://sourceforge.net/projects/tango-ds/)
#
# tango-ds is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# tango-ds is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with tango-ds.  If not, see <http://www.gnu.org/licenses/>.

'''Contains mostly StateLogic and global constants shared between device server
   for Danfysik-9100 power supplies.
'''

import PowerSupply.standard as PS

DanfysikStatusDict = [('MAIN POWER',                 ['Off', 'On']),
                      ('POLARITY NORMAL',            ['Yes', 'No']),
                      ('POLARITY REVERSED',          ['Yes', 'No']),
                      ('NOT USED',                   ['', '']),
                      ('CROWBAR',                    ['On', 'Off']),
                      ('I-MODE',                     ['I-mode', 'V-mode']),
                      ('UNIT',                       ['%', 'Amps and Volts']),
                      ('EXTERNAL INTERLOCK 0',       ['Interlock', 'No Interlock']),
                      ('NOT USED',                   ['', '']),
                      ('SUM - INTERLOCK',            ['Sum Interlock', 'No Interlock']),
                      ('OVER VOLTAGE (OVP)',         ['Over Voltage', 'No Over Voltage']),
                      ('DC OVER CURRENT (OCP)',      ['Over Current', 'No Over Current']),
                      ('DC UNDERVOLTTAGE',           ['Fault', 'Ok']),
                      ('NOT USED',                   ['', '']),
                      ('PHASE FAILURE (AC LINE OK)', ['Fault', 'Ok']),
                      ('NOT USED',                   ['', '']),
                      ('EARTH LEAKAGE',              ['Fault', 'Ok']),
                      ('FAN',                        ['Fault', 'Ok']),
                      ('MPS OVER TEMPERATURE',       ['Fault', 'Ok']),
                      ('EXTERNAL INTERLOCK 1',       ['Interlock', 'No Interlock']),
                      ('EXTERNAL INTERLOCK 2',       ['Interlock', 'No Interlock']),
                      ('EXTERNAL INTERLOCK 3',       ['Interlock', 'No Interlock']),
                      ('MPS NOT READY',              ['Not Ready', 'Ready']),
                      ('NOT USED',                   ['', ''])
                     ]

#class IocasteStateLogic(PS.StateLogic):
#    def __init__(self, device, key):
#        PS.StateLogic.__init__(self, device)
        
