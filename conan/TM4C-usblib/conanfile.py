from conans import ConanFile
from conans.tools import download, unzip
import os
import shutil

class Tm4cUsblib(ConanFile):
	name="TM4C-usblib"
	version="2.1.3.156a"
	description="""
		TivaWare usb library from Texas Instruments.
		Nothing is changed from the original release by Texas Instruments.
		Only arm-none-eabi-gcc toolchain is supported.
		"""
	url="http://www.ti.com/tool/SW-TM4C"
	license="TI BSD"
	author="Mathias Spiessens"
	build_policy="missing"
	requires = "TM4C-driverlib/2.1.3.156a@spiessensm/stable"

	def source(self):
		download("https://github.com/CynaraKrewe/TivaWare_TM4C/archive/v2.1.3.156a.zip", "TivaWare_TM4C-2.1.3.156a.zip")
		unzip("TivaWare_TM4C-2.1.3.156a.zip")
		shutil.move("TivaWare_TM4C-2.1.3.156a", "TivaWare_TM4C")
		os.unlink("TivaWare_TM4C-2.1.3.156a.zip")

	def build(self):
		self.run("cd TivaWare_TM4C/usblib; make")

	def package(self):
		self.copy("*.h", "include/tm4c/usblib", "TivaWare_TM4C/usblib")
		self.copy("*.a", "library", "TivaWare_TM4C/usblib/gcc")
