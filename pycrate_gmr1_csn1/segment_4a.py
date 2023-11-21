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
# * File Name : pycrate_gmr1_csn1/segment_4a.py
# * Created : 2023-10-24
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: ETSI TS 101 376-04-08
# section: 11.5.2.85         Segment A4
# top-level object: Segment 4A



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_bits = CSN1Bit(name='spare_bits', num=-1)
Spare_bits = spare_bits
Spare_Bits = spare_bits

header_segment_4a = CSN1List(name='header_segment_4a', list=[
  CSN1Val(name='class_type_4', val='110'),
  CSN1Val(name='segment_type', val='0000')])

repeated_utran_fdd_neighbour_cells_struct = CSN1List(name='repeated_utran_fdd_neighbour_cells_struct', list=[
  CSN1Bit(name='fdd_arfcn', bit=14),
  CSN1Bit(name='fdd_indic0'),
  CSN1Bit(name='nr_of_fdd_cells', bit=5),
  CSN1Bit(name='fdd_cell_information_field', bit=('# unprocessed: (p(NR_OF_FDD_CELLS))', lambda: 0))])

_3g_neighbour_cell_description = CSN1Alt(name='_3g_neighbour_cell_description', alt={
  '0': ('', []),
  '1': ('', [
  CSN1Bit(name='bandwidth_fdd', bit=3),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='repeated_utran_fdd_neighbour_cells', obj=repeated_utran_fdd_neighbour_cells_struct)]),
  CSN1Val(name='', val='0'),
  CSN1Ref(obj=spare_bits)])})

segment_4a = CSN1List(name='segment_4a', list=[
  CSN1Bit(name='radio_link_timeout', bit=8),
  CSN1Ref(obj=_3g_neighbour_cell_description),
  CSN1Ref(obj=spare_bits)])
