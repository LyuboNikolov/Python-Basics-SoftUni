from math import ceil

from math import floor

number_paint_boxes = int(input())
number_wall_decorations = int(input())
price_gloves = float(input())
price_brush = float(input())

price_paint_box = 21.5
price_wall_decorations = 5.2
number_gloves = ceil(0.35 * number_wall_decorations)
number_brushes = floor(0.48 * number_paint_boxes)

total_price = number_paint_boxes * price_paint_box + number_wall_decorations * price_wall_decorations + \
              number_gloves * price_gloves + number_brushes * price_brush
delivery_price = total_price / 15

print(f"This delivery will cost {delivery_price:.2f} lv.")