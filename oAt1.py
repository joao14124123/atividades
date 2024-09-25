class vazio:
    ligarMotor = ""
    desligarMotor = "desligado"
    andar = "status"
    parar = "status"
    
    def ligarmotor(self):
        self.ligarMotor = "ligado" 
        print(self.ligarMotor)
    
    def desligarrmotor(self):
        self.desligarMotorMotor = "desligado" 
        print(self.desligarMotorMotor)
    
    def andarr(self):
        self.andar = "em movimento" 
        print(self.andar)
    
    def pararr(self):
        self.parar = "parado" 
        print(self.parar)






st1 = vazio()
st1.ligarmotor()
st1.desligarrmotor()
st1.andarr()
st1.pararr()