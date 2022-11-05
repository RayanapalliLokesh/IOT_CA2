from time import sleep
from rpi_lcd import LCD

lcd = LCD()

while True:
	try:
		lcd.text("Good Morning ",1,2)
		lcd.text("LPU",2,3)
		sleep(3)
		
		lcd.clear()
		sleep(1)
	except KeyboardInterrupt:
		
		lcd.clear()
		lcd.text("Good Afternoon ",1,2)
		lcd.text("LPU",2,3)
		sleep(3)
			
