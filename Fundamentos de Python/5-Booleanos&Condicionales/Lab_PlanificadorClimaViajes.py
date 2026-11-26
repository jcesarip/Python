#Para este laboratorio, usarás sentencias condicionales para determinar si es posible desplazarte según el clima, la distancia a recorrer y la disponibilidad de un vehículo.

distance_mi = 0
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = False

if not distance_mi:
    print(False)
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)