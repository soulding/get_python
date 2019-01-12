import sys
import pygame
#导入Settings类
from settings import Settings
#导入Ship类
from ship import Ship
def run_game():
	#初始化背景设置
	pygame.init()
	#实例化设置类
	ai_settings = Settings()
	#创建一个显示窗口，相当于画布
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_hight)
	)
	#窗口标题
	pygame.display.set_caption("Alien Invasion")
	#背景颜色
	ship = Ship(screen)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		#填充背景色
		screen.fill(ai_settings.bg_color)
		ship.blitme()
		#更新屏幕
		pygame.display.flip()
run_game()