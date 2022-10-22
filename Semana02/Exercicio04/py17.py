import datetime

d = datetime.date(2016,7,24) #year,mounth,day -- ele monta uma string de data para voce.
print(d)

tday = datetime.date.today() #retorna a string tear-month-day do dia de hoje
print(tday)
print(tday.year) #pegar so o ano do formato de hoje
print(tday.month) #pegar so o mes do formato de hoje
print(tday.day) #pegar so o dia do formato de hoje
print(tday.weekday()) #segunda = 0 e domingo é 6. Dia da semana.

tdelta = datetime.timedelta(days=7) #diferenca entre dois time stamps
print(tday + tdelta) #somando os dois objetos tempo, ele me mostra string do dia de hoje mais os 7 dias apos
print(tday - tdelta) #7 dias antes...

bday = datetime.date(2022,12,4)
till_bday = bday - tday #Obtendo a diferenca entre o tempo desejado e o de hoje
print(till_bday) #A diferenca
print(till_bday.total_seconds()) #Total em segundos dessa diferenca

t = datetime.time(9,30,45,100000) #hours:minutes:seconds:microseconds
print(t) #o .time controla somente o tempo das horas enquando o date controla somente o dia ano e mes
print(t.hour)

dt = datetime.datetime(2022,10,21,19,52,0,0) # ano, mes, dia, hora, minuto, segundo, microsegundo)
print(dt) #o datetime.datetime controla tudo.
print(dt.date()) #podemos extrair somente a data
print(dt.time()) #podemos extrair somente as horas
print(dt.year) #podemos extrair suas props.

print(dt + tdelta) #Aceita a diferenca de tempo tambem
tdelta = datetime.timedelta(hours=7) 
print(dt + tdelta) #somando mais 7 horas, ele ajusta o dia.



dt_today = datetime.date.today() #retorna o dia e a hora atual
dt_now = datetime.datetime.now() #retorna o dia e a hora atual, porem deixa voce pegar o timezone
dt_utcnow = datetime.datetime.utcnow() 
print(dt_today)
print(dt_now)
print(dt_utcnow)




import pytz #Para trabalhar com maior facilidade em timezones
dt = datetime.datetime(2022,10,21,19,52,0,0, tzinfo= pytz.UTC) #
print(dt)

dt_now = datetime.datetime.now(tz= pytz.UTC) #retorna o dia e a hora atual, porem deixa voce pegar o timezone
print(dt_now) #esse eh menos tiposo.

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo= pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain')) #configurando para uma timezone qualquer
print(dt_mtn)

#for tz in pytz.all_timezones:
#    print(tz) #printando todas as timezones

dt_now = datetime.datetime.now() #Agora (naive), ele sempre retorna na timezone zero. 
timezone_new = pytz.timezone('US/Mountain') #a diferenca timezone
dt_now = timezone_new.localize(dt_now) #pede para elas se ajustarem
print(dt_now) 

#tambem podemos fazer da seguinte forma:
dt_now = datetime.datetime.now(tz=pytz.timezone('Brazil/West')) 
print(dt_now) 

dt_str = 'July 26, 2016'
dt = datetime.datetime.strptime(dt_str,'%B %d, %Y') #string to datetime
print(dt)
