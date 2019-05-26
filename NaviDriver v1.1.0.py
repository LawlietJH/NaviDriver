
# Python 3
# NavyDriver
# v1.1.0

#=======================================================================

#Hide Console
def Hide(xD=True):
	
	import win32console,win32gui
	window = win32console.GetConsoleWindow()
	
	if xD == True:
		win32gui.ShowWindow(window,0)
		return True
	elif xD == False:
		win32gui.ShowWindow(window,1)
		return False

Hide()

#=======================================================================

# Dependencias:
from selenium import webdriver		# pip install selenium
from pygame import mixer			# pip install pygame
from bs4 import BeautifulSoup		# pip install beautifoulsoup4
from PIL import Image, ImageTk		# pip install pillow
from PIL import ImageGrab			# pip install pillow
import tkinter as tk
import pywintypes
import threading
import keyboard						# pip install keyboard
import base64
import random
import struct
import ctypes
import time
import json
import sys
import os
import re

# Manipulacion de DLLs de Windows ======================================

from ctypes import windll

# pip install pywin32 ==================================================
from win32com.shell import shell
import win32api			as WA
import win32con			as WC
import win32gui			as WG
import win32ui			as WU
import win32net			as WN
import win32com			as WCM
import win32process		as WP
import win32security	as WS
import win32clipboard	as WCB
import win32console		as WCS
#=======================================================================

#~ cifrado    = base64.urlsafe_b64encode(document.encode())
#~ descifrado = base64.urlsafe_b64decode(document).decode()

run_command = lambda Comando: os.popen(Comando).read()

def isProcessActive(proceso):
	
	lista_procesos = run_command('wmic process get name').split('\n')
	
	for proc in lista_procesos:
		
		proc = proc.strip().split(' ')[0]
		
		if len(proc) == 0: continue
		
		if proc.endswith('.exe'):
			if proc.lower() == proceso.lower():
				return True
	
	return False


#=======================================================================
#=======================================================================
#=======================================================================

class Navi():
	
	def __init__(self):
		self.hiddencmd = True
		# Musica de Fondo:
		self._carga = 'sound/Memz Guitar.wav'
		self._click = [
			'sound/Clic3.wav',
			'sound/Clic14.wav',
			'sound/Clic15.wav',
			'sound/Kwahmah-Click.wav',
			'sound/Level Up.wav',
			'sound/Success.wav',
			'sound/Victoria.wav'
		]
		self._songs = [
			'sound/Errinerung - Debussy.wav',
			'sound/Memz Pretty Pluck Sound.wav',
			'sound/Setuniman - Little Pleasures.wav',
			'sound/Tim-Kahn - Cedellia.wav',
			'sound/Tim-Kahn - Sigj.wav'
		]
		
		mixer.init()
		
		# Inicio:
		self.root = tk.Tk()
		self.menu = tk.Menu(self.root, tearoff=0)
		
		self.img1 = 'img/NaviDriver.png'
		self.img2 = 'img/Cargando.gif'
		self.img3 = 'img/Vaciando.gif'
		self.img4 = 'img/Cerrando.gif'
		self.img2size = (204,40)
		self.img3size = (204,72)
		self.img4size = (204,40)
		self.img2f = 4
		self.img3f = 4
		self.img4f = 4
		
		self.X = 0
		self.Y = 0
		self.size = (220, 210)
		self.centerXY()
		
		self.song = mixer.Sound(self._carga)
		self.song.play()
		self.contsong = 0
		self.contclick1 = 0
		self.contclick2 = 1
		self.click1 = mixer.Sound(self._click[0])
		self.click2 = mixer.Sound(self._click[1])
	
	
	def centerXY(self):
		
		self.X_Pos = int(self.root.winfo_screenwidth()/2 - self.size[0]/2)
		self.Y_Pos = int(self.root.winfo_screenheight()/2 - self.size[1]/2)
	
	def comandos(self, event):
		if self.hiddencmd:
			self.hiddencmd = False
		else:
			self.hiddencmd = True 
		self.playclick1()
		#~ with open('id', 'r') as File:
			#~ datos = File.read()
			#~ print([datos])
			#~ time.sleep(3)
		Hide(self.hiddencmd)
	
	def cerrar(self, event='Clic Derecho'):
		global endapp
		self.playclick1()
		print(event)
		endapp = True
		self.centrar()
		#~ sys.exit()
	
	def popup(self, event):
		self.playclick2()
		self.menu.post(event.x_root, event.y_root)
	
	def minimizar(self, event):
		self.root.overrideredirect(False)
		#~ self.root.wm_state('iconic')
		self.root.iconify()
	
	def cancelarshutdown(self, event=''):
		printText('Se Cancelo el Cierre de Sesion', 3)
		run_command('shutdown -a')
	
	def motion(self, event):
		print(event.x_root, event.y_root)
	
	def centrar(self, event=''):
		if event != '':
			self.playclick1()
		self.centerXY()
		self.root.update_idletasks()
		w = self.root.winfo_screenwidth()
		h = self.root.winfo_screenheight()
		x = w/2 - self.size[0]/2
		y = h/2 - self.size[1]/2
		self.root.geometry('{}x{}+{}+{}'.format(self.size[0], self.size[1], int(x), int(y)))
	
	def movewithB1(self, event):
		
		tmpX, tmpY = event.x, event.y
		dX, dY = tmpX - self.X, tmpY - self.Y
		self.X_Pos += dX
		self.Y_Pos += dY
		self.root.geometry('{}x{}+{}+{}'.format(self.size[0], self.size[1], self.X_Pos, self.Y_Pos))
		#~ print('{}, {}'.format(self.X_Pos, self.Y_Pos))
	
	def showB1click(self, event):
		self.X, self.Y = event.x, event.y
		#~ print(self.X, self.Y, '<-- Clic 1')
	
	def showB1release(self, event):
		self.playclick1()
		limit = 60
		if self.X_Pos < -(self.size[0]-limit) or self.X_Pos > self.root.winfo_screenwidth()-limit:
			self.centrar()
			self.centerXY()
		if self.Y_Pos < -(self.size[1]-limit) or self.Y_Pos > self.root.winfo_screenheight()-limit:
			self.centrar()
			self.centerXY()
		#~ print('Se solto')
	
	
	def minimizado(self, event): self.root.overrideredirect(False)
	
	def normalizado(self, event): self.root.overrideredirect(True)
	
	
	def GIF(self, img, size, t, disable=False):
		vImg = tk.Toplevel(self.root)
		vImg.overrideredirect(True)
		vImg.lift()
		self.root.wm_attributes('-disabled', True)
		vImg.wm_attributes('-disabled', True)
		vImg.wm_attributes('-topmost', True)
		vImg.wm_attributes('-transparentcolor', 'white')
		label = AnimatedGif(vImg, img, 0.3)
		label.pack()
		label.start_thread()
		vImg.geometry('{}x{}+{}+{}'.format(
			size[0], size[1],
			int(vImg.winfo_screenwidth()/2 - size[0]/2),
			int(vImg.winfo_screenheight()/2 - size[1]/2)
		))
		vImg.after(t*1000, lambda: vImg.destroy())
		self.root.after(t*1000, lambda: self.root.wm_attributes('-disabled', False))
	
	
	def playsong(self, song):
		self.contsong = self._songs.index(song)
		self.song = mixer.Sound(song)
		self.song.play()
	
	def playclick1(self): self.click1.play()
	
	def playclick2(self): self.click2.play()
	
	def nextsong(self, event):
		self.playclick1()
		self.contsong += 1
		self.contsong = self.contsong % len(self._songs)
		self.song.stop()
		self.song = mixer.Sound(self._songs[self.contsong])
		self.song.play()
	
	def nextclick1(self, event):
		self.contclick1 += 1
		self.contclick1 = self.contclick1 % len(self._click)
		if self.contclick1 == self.contclick2: self.contclick1 += 1
		self.click1 = mixer.Sound(self._click[self.contclick1])
		self.playclick1()
	
	def nextclick2(self, event):
		self.contclick2 += 1
		self.contclick2 = self.contclick2 % len(self._click)
		if self.contclick2 == self.contclick1: self.contclick2 += 1
		self.click2 = mixer.Sound(self._click[self.contclick2])
		self.playclick2()
	
	
	def runNavi(self):
		self.root.wm_title('Navi Driver')
		#~ self.root.resizable(False, False)
		#~ self.root.iconbitmap('/img/Navi.ico')
		
		# Eventos del Mouse:
		self.root.bind('<ButtonRelease-1>', self.showB1release)
		self.root.bind('<B1-Motion>', self.movewithB1)
		self.root.bind('<Button-1>', self.showB1click)
		self.root.bind('<Double-1>', self.minimizar)
		self.root.bind('<Button-3>', self.popup)
		self.root.bind('<Unmap>', self.minimizado)	# Reacciona con el Click al minimizar.
		self.root.bind('<Map>', self.normalizado)	# Reacciona con el Click al normalizar.
		#~ self.root.bind('<Motion>', self.motion)
		
		# Eventos del Teclado:
		self.root.bind('<Escape>', self.cerrar)
		self.root.bind('<C>', self.centrar)
		self.root.bind('<Q>', self.cerrar)
		self.root.bind('<M>', self.minimizado)
		self.root.bind('<N>', self.nextsong)
		self.root.bind('<S>', self.cancelarshutdown)
		self.root.bind('<c>', self.centrar)
		self.root.bind('<q>', self.cerrar)
		self.root.bind('<m>', self.minimizado)
		self.root.bind('<n>', self.nextsong)
		self.root.bind('<s>', self.cancelarshutdown)
		#~ self.root.bind('<s>', self.showCMD)
		
		
		# Menu PopUp:
		menu1 = tk.Menu(self.menu, tearoff=0)
		menu1.add_command(label='Minimizar', command=lambda:self.minimizar(self))
		menu1.add_command(label='Centrar', command=lambda:self.centrar(self))
		menu2 = tk.Menu(self.menu, tearoff=0)
		menu2.add_command(label='Next Song', command=lambda:self.nextsong(self))
		menu2.add_command(label='Next Click Izq', command=lambda:self.nextclick1(self))
		menu2.add_command(label='Next Click Der', command=lambda:self.nextclick2(self))
		
		self.menu.focus()
		self.menu.add_cascade(label='Acciones', menu=menu1)
		self.menu.add_cascade(label='Sonidos', menu=menu2)
		self.menu.add_separator()
		self.menu.add_command(label='Comandos', command=lambda:self.comandos(self))
		self.menu.add_separator()
		self.menu.add_command(label='Cancelar Apagado/Reinicio', command=lambda:self.cancelarshutdown(self))
		self.menu.add_separator()
		self.menu.add_command(label='Cerrar', command=lambda:self.cerrar(self))
		
		
		# Icono:
		#~ self.root.wm_iconphoto(True, tk.PhotoImage(file=self.name))
		
		# Imagen Navi Driver:
		self.root.image = tk.PhotoImage(file=self.img1)
		self.label = tk.Label(self.root, image=self.root.image, bg='white')
		self.root.overrideredirect(True)
		#~ self.root.geometry('{}x{}+{}+{}'.format(self.size[0], self.size[1], self.X_Pos, self.Y_Pos))
		self.root.lift()
		#~ self.root.wm_attributes('-disabled', True)
		self.root.wm_attributes('-topmost', True)
		self.root.wm_attributes('-transparentcolor', 'white')
		self.label.pack()
		
		# Gif:
		self.GIF(img=self.img2, size=self.img2size, t=10)
		
		# Reproduce la cancion principal:
		self.root.after(10000, lambda: self.playsong(random.choice(self._songs)))
		
		self.label.mainloop()
	
	#######

class Driver():
	
	def __init__(self):
		
		self.display_tipo = -1
		self.display_origin_settings = self.getDisplaySettings()
		self.display_settings = self.getDisplaySettings()
		self.display1_orientation = 0	# Default
		self.display2_orientation = 0	# Default
		self.volcont = 0
	
	# Funcion Principal ================================================
	
	def execute(self, cmd):
		cmd = cmd.lower()
		t_act = 5
		# Acciones de Sistema Activo: ==================================
		if 'volumen' in cmd:
			cmd = cmd.split()
			if len(cmd) == 2:
				try:
					vol = int(cmd[1])
					if vol > 100: vol = 100
					elif vol < 0: vol = 0
					self.volcont += 1
					if self.volcont <= 4: self.setVolume(vol)
					elif self.volcont == 5: self.setVolume(100)
					printText('Volumen al: {:>3}%'.format(vol), 2)
					time.sleep(2)
				except ValueError:
					pass
		elif 'cambiar resolucion' in cmd:
			self.display_settings[0] = 800
			self.display_settings[1] = 600
			self.setDisplaySettings(*self.display_settings)
			time.sleep(10)
			self.setDisplaySettings(*self.display_origin_settings)
			time.sleep(t_act)
		elif 'cambiar pantalla' in cmd:
			cmd = cmd.split()
			if len(cmd) == 3:
				try:
					tipo = int(cmd[2])-1
					if tipo >= 0 and tipo <= 3:
						printText('Cambiando A:', t_act)
						if tipo == self.display_tipo:
							printText('Sin Cambios',  t_act, 1)
							time.sleep(t_act)
						else:
							if   tipo == 0: printText('Solo Primer Pantalla',  t_act, 1)
							elif tipo == 1: printText('Solo Segunda Pantalla', t_act, 1)
							elif tipo == 2: printText('Pantalla Duplicada',    t_act, 1)
							elif tipo == 3: printText('Pantalla Extendida',    t_act, 1)
							self.displaySwitch(tipo)
							time.sleep(t_act)
						self.display_tipo = tipo
				except ValueError:
					pass
		elif cmd == 'vaciar papelera':
			try:
				items = self.getNumItemsInRecyclerBin()
				taman = self.getTotalSizeInRecyclerBin()
				taman2 = self.getTotalSizeInRecyclerBin(True)
				print('\n Items:', items)
				print('\n Tam:', taman)
				print('\n Tam2:', taman2)
				if items > 0:
					navi.centrar()
					navi.GIF(img=navi.img3, size=navi.img3size, t=3)
					#~ self.cleanRecyclerBin()
					self.cleanRecyclerBin(tipo=3)
				time.sleep(3)
			except self.ErrorVaciarPapelera:
				pass
		elif cmd == 'screenshot abierto':
			self.screenshot(True)
			time.sleep(t_act)
		elif cmd == 'screenshot':
			self.screenshot()
			time.sleep(t_act)
		elif cmd == 'abrir notepad':
			self.startApp('notepad.exe')
		elif cmd == 'girar pantalla 1':
			self.setDisplayRotation(0)
		elif cmd == 'girar pantalla 2':
			self.setDisplayRotation(1)
		elif cmd == 'expulsar disco':
			printText('Expulsando Disco', t_act, 2)
			self.ejectCDROM()
		elif cmd == 'minimizar todo': 
			self.minimizeAll()
		
		#===============================================================
		# Informacion de PC: ===========================================
		elif cmd == 'ver ram total':
			printText('RAM Total: ', t_act)
			printText(str(self.getTotalRAM()), t_act, 1)
			print(self.getTotalRAM())
			time.sleep(t_act)
		elif cmd == 'ver ram disponible':
			printText('RAM Disponible: ', t_act)
			printText(str(self.getAvailableRAM()), t_act, 1)
			print(self.getAvailableRAM())
			time.sleep(t_act)
		elif cmd == 'ver tiempo activo':
			printText('Tiempo Activo: ', t_act)
			printText(str(self.getTimeActiveSystem()), t_act, 1)
			print(self.getTimeActiveSystem())
			time.sleep(t_act)
		elif cmd == 'ver nombre pc':
			printText('Nombre PC: ', t_act)
			printText(str(self.getComputerName()), t_act, 1)
			print(self.getComputerName())
			time.sleep(t_act)
		elif cmd == 'ver nucleos':
			printText('Cantidad de Nucleos: ', t_act)
			printText(str(self.getNumberOfProcessors()), t_act, 2)
			print(self.getNumberOfProcessors())
			time.sleep(t_act)
		elif cmd == 'ver monitores':
			printText('Cantidad de Monitores: ', t_act)
			printText(str(self.getNumberOfMonitors()), t_act, 2)
			print(self.getNumberOfMonitors())
			time.sleep(t_act)
		elif cmd == 'ver gama':
			gama = 'Alta' if self.isSlowMachine() == 0 else 'Baja'
			printText('Tipo de Gama: '+gama, t_act)
			#~ printText(gama, t_act, 1)
			time.sleep(t_act)
		elif cmd == 'ver resolucion':
			printText('Resolucion de Pantalla:', t_act)
			xScreen = self.getDisplaySettings()[0]
			yScreen = self.getDisplaySettings()[1]
			printText('X: '+str(xScreen), t_act, 2)
			printText('Y: '+str(yScreen), t_act, 3)
			print(xScreen, yScreen)
			time.sleep(t_act)
		elif cmd == 'ver clave':
			printText('Clave de Producto:', t_act)
			clave = self.getWindowsProductKey(True)
			printText(clave, t_act, 2)
			print(clave)
			time.sleep(t_act)
		
		#===============================================================
		# Acciones de Sesion de Usuario: ===============================
		elif cmd == 'bloquear sesion':
			self.lockWorkStation()
			time.sleep(10)
		elif cmd == 'cerrar sesion':
			for seg in range(11):
				printText(str(10-seg), 2, 2)
				time.sleep(.5)
			time.sleep(2)
			self.exitWindows('logoff')
		elif cmd == 'reiniciar':
			printText('Reiniciando en 10 segundos', 10)
			run_command('shutdown -r -t 15')
			for seg in range(11):
				printText(str(10-seg), 2, 2)
				time.sleep(.5)
			time.sleep(2)
			#~ self.exitWindows('reboot')
		elif cmd == 'apagar':
			printText('Apagando en 10 segundos', 10)
			run_command('shutdown -s -t 15')
			for seg in range(11):
				printText(str(10-seg), 2, 2)
				time.sleep(.5)
			time.sleep(2)
			#~ self.exitWindows('shutdown')
		else: pass
		
		time.sleep(.5)
	
	#===================================================================
	#============================= Clases ==============================
	#===================================================================
	
	class ErrorVaciarPapelera(Exception):
		def __init__(self, cadena): self.cadenaerror = cadena
		def __str__(self): return repr(self.cadenaerror)
	
	class ErrorTipoMensage(Exception):
		def __init__(self, cadena): self.cadenaerror = cadena
		def __str__(self): return repr(self.cadenaerror)
	
	class ErrorTipoSalida(Exception):
		def __init__(self, cadena): self.cadenaerror = cadena
		def __str__(self): return self.cadenaerror
	
	class ErrorBeep(Exception):
		def __init__(self, cadena): self.cadenaerror = cadena
		def __str__(self): return self.cadenaerror
	
	class WinDesktopError(Exception):
		def __init__(self, cadena): self.cadenaerror = cadena
		def __str__(self): return repr(self.cadenaerror)
	
	# Driver.Clipboard.settext('Texto')
	# print(Driver.Clipboard.gettext())
	class Clipboard:
		
		def gettext():
			WCB.OpenClipboard()
			data = WCB.GetClipboardData()
			WCB.CloseClipboard()
			return data
		
		def settext(cadena):
			WCB.OpenClipboard()
			WCB.EmptyClipboard()
			WCB.SetClipboardText(cadena.encode('utf-8'), WCB.CF_TEXT)
			WCB.CloseClipboard()
	
	# Driver.Copiar('Text')
	# print(Driver.Pegar())
	Pegar	= Clipboard.gettext;	pegar	= Clipboard.gettext
	Paste	= Clipboard.gettext;	paste	= Clipboard.gettext
	Put		= Clipboard.gettext;	put		= Clipboard.gettext
	
	Copiar	= Clipboard.settext;	copiar	= Clipboard.settext
	Copy	= Clipboard.settext;	copy	= Clipboard.settext
	Get		= Clipboard.settext;	get		= Clipboard.settext
	
	#===================================================================
	#============================ Funciones ============================
	#===================================================================
	
	def beep(self, tono=5, duracion=0.5):
		
		if tono >= 1 and tono <= 10:
			if duracion >= .1 and duracion <= 10: WA.Beep(int(tono*100), int(duracion*1000))
			else: raise self.ErrorBeep('\n\n\t Duración Seleccionada: {} segundos\n\n\t Rango Valido de Duración: 0.3 a 10 segundos'.format(duracion))
		else: raise self.ErrorBeep('\n\n\t Tonalidad Seleccionada: {}\n\n\t Rango Valido de Tono: 3 a 10'.format(tono))
	
	def changePasswordCurrentUser(self, oldPassword, newPassword):
		WN.NetUserChangePassword(None, None, oldPassword, newPassword)
	
	def cleanRecyclerBin(self, tipo=0, unidad='C:'):	# int Tipo, str Unidad.
		""" Tipos:
		 -------------------------------------------------------------
		| 0 = NORMAL			  | 4 = SIN_SONIDO					  |
		| 1 = SIN_CONFIRMACION	  | 5 = 4 + 1						  |
		| 2 = SIN_BARRA_PROGRESO  | 6 = 4 + 2						  |
		| 3 = 2 + 1				  | 7 = 4 + 2 + 1 = TOTAL_INADVERTIDO |
		 -------------------------------------------------------------
		"""
		unidad = unidad.upper()
		if re.search('^[A-Z]{1}:$', str(unidad)) == None:
			return False
		if tipo >= 0 and tipo <= 7:
			try:
				shell.SHEmptyRecycleBin(None, unidad, tipo)
			except pywintypes.com_error:
				raise self.ErrorVaciarPapelera('La papelera ya esta vacia.')
	
	def closeCMD(self): WCS.FreeConsole()
	
	def displaySwitch(self, tipo=0):
		# 0 = internal:	Solo Primera Pantalla.
		# 1 = external:	Solo Segunda Pantalla.
		# 2 = clone:	Pantalla Duplicada.
		# 3 = extend:	Pantalla Extendida.
		if tipo < 0 or tipo > 3: tipo = 0
		tipos = ['/internal', '/external', '/clone', '/extend']
		cmd = 'displayswitch.exe ' + tipos[tipo]
		run_command(cmd)
	
	def ejectCDROM(self):
		
		name = 'eject.vbs'
		codigo = """
			' VBS Script para Expulsar la bandeja de Disco.
			
			Set oWMP = CreateObject("WMPlayer.OCX.7")
			Set colCDROMs = oWMP.cdromCollection
			colCDROMs.Item(0).eject
		"""
		
		with open(name,'w') as File:
			File.write(codigo)
			File.close()
		
		key = run_command('cscript '+name).split('\n')
		os.remove(name)
	
	def exitWindows(self, tiposalida):	# LogOff = Cierre Total de Sesión, Cierra Todas Las Aplicaciones.
		
		TS = str(tiposalida).lower()
		
		if   TS == 'logoff'   or TS == '0': WA.ExitWindowsEx(WC.EWX_LOGOFF,   0)	# EWX_LOGOFF	= 0
		elif TS == 'shutdown' or TS == '1': WA.ExitWindowsEx(WC.EWX_SHUTDOWN, 0)	# EWX_SHUTDOWN	= 1
		elif TS == 'reboot'   or TS == '2': WA.ExitWindowsEx(WC.EWX_REBOOT,   0)	# EWX_REBOOT	= 2
		else:
			texto =  "\n\n [!] El Tipo de Salida de Windows '{}' No Es Valido.".format(TS)
			texto += "\n\n [+] Tipos de Salida Validas:\n\n\t 0: 'LogOff'.\n\t 1: 'ShutDown'.\n\t 2: 'ReBoot'."
			raise self.ErrorTipoSalida(texto)
	
	def getAvailableRAM(self, raw=False):
		
		cadena = ''
		B = WA.GlobalMemoryStatus()['AvailPhys']
		Gb = B / 1073741824
		Mb = B / 1048576
		Kb = B / 1024
		B  = B % 1024
		
		if raw: return {'GB':int(Gb),'MB':int(Mb)%1024,'KB':int(Kb)%1024,'B':B}
		else:
			
			if   Gb > 1: cadena = '{:.3f} Gb'.format(Gb)
			elif Mb > 1: cadena = '{:.3f} Mb'.format(Mb)
			elif Kb > 1: cadena = '{:.3f} Kb'.format(Kb)
			else: cadena = '{} bytes'.format(B)
			
			return cadena
	
	def getComputerName(self): return WA.GetComputerName()
	
	def getCurrentProcess(self): return WA.GetCurrentProcessId()
	
	def getCursorPos(self): return WA.GetCursorPos()
	
	def getDisplaySettings(self):
		'''return x_resolution, y_resolution, colour_depth'''
		xScreen = WA.GetSystemMetrics(WC.SM_CXSCREEN)	# SM_CXSCREEN = 0
		yScreen = WA.GetSystemMetrics(WC.SM_CYSCREEN)	# SM_CYSCREEN = 1
		bPixels = WU.GetDeviceCaps(WG.GetDC(0), WC.BITSPIXEL)
		return [xScreen, yScreen, bPixels]
	
	def getNumberOfProcessors(self): return WA.GetNativeSystemInfo()[5]
	
	def getNumberOfMonitors(self): return WA.GetSystemMetrics(WC.SM_CMONITORS)	# SM_CMONITORS = 80
	
	def getNumItemsInRecyclerBin(self): return shell.SHQueryRecycleBin()[1]
	
	def getProcessID(self, nameprocess):
		
		def aux(HWND,info):
			if WG.IsWindowVisible(HWND) and WG.GetWindowText(HWND) != '': info.append((HWND, WG.GetWindowText(HWND)))#, WP.GetProcessId(HWND)))
		
		info = []
		WG.EnumWindows(aux, info)
		
		for inf in info:
			if nameprocess in inf[1]: return WP.GetWindowThreadProcessId(inf[0])[1]
	
	def getProcessPrivileges(self, PID):
		
		try:
			# obtain a handle to the target process
			HProc = WA.OpenProcess(WC.PROCESS_QUERY_INFORMATION, False, PID)	# PROCESS_QUERY_INFORMATION = 1024 # (0x0400) or PROCESS_VM_READ (0x0010) or PROCESS_ALL_ACCESS (0x1F0FFF)
			# open the main process token
			HTok = WS.OpenProcessToken(HProc, WC.TOKEN_QUERY)					# TOKEN_QUERY = 8
			# retrieve the list of privileges enabled
			privs = WS.GetTokenInformation(HTok, WS.TokenPrivileges)			# TokenPrivileges = 3
			# iterate over privileges and output the ones that are enabled
			privlist = ""
			
			for inf in privs:
				# check if the privilege is enabled
				if inf[1] == 3: privlist += "{}|".format(WS.LookupPrivilegeName(None, inf[0]))
					
		except: privlist = "N/A"
		
		return privlist
	
	def getTimeActiveSystem(self, segundos=False):
		
		_Ms = WA.GetTickCount()
		cadena = ''
		
		if segundos: return str(_Ms // 1000)	# Devuelve el Tiempo Activo del Sistema en Segundos.
		else:	# Devuelve el Tiempo Activo del Sistema en 'Dias Horas:Minutos:Segundos'.
			
			_Segundos = (  _Ms // 1000 )  % 60
			_Minutos = (( _Ms // 1000 ) // 60 )  % 60
			_Horas = ((( _Ms // 1000 ) // 60 ) // 60 )  % 24
			_Dias = ((( _Ms // 1000 ) // 60 ) // 60 ) // 24
			
			if not _Dias == 0: cadena += str(_Dias) + 'd '
			cadena += ('0' + str(_Horas) + ':') if _Horas < 10 else (str(_Horas) + ':')
			cadena += ('0' + str(_Minutos) + ':') if _Minutos < 10 else (str(_Minutos) + ':')
			cadena += ('0' + str(_Segundos)) if _Segundos < 10 else (str(_Segundos))
			
			return cadena
	
	def getTotalRAM(self, raw=False):
		
		cadena = ''
		B = WA.GlobalMemoryStatus()['TotalPhys']
		Gb = B / 1073741824
		Mb = B / 1048576
		Kb = B / 1024
		B  = B % 1024
		
		if raw: return {'GB':int(Gb),'MB':int(Mb)%1024,'KB':int(Kb)%1024,'B':B}
		else:
			
			if   Gb > 1: cadena = '{:.3f} Gb'.format(Gb)
			elif Mb > 1: cadena = '{:.3f} Mb'.format(Mb)
			elif Kb > 1: cadena = '{:.3f} Kb'.format(Kb)
			else: cadena = '{} bytes'.format(B)
			
			return cadena
	
	def getTotalSizeInRecyclerBin(self, raw=False):
		
		cadena = ''
		B = shell.SHQueryRecycleBin()[0]
		Gb = B / 1073741824
		Mb = B / 1048576
		Kb = B / 1024
		B  = B % 1024
		
		if raw: return {'GB':int(Gb),'MB':int(Mb)%1024,'KB':int(Kb)%1024,'B':B}
		else:
			
			if   Gb > 1: cadena = '{:.3f} Gb'.format(Gb)
			elif Mb > 1: cadena = '{:.3f} Mb'.format(Mb)
			elif Kb > 1: cadena = '{:.3f} Kb'.format(Kb)
			else: cadena = '{} bytes'.format(B)
			
			return cadena
	
	def getWindowsProductKey(self, return_key):
		
		name = 'gwpk.vbs'
		codigo = """
			' VBS Script para obtener la Clave de Producto Original de Windows.
			
			Set WshShell = WScript.CreateObject("WScript.Shell")
			KeyPath = "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\DigitalProductId"
			
			Function ExtractKey(KeyInput)
				Const KeyOffset = 52
				i = 28
				CharWhitelist = "BCDFGHJKMPQRTVWXY2346789"
				Do
					Cur = 0
					x = 14
					Do
						Cur = Cur * 256
						Cur = KeyInput(x + KeyOffset) + Cur
						KeyInput(x + KeyOffset) = (Cur \ 24) And 255
						Cur = Cur Mod 24
						x = x -1
					Loop While x >= 0
					i = i -1
					KeyOutput = Mid(CharWhitelist, Cur + 1, 1) & KeyOutput
					If (((29 - i) Mod 6) = 0) And (i <> -1) Then
						i = i -1
						KeyOutput = "-" & KeyOutput
					End If
				Loop While i >= 0
				ExtractKey = KeyOutput
			End Function
			
			Dim fso, MiArchivo
			Set fso = CreateObject("Scripting.FileSystemObject")
			Set MiArchivo = fso.CreateTextFile("ClaveProducto.zion", True)
			MiArchivo.WriteLine(ExtractKey(WshShell.RegRead(KeyPath)))
			MiArchivo.Close
			
			WScript.Echo ExtractKey(WshShell.RegRead(KeyPath))
		"""
		
		with open(name,'w') as File:
			File.write(codigo)
			File.close()
		
		key = run_command('cscript '+name).split('\n')
		os.remove(name)
		
		if return_key:
			while '' in key: key.remove('')
			return key[-1]
	
	def killProcess(self, PID):
		if PID != None:
			return (0 != WA.TerminateProcess(WA.OpenProcess(1, 0, int(PID)), 0))
	
	def lockWorkStation(self):
		#~ run_command('rundll32.exe user32.dll, LockWorkStation')
		windll.user32.LockWorkStation()
	
	def messageBox(self, titulo, mensage, tipo):
		
		if tipo < 0 or tipo > 6: raise self.ErrorTipoMensage('Tipo de Mensage Fuera del Rango: 0 a 6')
		
		respuesta = WA.MessageBox(-0, mensage, titulo, tipo)
		
		if   respuesta == 0: return 'Error'
		elif respuesta == 1: return 'Aceptar'
		elif respuesta == 2: return 'Cancelar'
		elif respuesta == 3: return 'Anular'
		elif respuesta == 4: return 'Reintentar'
		elif respuesta == 5: return 'Omitir'
		elif respuesta == 6: return 'Sí'
		elif respuesta == 7: return 'No'
		elif respuesta == 10: return 'Reintentar'
		elif respuesta == 11: return 'Continuar'
		else: return respuesta
	
	def minimizeWindowCMD(self): WG.ShowWindow(WG.GetForegroundWindow(), WC.SW_MINIMIZE)
	
	def minimizeAll(self):
		
		name = 'min.vbs'
		codigo = """
			' VBS Script para Minimizar todas las ventanas.
			
			Set var = CreateObject("Shell.Application")
			var.MinimizeAll
		"""
		
		with open(name,'w') as File:
			File.write(codigo)
			File.close()
		
		key = run_command('cscript '+name).split('\n')
		os.remove(name)
	
	def isMouseInstalled(self):
		val = WA.GetSystemMetrics(WC.SM_MOUSEPRESENT)	# SM_MOUSEPRESENT = 19
		return val == 1
	
	def isSlowMachine(self):
		# Es 1 si la computadora tiene un procesador de gama baja (lento)
		val = WA.GetSystemMetrics(WC.SM_SLOWMACHINE)		# SM_SLOWMACHINE = 73
		return val == 1
	
	def isUserAnAdmin(self): return shell.IsUserAnAdmin()
	
	def screenshot(self, openss=False): 
				
		# Usa DPI Aware para tomar una captura de pantalla completa.
		windll.user32.SetProcessDPIAware()
		
		# Valida el nombre y ruta de guardado para la captura:
		if not os.path.exists('Screenshots'):
			os.mkdir('Screenshots')
		
		data = 0
		save_as = 'Screenshots\\Screenshot_{}.jpg'.format(str(data).zfill(2))
		
		while os.path.isfile(save_as):
			print(os.path.isfile(save_as))
			data += 1
			save_as = 'Screenshots\\Screenshot_{}.jpg'.format(str(data).zfill(2))
		
		# Guarda la captura:
		image = ImageGrab.grab()
		image.save(save_as)
		if openss: threading.Thread(target=image.show).start()
	
	def setCursorPos(self, posX, posY): WA.SetCursorPos((posX, posY))
	
	def setDisplayRotation(self, monitor=0):
		# monitor:
		# 0 = Monitor Principal
		# 1 = Segundo Monitor
		display = self.display1_orientation if monitor == 0 else self.display2_orientation
		
		device = WA.EnumDisplayDevices(None, monitor);
		fullName = device.DeviceString
		name = device.DeviceName
		dm = WA.EnumDisplaySettings(name, WC.ENUM_CURRENT_SETTINGS)
		# WC.DMDO_DEFAULT=0, WC.DMDO_90=1, WC.DMDO_180=2, WC.DMDO_270=3
		
		dm.DisplayOrientation = 0 if display == 2 else 2
		if   monitor == 0: self.display1_orientation = dm.DisplayOrientation
		elif monitor == 1: self.display2_orientation = dm.DisplayOrientation
		dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
		dm.Fields = dm.Fields & WC.DM_DISPLAYORIENTATION
		WA.ChangeDisplaySettingsEx(name, dm)
	
	def setDisplaySettings(self, xres=None, yres=None, cdepth=32):
		"""Changes the display resolution and bit depth on Windows.
		
		From Shane Holloway's post http://aspn.activestate.com/ASPN/Mail/Message/wxPython-users/1684800"""
		
		DM_BITSPERPEL		= 0x00040000
		DM_PELSWIDTH		= 0x00080000
		DM_PELSHEIGHT		= 0x00100000
		CDS_UPDATEREGISTRY	= 0x00000001
		CDS_FULLSCREEN		= 0x00000004
		SIZEOF_DEVMODE		= 148
		
		DevModeData = struct.calcsize("32BHH") * '\x00'.encode()
		DevModeData += struct.pack("H", SIZEOF_DEVMODE)
		DevModeData += struct.calcsize("H") * '\x00'.encode()
		dwFields = (xres and DM_PELSWIDTH or 0) | (yres and DM_PELSHEIGHT or 0) | (cdepth and DM_BITSPERPEL or 0)
		DevModeData += struct.pack("L", dwFields)
		DevModeData += struct.calcsize("l9h32BHL") * '\x00'.encode()
		DevModeData += struct.pack("LLL", cdepth or 0, xres or 0, yres or 0)
		DevModeData += struct.calcsize("8L") * '\x00'.encode()
		result = ctypes.windll.user32.ChangeDisplaySettingsA(DevModeData, CDS_FULLSCREEN | CDS_UPDATEREGISTRY)
		if result != 0: # success if zero, some failure otherwise
			raise WinDesktopError("setDisplaySettings() died, call to ChangeDisplaySettingsA returned" + repr(result))
	
	def setPriorityPID(self, PID=None, priority=1):
		
		""" Setea La Prioridad de un Proceso de Windows.
			El Valor de Prioridad se da entre 0-5 en donde 2 es la Prioridad Normal.
			Pro Defecto se pondra la Prioridad en 1 en el Actual Proceso de Python."""
		
		priorityclasses = [WP.IDLE_PRIORITY_CLASS,
						   WP.BELOW_NORMAL_PRIORITY_CLASS,
						   WP.NORMAL_PRIORITY_CLASS,
						   WP.ABOVE_NORMAL_PRIORITY_CLASS,
						   WP.HIGH_PRIORITY_CLASS,
						   WP.REALTIME_PRIORITY_CLASS]
		
		if PID == None: PID = WA.GetCurrentProcessId()
		
		handle = WA.OpenProcess(WC.PROCESS_ALL_ACCESS, True, PID)
		WP.SetPriorityClass(handle, priorityclasses[priority])
	
	def setTopWindow(self, nameprocess):
		
		def aux(HWND,info):
			
			if WG.IsWindowVisible(HWND) and WG.GetWindowText(HWND) != '': info.append((HWND, WG.GetWindowText(HWND)))
		
		info = []
		WG.EnumWindows(aux, info)

		for inf in info:
			
			# ~ print(inf)
			if nameprocess in inf[1]:
				
				PyCWnd1 = WU.FindWindow( None, inf[1] )
				PyCWnd1.SetForegroundWindow()
				PyCWnd1.SetFocus()
				return True
	
	def setVolume(self, porcent):
		porcent = porcent//2
		name = 'vol.vbs'
		codigo = """
			' VBS Script para Subir o Bajar el Volumen del Sistema Activo.
			
			Set WshShell = CreateObject("WScript.Shell")
			
			for i = 1 to 50
				WshShell.SendKeys(chr(174))
			next
			
			for i = 1 to {}
				WshShell.SendKeys(chr(175))
			next
		""".format(porcent)
		
		with open(name,'w') as File:
			File.write(codigo)
			File.close()
		
		key = run_command('cscript '+name).split('\n')
		os.remove(name)
	
	def startApp(self, nombre): WA.WinExec(nombre)
	
	#######

class AnimatedGif(tk.Label):
	"""
	Class to show animated GIF file in a label
	Use start() method to begin animation, and set the stop flag to stop it
	"""
	def __init__(self, root, gif_file, delay=0.04):
		"""
		:param root: tk.parent
		:param gif_file: filename (and path) of animated gif
		:param delay: delay between frames in the gif animation (float)
		"""
		tk.Label.__init__(self, root)
		self.root = root
		self.gif_file = gif_file
		self.delay = delay  # Animation delay - try low floats, like 0.04 (depends on the gif in question)
		self.stop = False  # Thread exit request flag

		self._num = 0

	def start(self):
		""" Starts non-threaded version that we need to manually update() """
		self.start_time = time.time()  # Starting timer
		self._animate()

	def stop(self):
		""" This stops the after loop that runs the animation, if we are using the after() approach """
		self.stop = True

	def _animate(self):
		try:
			self.gif = tk.PhotoImage(file=self.gif_file, format='gif -index {}'.format(self._num))  # Looping through the frames
			self.configure(image=self.gif)
			self._num += 1
		except tk.TclError:  # When we try a frame that doesn't exist, we know we have to start over from zero
			self._num = 0
		if not self.stop:    # If the stop flag is set, we don't repeat
			self.root.after(int(self.delay*1000), self._animate)

	def start_thread(self):
		""" This starts the thread that runs the animation, if we are using a threaded approach """
		from threading import Thread  # We only import the module if we need it
		self._animation_thread = Thread()
		self._animation_thread = Thread(target=self._animate_thread).start()  # Forks a thread for the animation

	def stop_thread(self):
		""" This stops the thread that runs the animation, if we are using a threaded approach """
		self.stop = True

	def _animate_thread(self):
		""" Updates animation, if it is running as a separate thread """
		while self.stop is False:  # Normally this would block mainloop(), but not here, as this runs in separate thread
			try:
				time.sleep(self.delay)
				self.gif = tk.PhotoImage(file=self.gif_file, format='gif -index {}'.format(self._num))  # Looping through the frames
				self.configure(image=self.gif)
				self._num += 1
			except tk.TclError:  # When we try a frame that doesn't exist, we know we have to start over from zero
				self._num = 0
			except RuntimeError:
				sys.exit()
	
	#######

#=======================================================================
#=======================================================================
#=======================================================================

def getSession(driver):
	global id_a
	
	path = os.getcwd()		# Ruta actual del Script.
	
	if os.path.exists(path+'/id'):
		with open(path+'/id', 'r') as File:
			text = File.read()
			id_a = int(text.split(': ')[1])
			File.close()
	else:
		id_a = 0
	#~ 
	#~ html = driver.execute_script('return document.documentElement.outerHTML')
	#~ soup = BeautifulSoup(html, 'html.parser')
	#~ 
	#~ jsons = soup.findAll('td')	# obtenemos todos los JSONs
	#~ jsons.pop(0)				# Eliminamos el primer elemento, no lo necesitamos.
	#~ jslen = len(jsons)			# Obtenemos la candidad de JSONs
	#~ 
	#~ # Si el comando del ultimo ID ejecutado (id_a) es mayor a la
	#~ # cantidad de JSONs, entonces se borraron JSONs.
	#~ if id_a > jslen:
		#~ id_a = 0
	
	return


def saveSession():
	path = os.getcwd()
	with open(path+'/id', 'w') as File:
		File.write('ID: '+str(id_a))
		File.close()


def connect(driver):
	
	global cont, cony, id_a
	
	title = None
	cony += 1
	
	html = driver.execute_script('return document.documentElement.outerHTML')
	soup = BeautifulSoup(html, 'html.parser')
	
	os.system('cls')			# Limpiamos pantalla.
	jsons = soup.findAll('td')	# obtenemos todos los JSONs
	try:
		jsons.pop(0)				# Eliminamos el primer elemento, no lo necesitamos.
	except:
		pass
	jslen = len(jsons)			# Obtenemos la candidad de JSONs
	cmds = []					# Lista de JSONS (Cmds = Comandos)
	
	if jslen > 0 and jslen < id_a:
		id_a = 0
	
	print('\n Elementos: '+str(jslen))
	
	if jslen == 0:
		cont += 1
		if cont == 30:
			print('\n\n Actualizando...\n')
			driver.get(page)
			cont, cony = 0, 0
	else:
		for j in jsons:
			j = json.loads(j.text)
			id_ = j['id']
			if id_ > id_a:
				id_a = id_
				cmds.append(j)
				saveSession()
	
	if cony == 200:
		print('\n\n Actualizando...\n')
		driver.get(page)
		cont, cony = 0, 0
	
	time.sleep(.01)
	
	return driver, cmds


def executecmd(driver):
	
	lc = len(cola)
	
	for _ in range(lc):
		
		cmd = cola.pop(0)
		print('\n' + str(cmd['id']) + ':' + cmd['comando'] + ' - En ejecucion...', end='')
		sys.stdout.write('\r' + str(cmd['id']) + ':' + cmd['comando'] + '\t\t\t')
		
		driver.execute(cmd['comando'])


def closeApp():
	
	while True:
		if keyboard.is_pressed('esc')\
		or keyboard.is_pressed('q')\
		or endapp:
			
			navi.GIF(img=navi.img4, size=navi.img4size, t=10)
			time.sleep(5)
			
			Hide(False)
			run_command('mode con cols=15 lines=5')
			#~ drivercmds.minimizeWindowCMD()
			
			#~ with open('down.cmd', 'w') as File:
				#~ File.write('del "%0" && timeout /nobreak 5 && taskkill /F /IM cmd.exe ')
				#~ File.close()
			#~ run_command('start down.cmd')
			
			#~ print(isProcessActive('cmd.exe'))
			
			run_command('taskkill /F /IM chromedriver.exe')
			run_command('taskkill /F /IM cmd.exe')
			
			#~ PID = drivercmds.getProcessID('Navi Driver')
			#~ print(PID)
			#~ drivercmds.killProcess(PID)
			#~ drivercmds.closeCMD()
			PID = drivercmds.getCurrentProcess()
			print(PID)
			drivercmds.killProcess(PID)
			sys.exit()
		time.sleep(.05)


def startApp():
	global navi
	# Run:
	navi = Navi()
	navi.centrar()
	navi.runNavi()


def rot13(text):
	text = text.upper()
	nor = [l for l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
	inv = [l for l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'][::-1]
	norn = [l for l in '5123467890']
	invn = [l for l in '5123467890'][::-1]
	t = ''
	for x in range(len(text)):
		try:
			t += inv[nor.index(text[x])]
		except ValueError:
			try:
				t += invn[norn.index(text[x])]
			except ValueError:
				t += text[x]
	return t


def showText(text, pos, t, ext):
	pos += ext
	master = tk.Tk()
	master.overrideredirect(True)
	master.lift()
	#~ master.wm_attributes('-disabled', True)
	master.wm_attributes('-topmost', True)
	master.wm_attributes('-transparentcolor', 'white')
	label = tk.Label(master, text=rot13(text), bg='cyan', font=('PixelCrypt', 24), width=16, height=1).pack()
	size = master.geometry().split('+')[0].split('x')
	X = int(master.winfo_screenwidth()/2 - int(size[0])/2)
	Y = int(master.winfo_screenheight()/2 - int(size[1])/2)
	master.geometry('+{}+{}'.format(X, Y+(pos*32)))
	#~ print(master.geometry())
	master.after(t*1000, lambda: master.destroy())
	master.mainloop()


def printText(text, time, ext=0):
	temp = text.split()
	tlis = ['' for _ in range(10)]
	cade = ''
	cont = 0
	
	for i, x in enumerate(temp):
		if len(cade+x) > 16:
			tlis[cont] += cade
			cont += 1
			cade = ''
		print(x, cade)
		if cade == '':
			cade += x
		else:
			cade += ' '+x
	tlis[cont] += cade
	
	while '' in tlis: tlis.remove('')
	
	for i, x in enumerate(tlis):
		threading.Thread(target=showText, args=(x, i, time, ext,)).start()


def run():
	global cola, endapp, CAT
	
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')		# No mostrar el navegador
	driver = webdriver.Chrome(chrome_options = chrome_options)
	driver.get(page)
	getSession(driver)
	printText('Cargado', 2, 3)
	while True:
		
		driver, cmds = connect(driver)
		
		if not CAT.is_alive():
			CAT = threading.Thread(target=closeApp)
			CAT.start()
			print('xD')
			os.system('Pause')
		
		for cmd in cmds:
			cola.append(cmd)
		
		if not cola == []:
			executecmd(drivercmds)



os.system('title Navi Driver')

print('Cargando...')

drivercmds = Driver()
navi = None
endapp = False
page = 'https://driver-so.firebaseapp.com'
cola = []
id_a = 0
cont = 0
cony = 0

SAT = threading.Thread(target=startApp)
SAT.setName('StartApp')
SAT.start()
time.sleep(3)
CAT = threading.Thread(target=closeApp)
CAT.setName('CloseApp')
CAT.start()

#~ printText('Bienvenidos Todos a este programa', 10)

print('Cargado...')

run()


