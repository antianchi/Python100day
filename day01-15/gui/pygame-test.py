# -*- coding: utf-8 -*-
#! python3
"""
Author: antch
Email: atc00@foxmail.com

date: 2019/5/26 16.46
desc: GUI程序开发-pygame.

"""

import pygame
import random
import math
# 枚举支持
from enum import Enum, unique


@unique
class Color(Enum):
    """颜色"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)


class Ball(object):
    """球"""

    def __init__(self, x, y, radius, sx, sy, screen, c=Color.RED):
        """初始化方法"""
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = c
        self.alive = True
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

    def move(self, screen):
        """移动"""
        self.x += self.sx
        self.y += self.sy

        if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        """吃其他球"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

        # 球的半径不能大于，窗口的高/2和宽/2的最小值
        if self.radius >= min(self.screen_height/2, self.screen_width/2):
            self.alive = False

    def draw(self, screen):
        """在窗口上绘制球"""
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)


def main():
    # 初始化导入的pygame中的模块
    pygame.init()

    # 初始化用于显示的窗口，并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))

    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')

    # 设置窗口的背景颜色，颜色是由三原色元组勾成的
    screen.fill((242, 242, 242))

    ball_image = pygame.image.load('f:/1.png')

    # 在窗口上渲染图像
    screen.blit(ball_image, (50, 50))

    # 定义变量用来表示小球在屏幕上的位置
    x, y = 50, 50

    # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
    pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
    # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    pygame.display.flip()

    running = True

    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0,), (x, y), 30, 0)
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        x, y = x + 5, y + 5


def main2():
    # 定义用来承装所有球的容器
    balls = []
    # 初始化导入的pygame中的模块
    pygame.init()

    # 初始化用于显示的窗口并设置窗口的尺寸
    screen = pygame.display.set_mode((800, 600))

    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 处理鼠标事件的代码
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获得鼠标点击的位置
                x, y = event.pos
                radius = random.randint(10, 100)
                sx, sy = random.randint(-10, 10), random.randint(-10, 10)
                color = Color.random_color()
                # 在点击鼠标的位置创建一个球大小和位置随机变化
                ball = Ball(x, y, radius, sx, sy, screen, color)
                # 将球添加到列表容器中
                balls.append(ball)
        screen.fill((255, 255, 255))

        # 取出容器中的球，如果没有被吃掉就绘制  被吃掉就移除

        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)

        pygame.display.flip()

        # 每隔50毫秒就改变球的位置再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 检查有木有吃到其他的球
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main2()
