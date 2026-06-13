from datetime import datetime
from zoneinfo import ZoneInfo

# ========== 可配置区域 ==========
# 上次更新日期，格式：年-月-日（北京时间）
LAST_UPDATE_DATE = "2025-01-20"
# 左侧标签文字
LABEL_TEXT = "拖更天数"
# 天数后缀
SUFFIX_TEXT = "天"
# 徽章样式配置
BADGE_HEIGHT = 20
LEFT_BG_COLOR = "#555555"  # 左侧背景色
RIGHT_BG_COLOR = "#d73a4a" # 右侧背景色
TEXT_COLOR = "#ffffff"     # 文字颜色
# =================================

# 统一使用北京时间计算，避免时区误差
beijing_tz = ZoneInfo("Asia/Shanghai")
today = datetime.now(beijing_tz).date()
last_date = datetime.strptime(LAST_UPDATE_DATE, "%Y-%m-%d").date()

# 计算整数天数差
days_since = (today - last_date).days

# 生成右侧显示文本
if days_since == 0:
    right_text = "今日更新"
elif days_since < 0:
    right_text = f"还有{-days_since}{SUFFIX_TEXT}"
else:
    right_text = f"{days_since}{SUFFIX_TEXT}"

full_aria_label = f"{LABEL_TEXT}: {right_text}"

# 生成对应样式的SVG
svg_content = f'''<svg width="96" height="20" role="img" aria-label="{full_aria_label}">
  <title>{full_aria_label}</title>
  <filter id="blur">
    <feGaussianBlur stdDeviation="16"/>
  </filter>
  <linearGradient id="s" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <clipPath id="r">
    <rect width="96" height="{BADGE_HEIGHT}" rx="3"/>
  </clipPath>
  <g clip-path="url(#r)">
    <rect width="55" height="{BADGE_HEIGHT}" fill="{LEFT_BG_COLOR}"/>
    <rect x="55" width="41" height="{BADGE_HEIGHT}" fill="{RIGHT_BG_COLOR}"/>
    <rect width="96" height="{BADGE_HEIGHT}" fill="url(#s)"/>
  </g>
  <g fill="{TEXT_COLOR}" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110">
    <g transform="scale(.1)">
      <g aria-hidden="true" fill="#010101">
        <text x="285" y="150" fill-opacity=".8" filter="url(#blur)" textLength="450">{LABEL_TEXT}</text>
        <text x="285" y="150" fill-opacity=".3" textLength="450">{LABEL_TEXT}</text>
      </g>
      <text x="285" y="140" textLength="450">{LABEL_TEXT}</text>
    </g>
    <g transform="scale(.1)">
      <g aria-hidden="true" fill="#010101">
        <text x="745" y="150" fill-opacity=".8" filter="url(#blur)" textLength="310">{right_text}</text>
        <text x="745" y="150" fill-opacity=".3" textLength="310">{right_text}</text>
      </g>
      <text x="745" y="140" textLength="310">{right_text}</text>
    </g>
  </g>
</svg>'''

# 保存为SVG文件
with open("badge.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)  <linearGradient id="s" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <clipPath id="r">
    <rect width="96" height="20" rx="3"/>
  </clipPath>
  <g clip-path="url(#r)">
    <rect width="55" height="20" fill="{LEFT_BG_COLOR}"/>
    <rect x="55" width="41" height="20" fill="{RIGHT_BG_COLOR}"/>
    <rect width="96" height="20" fill="url(#s)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110">
    <g transform="scale(.1)">
      <g aria-hidden="true" fill="#010101">
        <text x="285" y="150" fill-opacity=".8" filter="url(#blur)" textLength="450">{LABEL_TEXT}</text>
        <text x="285" y="150" fill-opacity=".3" textLength="450">{LABEL_TEXT}</text>
      </g>
      <text x="285" y="140" textLength="450">{LABEL_TEXT}</text>
    </g>
    <g transform="scale(.1)">
      <g aria-hidden="true" fill="#010101">
        <text x="745" y="150" fill-opacity=".8" filter="url(#blur)" textLength="310">{right_text}</text>
        <text x="745" y="150" fill-opacity=".3" textLength="310">{right_text}</text>
      </g>
      <text x="745" y="140" textLength="310">{right_text}</text>
    </g>
  </g>
</svg>'''

# 保存为图片文件
with open("badge.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("badge.svg 已成功生成")        font-size="{FONT_SIZE}" 
        fill="{TEXT_COLOR}" 
        text-anchor="middle">
    {display_text}
  </text>
</svg>'''

# 保存为图片文件
with open("badge.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)  <linearGradient id="s" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <clipPath id="r">
    <rect width="96" height="20" rx="3"/>
  </clipPath>
  <g clip-path="url(#r)">
    <rect width="55" height="20" fill="{LEFT_BG_COLOR}"/>
    <rect x="55" width="41" height="20" fill="{RIGHT_BG_COLOR}"/>
    <rect width="96" height="20" fill="url(#s)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110">
    <g transform="scale(.1)">
      <g aria-hidden="true" fill="#010101">
        <text x="285" y="150" fill-opacity=".8" filter="url(#blur)" textLength="450">{LABEL_TEXT}</text>
        <text x="285" y="150" fill-opacity=".3" textLength="450">{LABEL_TEXT}</text>
      </g>
      <text x="285" y="140" textLength="450">{LABEL_TEXT}</text>
    </g>
    <g transform="scale(.1)">
      <g aria-hidden="true" fill="#010101">
        <text x="745" y="150" fill-opacity=".8" filter="url(#blur)" textLength="310">{right_text}</text>
        <text x="745" y="150" fill-opacity=".3" textLength="310">{right_text}</text>
      </g>
      <text x="745" y="140" textLength="310">{right_text}</text>
    </g>
  </g>
</svg>'''

# 保存为图片文件
with open("badge.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("badge.svg 已成功生成")        font-size="{FONT_SIZE}" 
        fill="{TEXT_COLOR}" 
        text-anchor="middle">
    {display_text}
  </text>
</svg>'''

# 保存为图片文件
with open("badge.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)        font-size="{FONT_SIZE}" 
        fill="{TEXT_COLOR}" 
        text-anchor="middle">
    {display_text}
  </text>
</svg>'''

# 保存为图片文件
with open("badge.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
