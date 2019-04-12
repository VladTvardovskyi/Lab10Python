import WaterPump

First_WaterPump = WaterPump.WaterPump(power=100, manufacturer = 'MainBish', value=45, price=150,
                                      weight=1000, colour='orange', height=5)
Second_WaterPump = WaterPump.WaterPump(power=150, manufacturer = 'CACTUS', value=68, price=345,
                                       weight=1500, colour='black', height=9)
Third_WaterPump = WaterPump.WaterPump(power=200, manufacturer = 'Elite_PUMP', value=79, price=567,
                                      weight=1900, colour='grey', height=12)

print(First_WaterPump)
print(Second_WaterPump)
print(Third_WaterPump)