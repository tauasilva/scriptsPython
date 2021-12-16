
import requests
import sched, time
import datetime
s = sched.scheduler(time.time, time.sleep)
url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{:02d}-{:02d}-{}'&$top=100&$format=json"
print('executando consulta / Tempo de espera entre cada consulta: 1 minuto')
def do_getAPI(sc): 
    x = datetime.datetime.now()
    urlGet= url.format(x.month,x.day,x.year)
    request = requests.get(urlGet)
    address_data = request.json()
    print(address_data["value"])

    s.enter(60, 1, do_getAPI, (sc,))
s.enter(60, 1, do_getAPI, (s,))
s.run()