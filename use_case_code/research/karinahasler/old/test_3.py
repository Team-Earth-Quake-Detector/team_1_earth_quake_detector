zoom_start_dict = {}

for i in range(0, 19):
    zoom_start_dict[100 + i * 50] = 7.0 - i * 0.1

print(zoom_start_dict[500])
