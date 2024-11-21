#fletとmathをインポートする
import flet as ft
import math

#CalcButtonクラスを作成する
class CalcButton(ft.ElevatedButton):
    def __init__(self, text, button_clicked, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand
        self.on_click = button_clicked
        self.data = text

#DigitButtonクラスを作成する
class DigitButton(CalcButton):
    def __init__(self, text, button_clicked, expand=1):
        CalcButton.__init__(self, text, button_clicked, expand)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE

#ActionButtonクラスを作成する
class ActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK

#ExtraActionButtonクラスを作成する
class ExtraActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK

#MemoryButtonクラスを作成する
class MemoryButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK

#ScientificButtonクラスを作成する
class ScientificButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK

#CalculatorAppクラスを作成する
class CalculatorApp(ft.Container):
    def __init__(self):
        super().__init__()

        self.reset()
        self.memory = 0

        #resultプロパティを作成する
        self.result = ft.Text(value="0", color=ft.colors.WHITE, size=20)
        self.width = 500
        self.bgcolor = ft.colors.BLACK
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20
        self.content = ft.Column(
            controls=[
                ft.Row(controls=[self.result], alignment="end"),
                #各ボタンを作成する
                ft.Row(
                    controls=[
                        ScientificButton(text="√", button_clicked=self.button_clicked),
                        ScientificButton(text="log10", button_clicked=self.button_clicked),
                        ScientificButton(text="!", button_clicked=self.button_clicked),
                        ScientificButton(text="x^y", button_clicked=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        MemoryButton(text="MC", button_clicked=self.button_clicked),
                        MemoryButton(text="M+", button_clicked=self.button_clicked),
                        MemoryButton(text="M-", button_clicked=self.button_clicked),
                        MemoryButton(text="MR", button_clicked=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        ExtraActionButton(text="AC", button_clicked=self.button_clicked),
                        ExtraActionButton(text="+/-", button_clicked=self.button_clicked),
                        ExtraActionButton(text="%", button_clicked=self.button_clicked),
                        ActionButton(text="/", button_clicked=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="7", button_clicked=self.button_clicked),
                        DigitButton(text="8", button_clicked=self.button_clicked),
                        DigitButton(text="9", button_clicked=self.button_clicked),
                        ActionButton(text="*", button_clicked=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="4", button_clicked=self.button_clicked),
                        DigitButton(text="5", button_clicked=self.button_clicked),
                        DigitButton(text="6", button_clicked=self.button_clicked),
                        ActionButton(text="-", button_clicked=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="1", button_clicked=self.button_clicked),
                        DigitButton(text="2", button_clicked=self.button_clicked),
                        DigitButton(text="3", button_clicked=self.button_clicked),
                        ActionButton(text="+", button_clicked=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="0", expand=2, button_clicked=self.button_clicked),
                        DigitButton(text=".", button_clicked=self.button_clicked),
                        ActionButton(text="=", button_clicked=self.button_clicked),
                    ]
                ),
            ]
        )

    #ボタンがクリックされたときの処理を行う
    def button_clicked(self, e):
        data = e.control.data
        print(f"Button clicked with data = {data}")
        if data == "AC":
            self.result.value = "0"
            self.reset()
        elif data == "MC":
            self.memory = 0
            print("Memory Cleared")
        elif data == "M+":
            self.memory += float(self.result.value)
            print(f"Memory added: {self.result.value}. Memory: {self.memory}")
        elif data == "M-":
            self.memory -= float(self.result.value)
            print(f"Memory subtracted: {self.result.value}. Memory: {self.memory}")
        elif data == "MR":
            self.result.value = str(self.memory)
            print(f"Memory recalled: {self.memory}")
            self.new_operand = True
        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == "0" or self.new_operand:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data
        elif data in ("+", "-", "*", "/", "x^y"):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = 0
            else:
                self.operand1 = float(self.result.value)
            self.new_operand = True
        elif data == "=":
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.reset()
        elif data == "%":
            self.result.value = float(self.result.value) / 100
            self.reset(False)
        elif data == "+/-":
            if float(self.result.value) > 0:
                self.result.value = "-" + self.result.value
            else:
                self.result.value = self.result.value[1:]
        elif data in ("√", "log10", "!"):
            self.result.value = self.extra_calculate(float(self.result.value), data)
            self.reset()

        self.update()

    #数値を適切な値にフォーマットする
    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    #計算を行う
    def calculate(self, operand1, operand2, operator):
        if operator == "+":
            return self.format_number(operand1 + operand2)
        elif operator == "-":
            return self.format_number(operand1 - operand2)
        elif operator == "*":
            return self.format_number(operand1 * operand2)
        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)
        elif operator == "x^y":
            return self.format_number(operand1 ** operand2)

    #追加の計算を行う
    def extra_calculate(self, operand, operator):
        if operator == "√":
            return self.format_number(math.sqrt(operand))
        elif operator == "log10":
            if operand <= 0:
                return "Error"
            return self.format_number(math.log10(operand))
        elif operator == "!":
            if operand < 0:
                return "Error"
            return math.factorial(int(operand))

    #電卓の状態をリセットする
    def reset(self, full_reset=True):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True

#fletを初期化して電卓のUIを表示する
def main(page: ft.Page):
    page.title = "Calc App"
    calc = CalculatorApp()
    page.add(calc)

#main関数を実行する
ft.app(target=main)