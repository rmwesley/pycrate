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
# * File Name : pycrate_gmr1_csn1/uplink_rlc_mac_control_message.py
# * Created : 2023-10-24
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: ETSI TS 101 376-04-12
# section: 11.2.0.2 Uplink RLC/MAC messages
# top-level object: Uplink RLC/MAC control message

# external references
from pycrate_gmr1_csn1.packet_link_quality_report_message_content import packet_link_quality_report_message_content
from pycrate_gmr1_csn1.packet_uplink_dummy_control_block_message_content import packet_uplink_dummy_control_block_message_content
from pycrate_gmr1_csn1.packet_resource_request_message_content import packet_resource_request_message_content
from pycrate_gmr1_csn1.packet_measurement_report_message_content import packet_measurement_report_message_content
from pycrate_gmr1_csn1.packet_link_quality_report_type2_message_content import packet_link_quality_report_type2_message_content
from pycrate_gmr1_csn1.packet_dch_downlink_ack_nack_message_content import packet_dch_downlink_ack_nack_message_content
from pycrate_gmr1_csn1.packet_uplink_talk_burst_control_message_content import packet_uplink_talk_burst_control_message_content
from pycrate_gmr1_csn1.packet_control_acknowledgement_message_content import packet_control_acknowledgement_message_content
from pycrate_gmr1_csn1.packet_mobile_tbf_status_message_content import packet_mobile_tbf_status_message_content
from pycrate_gmr1_csn1.packet_downlink_ack_nack_message_content import packet_downlink_ack_nack_message_content

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

uplink_rlc_mac_control_message = CSN1Alt(name='uplink_rlc_mac_control_message', alt={
  '000001': ('message_type', [
  CSN1Ref(obj=packet_control_acknowledgement_message_content)]),
  '000010': ('message_type', [
  CSN1Ref(obj=packet_downlink_ack_nack_message_content)]),
  '000011': ('message_type', [
  CSN1Ref(obj=packet_uplink_dummy_control_block_message_content)]),
  '000100': ('message_type', [
  CSN1Ref(obj=packet_link_quality_report_message_content)]),
  '000101': ('message_type', [
  CSN1Ref(obj=packet_resource_request_message_content)]),
  '000110': ('message_type', [
  CSN1Ref(obj=packet_mobile_tbf_status_message_content)]),
  '000111': ('message_type', [
  CSN1Ref(obj=packet_uplink_talk_burst_control_message_content)]),
  '001000': ('message_type', [
  CSN1Ref(obj=packet_link_quality_report_type2_message_content)]),
  '001010': ('message_type', [
  CSN1Ref(obj=packet_measurement_report_message_content)]),
  '001011': ('message_type', [
  CSN1Ref(obj=packet_downlink_ack_nack_message_content)]),
  '011111': ('message_type', [
  CSN1Ref(obj=packet_dch_downlink_ack_nack_message_content)])})
