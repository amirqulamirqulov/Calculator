import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.fin_nums = []
        self.fin_nums1 = ""
        self.result_field.setText("0")
        self.showNormal()

    
    def keypad(self):
        contanier = qtw.QWidget()
        contanier.setLayout(qtw.QGridLayout())


        self.result_field = qtw.QLineEdit()
        btn_enter = qtw.QPushButton("Enter", clicked = self.func_result)
        btn_clear = qtw.QPushButton("Clear", clicked = self.clear_calc)
        btn_1 = qtw.QPushButton("1", clicked = lambda: self.num_press("1"))
        btn_2 = qtw.QPushButton("2", clicked = lambda: self.num_press("2"))
        btn_3 = qtw.QPushButton("3", clicked = lambda: self.num_press("3"))
        btn_4 = qtw.QPushButton("4", clicked = lambda: self.num_press("4"))
        btn_5 = qtw.QPushButton("5", clicked = lambda: self.num_press("5"))
        btn_6 = qtw.QPushButton("6", clicked = lambda: self.num_press("6"))
        btn_7 = qtw.QPushButton("7", clicked = lambda: self.num_press("7"))
        btn_8 = qtw.QPushButton("8", clicked = lambda: self.num_press("8"))
        btn_9 = qtw.QPushButton("9", clicked = lambda: self.num_press("9"))
        btn_0 = qtw.QPushButton("0", clicked = lambda: self.num_press("0"))
        btn_point = qtw.QPushButton(".", clicked = lambda: self.point_press("."))
        btn_plus = qtw.QPushButton("+", clicked = lambda: self.func_press("+"))
        btn_minus = qtw.QPushButton("-", clicked = lambda: self.func_press("-"))
        btn_mult = qtw.QPushButton("*", clicked = lambda: self.func_press("*"))
        btn_divd = qtw.QPushButton("/", clicked = lambda: self.func_press("/"))
        btn_back = qtw.QPushButton("<-", clicked = lambda: self.onback())


        contanier.layout().addWidget(self.result_field, 0, 0, 1, 4)
        contanier.layout().addWidget(btn_clear, 1, 0, 1, 2)
        contanier.layout().addWidget(btn_enter, 1, 2, 1, 2)
        contanier.layout().addWidget(btn_9, 2, 0, 1, 1)
        contanier.layout().addWidget(btn_8, 2, 1, 1, 1)
        contanier.layout().addWidget(btn_7, 2, 2, 1, 1)
        contanier.layout().addWidget(btn_plus, 2, 3, 1, 1)
        contanier.layout().addWidget(btn_6, 3, 0, 1, 1)
        contanier.layout().addWidget(btn_5, 3, 1, 1, 1)
        contanier.layout().addWidget(btn_4, 3, 2, 1, 1)
        contanier.layout().addWidget(btn_minus, 3, 3, 1, 1)
        contanier.layout().addWidget(btn_3, 4, 0, 1, 1)
        contanier.layout().addWidget(btn_2, 4, 1, 1, 1)
        contanier.layout().addWidget(btn_1, 4, 2, 1, 1)
        contanier.layout().addWidget(btn_mult, 4, 3, 1, 1)
        contanier.layout().addWidget(btn_0, 5, 1, 1, 1)
        contanier.layout().addWidget(btn_point, 5, 2, 1, 1)
        contanier.layout().addWidget(btn_back, 5, 0, 1, 1)
        contanier.layout().addWidget(btn_divd, 5, 3, 1, 1)
        self.layout().addWidget(contanier)

    def num_press(self, key_number):
        self.temp_nums.append(key_number)
        if self.temp_nums[0] == "0" and key_number != "0" and (not("." in self.temp_nums)):
            self.temp_nums = []
            self.temp_nums[0] = f"{key_number}"
        if self.temp_nums[0] == "0" and key_number == "0":
            self.temp_nums = []
            return
        temp_string = "".join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText("".join(self.fin_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)

    def point_press(self, key_number):
        if key_number in self.temp_nums:
            pass
        else:
            if self.temp_nums == []:
                self.temp_nums = ["0"]
            self.temp_nums.append(key_number)
            temp_string = "".join(self.temp_nums)
            if self.fin_nums:
                self.result_field.setText("".join(self.fin_nums) + temp_string)
            else:
                self.result_field.setText(temp_string)


    def func_press(self, operator):
        temp_string = "".join(self.temp_nums)
        self.fin_nums.append(temp_string)
        if self.fin_nums == [""] and self.fin_nums1 != "":
            self.fin_nums.append(self.fin_nums1) 
        if self.temp_nums == [] and self.fin_nums != [""]:
            self.fin_nums.remove(self.fin_nums[-2])
            self.fin_nums.append(operator)
        elif self.temp_nums == [] and self.fin_nums == [""]:
            self.temp_nums = []
            self.fin_nums = []
            return
        else:
            self.fin_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText("".join(self.fin_nums))

    def func_result(self):
        fin_string = "".join(self.fin_nums) + "".join(self.temp_nums)
        result_string = eval(fin_string)
        if result_string - int(result_string) == 0:
            result_string = int(result_string)
        fin_string = str(round(result_string, 5))
        self.fin_nums1 = fin_string
        self.fin_nums = []
        self.temp_nums = []
        self.result_field.setText(fin_string)

    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []
        self.fin_nums1 = ""
        self.result_field.setText("0")

    def onback(self):
       
        satr = self.result_field.text()
        if  satr == "0":
            pass
        elif self.temp_nums != []:
            satr = satr[:-1]
            self.temp_nums.remove(self.temp_nums[-1])
            self.result_field.setText(satr)
            if satr == "":
                self.result_field.setText("0")
        else:
            satr = satr[:-1]
            self.result_field.setText(satr)
            if satr == "":
                self.result_field.setText("0")
            


app = qtw.QApplication([])
app.setStyle(qtw.QStyleFactory.create("Fucion"))
mw = MainWindow()
mw.showNormal()
app.exec_()