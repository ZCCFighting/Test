	def paintEvent(self,e):
		'''
		绘图
		:param e:
		:return:
		'''
		painter = QPainter()
		painter.begin(self)
		self.draw_img(painter)
		painter.end()

	def draw_img(self,painter):
		painter.drawPixmap(self.lable_show_img.point, self.scaled_img)

	def mouseMoveEvent(self.able_show_img, e):  # 重写移动事件
		if self.lable_show_img.left_click:
			self.lable_show_img._endPos = e.pos() - self.lable_show_img._startPos
			self.lable_show_img.point = self.lable_show_img.point + self.lable_show_img._endPos
			self.lable_show_img._startPos = e.pos()
			self.lable_show_img.repaint()


	def mousePressEvent(self, e):
		if e.button() == Qt.LeftButton:
			self.left_click = True
			self._startPos = e.pos()

	def mouseReleaseEvent(self, e):
		if e.button() == Qt.LeftButton:
			self.left_click = False
		elif e.button() == Qt.RightButton:
			self.point = QPoint(0, 0)
			self.scaled_img = self.img.scaled(self.size())
			self.repaint()



	def wheelEvent(self, e):
		if e.angleDelta().y() > 0:
			# 放大图片
			self.scaled_img = self.img.scaled(self.scaled_img.width()-15, self.scaled_img.height()-15)
			new_w = e.x() - (self.scaled_img.width() * (e.x() - self.point.x())) / (self.scaled_img.width() + 15)
			new_h = e.y() - (self.scaled_img.height() * (e.y() - self.point.y())) / (self.scaled_img.height() + 15)
			self.point = QPoint(new_w, new_h)
			self.repaint()
		elif e.angleDelta().y() < 0:
			# 缩小图片
			self.scaled_img = self.img.scaled(self.scaled_img.width()+15, self.scaled_img.height()+15)
			new_w = e.x() - (self.scaled_img.width() * (e.x() - self.point.x())) / (self.scaled_img.width() - 15)
			new_h = e.y() - (self.scaled_img.height() * (e.y() - self.point.y())) / (self.scaled_img.height() - 15)
			self.point = QPoint(new_w, new_h)
			self.repaint()


	def resizeEvent(self, e):
		if self.parent is not None:
			self.scaled_img = self.img.scaled(self.size())
			self.point = QPoint(0, 0)
			self.update()
