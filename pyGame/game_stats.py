class GameStats(object):
	"""跟踪该游戏的统计信息"""
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()

	def reset_stats(self):
		"""初始化在游戏运行期间可能变化的统计信息"""
		self.ship_limit = self.ai_settings.ship_limit
		