length = 10
width = 5
depth = 2
flow_rate = 3

pool_volume = length * width * depth

if flow_rate > 0:
    time_to_fill = pool_volume / flow_rate
    print(f"Басейн заповниться за {time_to_fill:.2f} хвилин.")
else:
    print("Швидкість подачі води повинна бути більшою за 0.")