# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.4
# *
# * Copyright 2018. Benoit Michau. P1sec.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_gmr1_csn1/link_quality_report_ie.py
# * Created : 2023-10-24
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: ETSI TS 101 376-04-12
# section: 12.30 Link quality report
# top-level object: Link Quality Report IE



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

link_quality_report_ie = CSN1List(name='link_quality_report_ie', list=[
  CSN1Bit(name='sqir', bit=6),
  CSN1Bit(name='gmprs_terminal_type_identifier', bit=7),
  CSN1Bit(name='sin', bit=4),
  CSN1Bit(name='pan', bit=6),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='imei', bit=64)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gps_position', bit=40)])})])
