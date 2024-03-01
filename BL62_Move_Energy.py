""" Move BL62 mono to a given energy """

import math
import epics

""" Calculate a crystal angle at a given energy"""
def energy(mono):
	hc = 12398.4244
	dspacing = 3.1356
	fmono = float(mono)
	crystal_1 = epics.PV("BL62:DMC02:m1.VAL")
	if fmono >= 3000.0 and fmono <= 13000.0:
		m1 = 2*dspacing*fmono
		crystal = math.asin(hc/m1)
		angle_crystal=int((180.0*crystal/math.pi) * 1000)/1000.0
		print(str(fmono) + " eV" +" : " + str(angle_crystal))
		crystal_1.put(angle_crystal.value, wait=True)
		print(str(crystal_1.value))
	else:
		print("Energy is out of range")
energy(10000)

