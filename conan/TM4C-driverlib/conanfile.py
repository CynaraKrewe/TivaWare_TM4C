from conans import ConanFile
from conans.tools import download, unzip
import os
import shutil

class Tm4cDriverlib(ConanFile):
	name="TM4C-driverlib"
	version="2.1.3.156"
	description="""
		TivaWare driver library from Texas Instruments.
		Nothing is changed from the original release by Texas Instruments.
		Only arm-none-eabi-gcc toolchain is supported.
		"""
	url="http://www.ti.com/tool/SW-TM4C"
	license="TI BSD"
	author="Mathias Spiessens"
	build_policy="missing"
	exports="*"

	def source(self):
		download("https://github.com/CynaraKrewe/TivaWare_TM4C/archive/v2.1.3.156.zip", "TivaWare_TM4C-2.1.3.156.zip")
		unzip("TivaWare_TM4C-2.1.3.156.zip")
		shutil.move("TivaWare_TM4C-2.1.3.156", "TivaWare_TM4C")
		os.unlink("TivaWare_TM4C-2.1.3.156.zip")

	def build(self):
		self.run("cd TivaWare_TM4C/driverlib; make")

	def package(self):
		self.copy("*.h", "include/tm4c/inc", "TivaWare_TM4C/inc")
		self.copy("*.h", "include/tm4c/driverlib", "TivaWare_TM4C/driverlib")
		self.copy("*.a", "library", "TivaWare_TM4C/driverlib/gcc")
