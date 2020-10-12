from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore
from os import path
from functions import *
import urllib.request
import os
import sys
import re

From_Class,_= loadUiType(path.join(path.dirname(__file__), 'youtube.ui'))

class MainApp(QMainWindow, From_Class): 
	def __init__(self, parent=None):
		super(MainApp, self).__init__(parent)
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.initGUI()
		self.connectButtons()

	def initGUI(self):
		self.setFixedSize(539, 431)

	def connectButtons(self):
		cwd = os.getcwd()
		self.location_input.setText(cwd)
		self.start_download.clicked.connect(self.startDownload)
		self.browse.clicked.connect(self.browse_button)
		self.fetch_urls.clicked.connect(self.fetchUrls)
		self.stop_downloading.clicked.connect(self.stopDownload)

	def browse_button(self):
		save_location = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
		self.location_input.setText(save_location)

	def setQuality(self):
		pass

	def fetchUrls(self):
		url = self.url_input.text()
		if "https://" not in url:
			QMessageBox.warning(self, "invalid URL", "Please Enter a valid URL")
		else:
			playlist = fetch_playlist_urls(url)
			for i in range(len(playlist[0])):
				title = playlist[1][i]
				self.status_box.append(title)
				link = playlist[0][i]
				self.status_box.append(link)
				self.status_box.append("-----------------------------------")
	def startDownload(self):
		url = self.url_input.text()
		save_location = str(self.location_input.text())
		self.status_box.append("Start Downloading...")
		try:
			urllib.request.urlretrieve(url, save_location, self.progressPar)
		except Exception:
			QMessageBox.warning(self, "Faild", "Faild to Download!!")
			return
		self.status_box.append("Downloading Completed Successfully")
		QMessageBox.information(self, "Success", "Download Completed Successfully!")
		self.progressBar.setValue(0)

	def stopDownload(self):
		pass

	def progressPar(self, blockNum, blockSize, totalSize):
		read = blockNum * blockSize
		if totalSize > 0 :
			percent = read * 100 / totalSize
			self.progressBar.setValue(int(percent))
			QApplication.processEvents()

	def statusBar(self):
		pass

	def totalVideos(self):
		pass

	def currentVideo(self):
		pass


def main():
	app = QApplication(sys.argv)
	window = MainApp()
	window.show()
	app.exec_()


if __name__ == '__main__':main()