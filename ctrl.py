class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()
        
    def calculate(self):
        num1 = float(self.view.le1.text()) # 첫 번째 라인 에디트에 입력된 숫자를 읽어옴
        num2 = float(self.view.le2.text()) # 두 번째 라인 에디트에 입력된 숫자를 읽어옴
        operator = self.view.cb.currentText() # 콤보 박스에서 선택된 연산자를 읽어옴

        if operator == '+':
            return f'{num1} + {num2} = {self.sum(num1, num2)}'
        else:
            return "Calculation Error"
        
    
    def connectSignals(self): # btn1을 클릭하면 calculate 함수를 호출하여 결과를 메시지로 표시
        self.view.btn1.clicked.connect(lambda: self.view.setDisplay(self.calculate())) # 버튼 클릭 시 계산 결과를 메시지로 표시
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(self, a, b): # 예외 처리 제거 : 향후 calculate 함수에서 처리하도록 구현 예정
            return str(a+b)
