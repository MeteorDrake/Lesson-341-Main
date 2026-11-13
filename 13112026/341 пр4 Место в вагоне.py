print("Введите своё место в вагоне")
place_in_train = int(input())
seats_in_compartment = 4
compartment_in_train = (place_in_train//seats_in_compartment)
if place_in_train>0 and place_in_train<=36:
    if place_in_train%4 == 0:
        print("Ваше купе:",compartment_in_train)
    else:
        print("Ваше купе:",(compartment_in_train)+1)
else:
    print("Введенно неверное место, место должно быть больше 0 и не больше максимального количества мест в вагоне")
