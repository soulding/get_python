import pygame
#导入Settings类
from settings import Settings
#导入Ship类
from ship import Ship
#导入游戏函数
import game_functions as gf

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
	ship = Ship(ai_settings, screen)
	while True:
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)
run_game()