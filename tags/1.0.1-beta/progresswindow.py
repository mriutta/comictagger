"""
A PyQT4 dialog to show ID log and progress
"""

"""
Copyright 2012  Anthony Beville

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys
from PyQt4 import QtCore, QtGui, uic
import os
from settings import ComicTaggerSettings


class IDProgressWindow(QtGui.QDialog):
	
	
	def __init__(self, parent):
		super(IDProgressWindow, self).__init__(parent)
		
		uic.loadUi(os.path.join(ComicTaggerSettings.baseDir(), 'progresswindow.ui' ), self)
		
		# we can't specify relative font sizes in the UI designer, so
		# make font for scroll window a smidge smaller
		f = self.textEdit.font()
		if f.pointSize() > 10:
			f.setPointSize( f.pointSize() - 2 )
		self.textEdit.setFont( f )	


		