class Settings():
	#存储游戏所有设置的类
	def __init__(self):
		self.screen_width	= 1200
		self.screen_hight	= 500
		self.bg_color		= (230,230,230)
		#速度设置
		self.ship_speed_factor = 1.5
		#子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		
