from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Button(QPushButton):

	def __init__(self,a,b,pic):
		super(Button, self).__init__(a,b)
		self.setSizePolicy ( QSizePolicy.Preferred, QSizePolicy.Preferred)
		self.setMaximumWidth(48)
		self.setMaximumHeight(48)
		self.resize(48,48)
		self.setFlat(True)
		self.setAutoFillBackground(True)
		self.setIcon(QIcon(pic))
		self.setIconSize(QSize(48,48))
		self.flag = True
		self.towerpic = pic

	def set_flag(self, a):
		self.flag = a

	def mouseMoveEvent(self, e):
		if e.buttons() != Qt.LeftButton:
			return

		if (self.flag == True):
			# write the relative cursor position to mime data
			mimeData = QMimeData()
			# simple string with 'x,y'
			mimeData.setText('%d,%d' % (e.x(), e.y()))

			# let's make it fancy. we'll show a "ghost" of the button as we drag
			# grab the button to a pixmap
			pixmap = QPixmap.grabWidget(self)

			# below makes the pixmap half transparent
			painter = QPainter(pixmap)
			painter.setCompositionMode(painter.CompositionMode_DestinationIn)
			painter.fillRect(pixmap.rect(), QColor(0, 0, 0, 127))
			painter.end()

			# make a QDrag
			drag = QtGui.QDrag(self)
			# put our MimeData
			drag.setMimeData(mimeData)
			# set its Pixmap
			drag.setPixmap(pixmap)
			# shift the Pixmap so that it coincides with the cursor position
			drag.setHotSpot(e.pos())

			# start the drag operation
			# exec_ will return the accepted action from dropEvent
			if drag.exec_(Qt.CopyAction | Qt.MoveAction) == Qt.MoveAction:
				print 'moved'
			else:
				print 'copied'


	def mousePressEvent(self, e):
		if (self.flag == False):
			#QtGui.QPushButton.mousePressEvent(self, e)
			if e.button() == Qt.LeftButton:
				print "pressed"


############################################################
class Tower(Button):
	def __init__(self,a,b,attack,speed,pic):
		self.attack = attack
		self.speed = speed
		self.position = []
		Button.__init__(self,a,b, pic)

	def set_flag(self, a):
		return Button.set_flag(self,a)

	def get_attack(self):
		return self.attack

	def set_speed(self, a):
		self.speed = a

	def get_position(self):
		return self.position

	def set_position(self, row, column):
		self.position[0] = row
		self.position[1] = column

	def get_speed(self):
		return self.speed

	def set_attack(self, a):
		self.attack = a

############################################################
class arrowTower(Tower):
	def __init__(self,attack, speed, numName, pic):
		self.name = "arrow" + str(numName)
		Tower.__init__(self,attack,speed)

	def get_attack(self):
		return Tower.get_attack(self)

	def set_speed(self, a):
		Tower.set_speed(self,a)

	def get_position(self):
		return Tower.get_position(self)

	def set_position(self, row, column):
		Tower.set_position(self,row,column)

	def get_speed(self):
		return Tower.get_speed(self)

	def set_attack(self, a):
		Tower.set_attack(self,a)

#############################################################
class Player:
	def __init__(self):
		self.gold = 200
		self.lives = 100
		self.level = 0
		self.currentRound = 0

	def set_gold(self, a):
		self.gold = a

	def get_gold(self):
		return self.gold

	def set_lives(self, a):
		self.lives = a

	def get_lives(self):
		return self.lives

	def set_level(self, a):
		self.level = a

	def get_level(self):
		return self.level

	def set_round(self, a):
		self.currentRound = a

	def get_round(self):
		return self.currentRound

