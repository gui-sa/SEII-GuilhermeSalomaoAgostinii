import RPi.GPIO as GPIO #importando bibliotecas para trabalhar com GPIO do rasp
from flask import Flask, render_template, request #Importando Flask

app = Flask(__name__)

GPIO.setmode(GPIO.BCM) #O referenciamento da GPIO sera por BCM
GPIO.setwarnings(False)

#definindo pinos
senPIR = 16

ledRed = 13
ledYlw = 19
ledGrn = 26

#Inicializa os status como desligado
senPIRSts = 0
ledRedSts = 0
ledYlwSts = 0
ledGrnSts = 0

#Definindo pinos como entrada ou saida
GPIO.setup(senPIR, GPIO.IN)

GPIO.setup(ledRed, GPIO.OUT)   
GPIO.setup(ledYlw, GPIO.OUT) 
GPIO.setup(ledGrn, GPIO.OUT) 
 
GPIO.output(ledRed, GPIO.LOW)
GPIO.output(ledYlw, GPIO.LOW)
GPIO.output(ledGrn, GPIO.LOW)
	
@app.route("/")
def index():
	#LE status da GPIO
	senPIRSts = GPIO.input(senPIR)
	ledRedSts = GPIO.input(ledRed)
	ledYlwSts = GPIO.input(ledYlw)
	ledGrnSts = GPIO.input(ledGrn)

	templateData = {
      'senPIR'  : senPIRSts,
      'ledRed'  : ledRedSts,
      'ledYlw'  : ledYlwSts,
      'ledGrn'  : ledGrnSts,
      }
	return render_template('index.html', **templateData)
	

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	if deviceName == 'ledRed':
		actuator = ledRed
	if deviceName == 'ledYlw':
		actuator = ledYlw
	if deviceName == 'ledGrn':
		actuator = ledGrn
   
	if action == "on":
		GPIO.output(actuator, GPIO.HIGH)
	if action == "off":
		GPIO.output(actuator, GPIO.LOW)
		     
	senPIRSts = GPIO.input(senPIR)
	ledRedSts = GPIO.input(ledRed)
	ledYlwSts = GPIO.input(ledYlw)
	ledGrnSts = GPIO.input(ledGrn)
   
	templateData = {
      'senPIR'  : senPIRSts,
      'ledRed'  : ledRedSts,
      'ledYlw'  : ledYlwSts,
      'ledGrn'  : ledGrnSts,
	}
	return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(debug=True)
