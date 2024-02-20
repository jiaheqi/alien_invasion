import pygame.image


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # 新的飞船默认位置为屏幕中央
        self.rect.midbottom = self.screen_rect.midbottom
        # rect的x只能是证书，所以要将其转换为小数，因为飞船速度设置的小数
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志更新飞船位置"""
        # 为了确保飞船不会飞出屏幕右边，添加条件要小于屏幕的右边x坐标
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # 为了确保飞船不会飞出屏幕左边，添加条件大于屏幕左边x坐标
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
