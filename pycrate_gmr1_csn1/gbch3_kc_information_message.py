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
# * File Name : pycrate_gmr1_csn1/gbch3_kc_information_message.py
# * Created : 2023-10-24
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: ETSI TS 101 376-04-12
# section: 10.1.46b GBCH3 Keplerian Coordinate information
# top-level object: GBCH3 KC Information Message



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

gbch3_kc_information_type_1 = CSN1List(name='gbch3_kc_information_type_1', list=[
  CSN1Bit(name='message_version_number', bit=3),
  CSN1Bit(name='wn', bit=10),
  CSN1Bit(name='tow', bit=40),
  CSN1Bit(name='frame_number', bit=19),
  CSN1Bit(name='number_of_sv', bit=5),
  CSN1Bit(name='iode_sv1', bit=8),
  CSN1Bit(name='iode_sv2', bit=8),
  CSN1Bit(name='iode_sv3', bit=8),
  CSN1Bit(name='iode_sv4', bit=8),
  CSN1Bit(name='iode_sv5', bit=8),
  CSN1Bit(name='iode_sv6', bit=8),
  CSN1Bit(name='iode_sv7', bit=8),
  CSN1Bit(name='iode_sv8', bit=8),
  CSN1Bit(name='iode_sv9', bit=8),
  CSN1Bit(name='iode_sv10', bit=8),
  CSN1Bit(name='iode_sv11', bit=8),
  CSN1Bit(name='iode_sv12', bit=8),
  CSN1Bit(name='iodcmsb_sv1'),
  CSN1Bit(name='iodcmsb_sv2'),
  CSN1Bit(name='iodcmsb_sv3'),
  CSN1Bit(name='iodcmsb_sv4'),
  CSN1Bit(name='iodcmsb_sv5'),
  CSN1Bit(name='iodcmsb_sv6'),
  CSN1Bit(name='iodcmsb_sv7'),
  CSN1Bit(name='iodcmsb_sv8'),
  CSN1Bit(name='iodcmsb_sv9'),
  CSN1Bit(name='iodcmsb_sv10'),
  CSN1Bit(name='iodcmsb_sv11'),
  CSN1Bit(name='iodcmsb_sv12'),
  CSN1Bit(name='spare', bit=3)])

gbch3_kc_information_type_2 = CSN1List(name='gbch3_kc_information_type_2', list=[
  CSN1Bit(name='message_version_number', bit=3),
  CSN1Bit(name='sv_number_1', bit=6),
  CSN1Bit(name='sv_number_2', bit=6),
  CSN1Bit(name='tgd_sv_1', bit=8),
  CSN1Bit(name='toc_sv_1', bit=16),
  CSN1Bit(name='af2_sv_1', bit=8),
  CSN1Bit(name='af1_sv_1', bit=16),
  CSN1Bit(name='af0_sv_1', bit=22),
  CSN1Bit(name='tgd_sv_2', bit=8),
  CSN1Bit(name='toc_sv_2', bit=16),
  CSN1Bit(name='af2_sv_2', bit=8),
  CSN1Bit(name='af1_sv_2', bit=16),
  CSN1Bit(name='af0_sv_2', bit=22),
  CSN1Bit(name='idot_sv_1', bit=14),
  CSN1Bit(name='idot_sv_2', bit=14),
  CSN1Bit(name='spare', bit=5)])

gbch3_kc_information_type_3 = CSN1List(name='gbch3_kc_information_type_3', list=[
  CSN1Bit(name='message_version_number', bit=3),
  CSN1Bit(name='sv_number_1', bit=6),
  CSN1Bit(name='crs', bit=16),
  CSN1Bit(name='lambda_n', bit=16),
  CSN1Bit(name='m0', bit=32),
  CSN1Bit(name='cuc', bit=16),
  CSN1Bit(name='e', bit=32),
  CSN1Bit(name='cus', bit=16),
  CSN1Bit(name='axis_12', bit=32),
  CSN1Bit(name='toe', bit=16),
  CSN1Bit(name='alert_flag'),
  CSN1Bit(name='anti_spoof_flag'),
  CSN1Bit(name='spare')])

gbch3_kc_information_type_4 = CSN1List(name='gbch3_kc_information_type_4', list=[
  CSN1Bit(name='message_version_number', bit=3),
  CSN1Bit(name='sv_number_1', bit=6),
  CSN1Bit(name='cic', bit=16),
  CSN1Bit(name='omega0', bit=32),
  CSN1Bit(name='cis', bit=16),
  CSN1Bit(name='i0', bit=32),
  CSN1Bit(name='crc', bit=16),
  CSN1Bit(name='w', bit=32),
  CSN1Bit(name='omega_dot', bit=24),
  CSN1Bit(name='sv_health', bit=6),
  CSN1Bit(name='fit'),
  CSN1Bit(name='urai', bit=4)])

gbch3_kc_information_type_5 = CSN1List(name='gbch3_kc_information_type_5', list=[
  CSN1Bit(name='message_version_number', bit=3),
  CSN1Bit(name='sv_number_2', bit=6),
  CSN1Bit(name='crs', bit=16),
  CSN1Bit(name='lambda_n', bit=16),
  CSN1Bit(name='m0', bit=32),
  CSN1Bit(name='cuc', bit=16),
  CSN1Bit(name='e', bit=32),
  CSN1Bit(name='cus', bit=16),
  CSN1Bit(name='axis_12', bit=32),
  CSN1Bit(name='toe', bit=16),
  CSN1Bit(name='alert_flag'),
  CSN1Bit(name='anti_spoof_flag'),
  CSN1Bit(name='spare')])

gbch3_kc_information_type_6 = CSN1List(name='gbch3_kc_information_type_6', list=[
  CSN1Bit(name='message_version_number', bit=3),
  CSN1Bit(name='sv_number_2', bit=6),
  CSN1Bit(name='cic', bit=16),
  CSN1Bit(name='omega0', bit=32),
  CSN1Bit(name='cis', bit=16),
  CSN1Bit(name='i0', bit=32),
  CSN1Bit(name='crc', bit=16),
  CSN1Bit(name='w', bit=32),
  CSN1Bit(name='omega_dot', bit=24),
  CSN1Bit(name='sv_health', bit=6),
  CSN1Bit(name='fit'),
  CSN1Bit(name='urai', bit=4)])

gbch3_kc_information_message = CSN1Alt(name='gbch3_kc_information_message', alt={
  '1000': ('', []),
  '1001': ('', [
  CSN1Ref(obj=gbch3_kc_information_type_1)]),
  '1010': ('', [
  CSN1Ref(obj=gbch3_kc_information_type_2)]),
  '1011': ('', [
  CSN1Ref(obj=gbch3_kc_information_type_3)]),
  '1100': ('', [
  CSN1Ref(obj=gbch3_kc_information_type_4)]),
  '1101': ('', [
  CSN1Ref(obj=gbch3_kc_information_type_5)]),
  '1110': ('', [
  CSN1Ref(obj=gbch3_kc_information_type_6)])})
