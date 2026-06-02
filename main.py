 


 
 
def mover_servo(angulo):
    pmin = 26
    pmax = 128
 
    calculo = int(pmin + (angulo / 180) * (pmax - pmin))
    servo.duty(calculo)
mover_servo(90)

def mover_servo2(angulo2):
    pmin2 = 26
    pmax2 = 128
 
    calculo2 = int(pmin2 + (angulo2 / 180) * (pmax2 - pmin2))
    servo2.duty(calculo2)
mover_servo2(90)

 
def mover_servo3(angulo3):
    pmin3 = 26
    pmax3 = 128
 
    calculo3 = int(pmin3 + (angulo3 / 180) * (pmax3 - pmin3))
    servo3.duty(calculo3)
mover_servo3(90)



while True:
    if fecha_informatica.value() == 0:
        oled.fill(0)
        oled.text("INFORMATICA", 0, 10)
        oled.text("PORTA FECHADA", 0, 30)
        oled.show()
        led_fecha.on()
        time.sleep(0.15)
        led_fecha.off()
        mover_servo(0)

    if abre_informatica.value() == 0:
        oled.fill(0)
        oled.text("INFORMATICA", 0, 10)
        oled.text("PORTA ABERTA  ", 0, 30)
        oled.show()
        led_abre.on()
        time.sleep(0.15)
        led_abre.off()
        mover_servo(90)

    time.sleep(0.1)

    if fecha_prof.value() == 0:
        oled.fill(0)
        oled.text("PROFESSORES", 0, 10)
        oled.text("PORTA FECHADA", 0, 30)
        oled.show()
        led_fecha.on()
        time.sleep(0.15)
        led_fecha.off()
        mover_servo2(0)

    if abre_prof.value() == 0:
        oled.fill(0)
        oled.text("PROFESSORES", 0, 10)
        oled.text("PORTA ABERTA", 0, 30)
        oled.show()
        led_abre.on()
        time.sleep(0.15)
        led_abre.off()
        mover_servo2(90)

    time.sleep(0.1)

    if fecha_equipamentos.value() == 0:
        oled.fill(0)
        oled.text("ALMOXARIFADO", 0, 10)
        oled.text("PORTA FECHADA", 0, 30)
        oled.show()
        led_fecha.on()
        time.sleep(0.15)
        led_fecha.off()
        mover_servo3(0)

    if abre_equipamentos.value() == 0:
        oled.fill(0)
        oled.text("ALMOXARIFADO", 0, 10)
        oled.text("PORTA ABERTA", 0, 30)
        oled.show()
        led_abre.on()
        time.sleep(0.15)
        led_abre.off()
        mover_servo3(90)

    time.sleep(0.1)