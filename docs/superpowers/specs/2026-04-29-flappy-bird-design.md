# Flappy Bird 游戏设计文档

## 概述

用 Python + Pygame 实现经典 Flappy Bird 游戏。单文件 OOP 架构，复刻原版核心玩法。

## 架构

单文件 `main.py`，三个类 + 入口函数。

### Bird

- x、y、velocity、gravity (0.5)、flap_strength (-10)
- `update(dt)`: 更新速度和位置
- `flap()`: 设置 velocity 为 flap_strength
- `get_rect()`: 返回 pygame.Rect 碰撞矩形 (40×30)

### Pipe

- x、gap_y、gap_size (160)、width (70)、speed (-3)
- `update(dt)`: 向左移动 speed 像素
- `get_rects()`: 返回上下管道的 (top_rect, bottom_rect)
- `is_offscreen()`: x + width < 0

### Game

- 管理 bird、pipes 列表、score、state (START/PLAYING/GAME_OVER)
- `handle_events()`: 空格 flap / 重来
- `update(dt)`: 更新鸟和管道，碰撞检测，计分，清理离屏管道
- `render()`: 绘制背景、鸟、管道、分数/提示文字
- `reset()`: 重置状态到初始值

## 参数

| 参数 | 值 |
|------|-----|
| 窗口大小 | 400 × 600 |
| 帧率 | 60 FPS |
| 重力 | 0.5 px/帧² |
| flap力度 | -10 px/帧 |
| 管道间距 | 160 px |
| 管道宽 | 70 px |
| 管道速度 | -3 px/帧 |
| 生成间隔 | 每 90 帧 |

## 状态流程

START → (按空格) → PLAYING → (碰撞) → GAME_OVER → (按空格) → START

## 碰撞检测

用 pygame.Rect.colliderect 检测鸟的 rect 与每个管道 rect 或边界（y<0 或 y>600）的碰撞。

## 得分

鸟每穿过一对管道（pipe.x + pipe.width < bird.x 且未被计分），score +1。

## 不实现

- 音效
- 皮肤选择
- 最高分持久化
- 难度递增
