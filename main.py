import rumps
import ducoapi
from currency_converter import CurrencyConverter
import time
import os
import rumps



    def run(self):
        self.app.run()

    def duco():
        count = 0

        while count < 5:

            time.sleep(0)
            c = CurrencyConverter(decimal=False)


            api_connection = ducoapi.api_actions()

            api_connection.login(username='tsournia', password='bruh')

            current_balance = api_connection.balance()

            ducodollardprice = ducoapi.get_duco_price()
            print('duco dollard price',ducodollardprice,"$")
            eur = c.convert(ducodollardprice, 'USD', 'EUR')
            #c.convert(price, 'EUR', 'USD') # doctest: +SKIP
            print('duco euro price',eur,'€')

            #balance en € de l'utilisateur
            #on arondit a deux chiffres apres la virgule pour la valeur en euro
            userbalance = float(current_balance)*float(eur);
            userbalance2 = round(userbalance,2)
            #on converti current_balance en float puis on arondi a 4 chiffres apres la virgule
            floatbalance = float(current_balance)
            floatbalance4 = round(floatbalance,4)



            print(floatbalance,"ᕲ")

            #affichage
            print( 'TSOURNIAs BALANCE :',floatbalance4,'ᕲ','≈',userbalance2,'euro')
            print("=============================================================")


            api_connection.close()
            time.sleep(5)



if __name__ == '__main__':
    app.run()
    duco()
