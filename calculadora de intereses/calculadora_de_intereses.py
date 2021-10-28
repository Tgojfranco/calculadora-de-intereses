#Joel Franco Muñoz CALCULADORA DE DEUDA

T1= "Favor de introducir su "


Card_Name = input("{} Nombre de la Tarjeta: ".format(T1))
Interes_Rate = float(input("{} Tasa de interes: ".format(T1)))
Debt = float(input("{} Deuda: ".format(T1)))
Pay = float(input("{} Pago a realizar: ".format(T1)))
New_Charges = float(input("{} Nuevos cargos: ".format(T1)))
Monthly_Interest = float(Interes_Rate/12)
Recalculated_Deb = float((Debt-Pay)*(1+Monthly_Interest))
New_Debt = float(Recalculated_Deb + New_Charges)
while True:
    if Pay > Debt:
        print("El pago no puede superar el total de la deuda, favor de introducir un nuevo valor de pago")
        Pay = input("{} Pago a realizar: ".format(T1))
        print("\n\n                     RESUMEN \n\nNombre de la Tarjeta: {CN} \nTasa de interes: {IR} \nDeuda: {D} \nPago a realizar: {P} \nNuevos cargos: {NC} ".format(CN=Card_Name,IR=Interes_Rate,D=Debt,P=Pay,NC= New_Charges))
        print("Interes Mensual: {MI} \nDeuda Recalculada: {RD} \nNueva Deuda: {ND}".format(MI=Monthly_Interest, RD=Recalculated_Deb, ND=New_Debt))
        break
    else:
        print("\n\n                     RESUMEN \n\nNombre de la Tarjeta: {CN} \nTasa de interes: {IR} \nDeuda: {D} \nPago a realizar: {P} \nNuevos cargos: {NC} ".format(CN=Card_Name,IR=Interes_Rate,D=Debt,P=Pay,NC= New_Charges))
        print("Interes Mensual: {MI} \nDeuda Recalculada: {RD} \nNueva Deuda: {ND}".format(MI=Monthly_Interest, RD=Recalculated_Deb, ND=New_Debt))
        break