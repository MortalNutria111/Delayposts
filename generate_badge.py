from datetime import datetime
from zoneinfo import ZoneInfo

# ========== 可配置区域 ==========
# 上次更新日期，格式：年-月-日（北京时间）
LAST_UPDATE_DATE = "2025-01-20"
# 左侧标签文字
LABEL_TEXT = "拖更天数"
# 天数后缀
SUFFIX_TEXT = "天"
# 徽章基础尺寸
BADGE_HEIGHT = 20
LEFT_WIDTH = 55    # 左侧标签区域宽度
RIGHT_WIDTH = 41   # 右侧数值区域宽度
PADDING = 5        # 文字左右内边距
# 颜色配置
LEFT_BG = "#555555"   # 左侧背景色
RIGHT_BG = "#d73a4a"  # 右侧背景色
TEXT_COLOR = "#ffffff" # 文字颜色
# =================================

# 北京时间计算日期差
beijing_tz = ZoneInfo("Asia/Shanghai")
today = datetime.now(beijing_tz).date()
last_date = datetime.strptime(LAST_UPDATE_DATE, "%Y-%m-%d").date()
days_since = (today - last_date).days

# 生成右侧显示文本
if days_since == 0:
    right_text = "今日更新"
elif days_since < 0:
    right_text = f"还有{-days_since}{SUFFIX_TEXT}"
else:
    right_text = f"{days_since}{SUFFIX_TEXT}"

full_aria_label = f"{LABEL_TEXT}: {right_text}"
total_width = LEFT_WIDTH + RIGHT_WIDTH

# 适配缩放的坐标自动计算
scale = 0.1
left_center_x = (LEFT_WIDTH / 2) / scale
right_center_x = (LEFT_WIDTH + RIGHT_WIDTH / 2) / scale
left_text_len = (LEFT_WIDTH - PADDING * 2) / scale
right_text_len = (RIGHT_WIDTH - PADDING * 2) / scale

svg_content = f'''<svg width="{total_width}" height="{BADGE_HEIGHT}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{full_aria_label}">
  <title>{full_aria_label}</title>
  <filter id="blur">
    <feGaussianBlur stdDeviation="3"/>
  </filter>
  <linearGradient id="s" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <clipPath id="r">
    <rect width="{total_width}" height="{BADGE_HEIGHT}" rx="3"/>
  </clipPath>
  <g clip-path="url(#r)">
    <rect width="{LEFT_WIDTH}" height="{BADGE_HEIGHT}" fill="{LEFT_BG}"/>
    <rect x="{LEFT_WIDTH}" width="{RIGHT_WIDTH}" height="{BADGE_HEIGHT}" fill="{RIGHT_BG}"/>
    <rect width="{total_width}" height="{BADGE_HEIGHT}" fill="url(#s)"/>
  </g>
  <g fill="{TEXT_COLOR}" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110">
    <!-- 左侧标签 -->
    <g transform="scale({scale})">
      <g aria-hidden="true" fill="#010101">
        <text x="{left_center_x}" y="150" fill-opacity=".8" filter="url(#blur)" textLength="{left_text_len}">{LABEL_TEXT}</text>
        <text x="{left_center_x}" y="150" fill-opacity=".3" textLength="{left_text_len}">{LABEL_TEXT}</text>
      </g>
      <text x="{left_center_x}" y="140" textLength="{left_text_len}">{LABEL_TEXT}</text>
    </g>
    <!-- 右侧数值 -->
    <g transform="scale({scale})">
      <g aria-hidden="true" fill="#010101">
        <text x="{right_center_x}" y="150" fill-opacity=".8" filter="url(#blur)" textLength="{right_text_len}">{right_text}</text>
        <text x="{right_center_x}" y="150" fill-opacity=".3" textLength="{right_text_len}">{right_text}</text>
      </g>
      <text x="{right_center_x}" y="140" textLength="{right_text_len}">{right_text}</text>
    </g>
  </g>
</svg>'''

# 保存为SVG文件
with open("badge.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
