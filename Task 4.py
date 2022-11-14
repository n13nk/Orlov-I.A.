from datetime import timedelta
sec = int(input('Введите количество секунд: '))
td1 = str(timedelta(seconds = sec))
hh1, mm1, ss1 = td1.split(":") 
print(f"{sec} секунд в ЧЧ:ММ:СС - {hh1}:{mm1}:{ss1} \n" )

