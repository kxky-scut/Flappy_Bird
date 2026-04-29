# Flappy Bird

Python + Pygame 实现的经典 Flappy Bird 游戏。

## 安装运行

```bash
pip install pygame
python3 main.py
```

## 游戏操作

| 按键 | 作用 |
|------|------|
| 空格 | 开始游戏 / 拍翅膀 / 重新开始 |
| 关闭窗口 | 退出 |

## 浏览器运行

```bash
pip install pygbag
pygbag .
# 浏览器打开 http://localhost:8000
```

## 自定义角色

替换项目目录下的 `kun.png` 为你的图片（PNG，建议正方形），然后修改 `main.py` 中的 `Bird` 类：

- `SIZE` — 角色尺寸
- `flap_strength` — 跳跃力度（负值越大跳得越高）
- `gravity` — 下落速度

## 目录结构

```
Flappy_Bird/
├── main.py          # 游戏代码
├── kun.png          # 角色图片
└── README.md
```
