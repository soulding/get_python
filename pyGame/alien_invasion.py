import pygame
from pygame.sprite import Group
#导入Settings类
from settings import Settings
from game_stats import GameStats
from button import Button
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
		(ai_settings.screen_width,ai_settings.screen_height)
	)
	#窗口标题
	pygame.display.set_caption("Alien Invasion")
	#创建Play按钮
	play_button = Button(ai_settings, screen, "Play")
	#创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)
	#创建一艘飞船
	ship = Ship(ai_settings, screen)
	#创建一个用于存储子弹的编组
	bullets = Group()
	#创建一个外星人
	aliens = Group()
	gf.create_fleet(ai_settings, screen, ship, aliens)
	#开始游戏主循环
	while True:
		gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
			gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
run_game()