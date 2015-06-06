#!/usr/bin/python
# -*- coding: utf-8 *-*


########################################################################
#IMPORTS
########################################################################
import wx
from ImagePanel import ImagePanel


########################################################################
#CONSTANTS
########################################################################
IMAGE_FILE 	= 'image.png'
ICON 		= 'eye.png'

 
class MainFrame(wx.Frame):


	####################################################################
	#INIT
	####################################################################
	def __init__(self):
		wx.Frame.__init__(self, None)
		self.InitGUI()
		


	####################################################################
	#GUI
	####################################################################	
	def InitGUI(self):
		
		#INIT SIZER
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.imagePanel = ImagePanel(self)
		self.sizer.Add(self.imagePanel, 1, wx.EXPAND)
		self.SetSizer(self.sizer)
		
		#INIT IMAGE PANEL
		self.imagePanel.SetFocus()
		self.imagePanel.SetConfig(ImagePanel.ZOOM_SIZE)	#set config mask
		self.imagePanel.Bind(wx.EVT_CHAR, self.OnKey)	
		self.image = wx.Image(IMAGE_FILE, wx.BITMAP_TYPE_ANY)
		self.imagePanel.SetImage(self.image)

		#CONFIGURE FRAME
		icon = wx.Icon(ICON, wx.BITMAP_TYPE_PNG)
		self.SetIcon(icon)
		self.SetTitle('ImagePanel Example')
		self.Centre()
		self.SetSize((500, 500))
		self.Bind(wx.EVT_SIZE, self.OnSize)
		self.Bind(wx.EVT_ICONIZE, self.OnSize)
		self.Show()


	####################################################################
	#EVENTS
	####################################################################
	def OnKey(self, e):
		try:
			{
				314: 	self.OnLeftScroll,
				316: 	self.OnRightScroll,
				315:	self.OnUpScroll,
				317:	self.OnDownScroll,
				45:	 	self.OnShrink,
				43:	 	self.OnEnlarge,
				350: 	self.OnToggleFullScreen,
				27: 	self.OnExitFullScreen
			}[e.GetKeyCode()](e)
		except KeyError:
			msg = "The key %d hasn't an assigned function"
			print msg % e.GetKeyCode()
		except TypeError, inst:
			print inst.args[0]
		except Exception, inst:
			print inst.args
			

	def OnSize(self, e):
		if self.imagePanel.GetSize()[0] == self.GetSize()[0]:
			self.Unbind(wx.EVT_SIZE)
			self.imagePanel.AutoZoom()
		e.Skip()
	

	def OnUpScroll(self, e):
		self.imagePanel.MoveY(100)
		

	def OnDownScroll(self, e):
		self.imagePanel.MoveY(-100)
			

	def OnLeftScroll(self, e):
		self.imagePanel.MoveX(100)
			

	def OnRightScroll(self, e):
		self.imagePanel.MoveX(-100)

	
	def OnShrink(self, e):
		self.imagePanel.Shrink()
		
		
	def OnEnlarge(self, e):
		self.imagePanel.Enlarge()


	def OnToggleFullScreen(self, e):
		self.ShowFullScreen(not self.IsFullScreen())
			

	def OnExitFullScreen(self, e):
		self.ShowFullScreen(False) 





########################################################################
#INIT APP
########################################################################
if __name__ == "__main__":
	app = wx.App(False)
	frame = MainFrame()
	app.MainLoop()
