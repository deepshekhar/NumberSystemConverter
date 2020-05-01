from tkinter import *
import tkinter.font as tkFont

# global variable
expression1 = ""
expression2 = ""

# function to update expression in the text entry box


def press(num):

    global expression1  # point out the global variable
    expression1 = expression1 + str(num)  # concatination
    equation1.set(expression1)  # update the expression
    label.configure(text="Enter digits LESS THAN the BASE NUMBER.",fg="#FF5733", bg="#E6E6E6")
    label.after(3000, lambda: label.configure(text = ""))

# function to clear pevious expressions.

def clear():

    global expression1
    global expression2
    expression1 = ""
    expression2 = ""
    equation1.set("")
    equation2.set("")
    label.configure(text="Record Cleared", fg="#075632", bg="#E6E6E6")
    label.after(3000, lambda: label.configure(text=""))

def reset():

    global expression1
    global expression2
    expression1 = ""
    expression2 = ""
    equation1.set("")
    equation2.set("")
    variable1.set(OptionList1[0])
    variable2.set(OptionList2[0])
    label.configure(text="Reset Done...", fg="#075632", bg="#E6E6E6")
    label.after(3000, lambda: label.configure(text=""))


# function to run when Convert button is clicked.
def Convert():

    # Here Binary to Binary conversion will Happen.
    if variable1.get() == OptionList1[0] and variable2.get() == OptionList2[0]:
        label.configure(text="Error! Choose Different Option",fg="#FF5733", bg="#E6E6E6")
        label.after(3000, lambda: label.configure(text = ""))

    # Here Binary to Octal conversion will Happen.
    elif variable1.get() == OptionList1[0] and variable2.get() == OptionList2[1]:
        BinaryToOctal()
    # Here Binary to Decimal conversion will Happen.
    elif variable1.get() == OptionList1[0] and variable2.get() == OptionList2[2]:
        BinaryToDecimal()
    # Here Binary to Hexa decimal conversion will Happen.
    elif variable1.get() == OptionList1[0] and variable2.get() == OptionList2[3]:
        BinaryToHexa()

    # Here Octal to Binary conversion will Happen.
    elif variable1.get() == OptionList1[1] and variable2.get() == OptionList2[0]:
        OctalToBinary()
    # Here Octal to Octal conversion will Happen.
    elif variable1.get() == OptionList1[1] and variable2.get() == OptionList2[1]:
        label.configure(text="Error! Choose Different Option",fg="#FF5733", bg="#E6E6E6")
        label.after(3000, lambda: label.configure(text = ""))

    # Here Octal to decimal conversion will Happen.
    elif variable1.get() == OptionList1[1] and variable2.get() == OptionList2[2]:
        OctalToDecimal()
    # Here Octal to HexaDecimal conversion will Happen.
    elif variable1.get() == OptionList1[1] and variable2.get() == OptionList2[3]:
        binarynum = OctalToBinary()
        my_list1 = []
        if binarynum == 0:
            expression2 = str(binarynum)
            equation2.set(expression2)
        else:
            while binarynum:
                lastfournum = binarynum % 10000
                value = BitoDe(lastfournum) # binary to decimal temporary function calling
                binarynum = int(binarynum / 10000)
                my_list1.append(value)

            my_list1.reverse()
            my_string = "".join([str(elem) for elem in my_list1])
            expression2 = my_string
            equation2.set(expression2)

    # Here Decimal to Binary conversion will Happen.
    elif variable1.get() == OptionList1[2] and variable2.get() == OptionList2[0]:
        DecimalToBinary()
    # Here Decimal to Octal conversion will Happen.
    elif variable1.get() == OptionList1[2] and variable2.get() == OptionList2[1]:
        DecimalToOctal()
    # Here Decimal to Decimal conversion will Happen.
    elif variable1.get() == OptionList1[2] and variable2.get() == OptionList2[2]:
        label.configure(text="Error! Choose Different Option",fg="#FF5733", bg="#E6E6E6")
        label.after(3000, lambda: label.configure(text = ""))
    # Here Decimal to Hexa decimal conversion will Happen.
    elif variable1.get() == OptionList1[2] and variable2.get() == OptionList2[3]:
        DecimalToHexa()

    # Here Hexa decimal to Binary conversion will Happen.
    elif variable1.get() == OptionList1[3] and variable2.get() == OptionList2[0]:
        HexaToBinary()
    # Here Hexa decimal to Octal conversion will Happen.
    elif variable1.get() == OptionList1[3] and variable2.get() == OptionList2[1]:
        binFromHexa = HexaToBinary()
        octal = 0
        i = 1
        num = int(binFromHexa)
        while num:
            lastThreenum = num % 1000
            value = BtoD(lastThreenum) # here the BtoD temporary function is used.
            num = int(num / 1000)
            octal += value * i
            i = i * 10
        expression2 = str(octal)
        equation2.set(expression2)


    # Here Hexa decimal to Decimal conversion will Happen.
    elif variable1.get() == OptionList1[3] and variable2.get() == OptionList2[2]:
        HexaToDecimal()
    # Here Hexa decimal to Hexa decimal conversion will Happen.
    elif variable1.get() == OptionList1[3] and variable2.get() == OptionList2[3]:
        label.configure(text="Error! Choose Different Option",fg="#FF5733", bg="#E6E6E6")
        label.after(3000, lambda: label.configure(text = ""))
    else:
        from tkinter import messagebox
        messagebox.showinfo("Error!", "Choose Correct Option")


# this function is used in Binary to octal converter function
def BtoD(lastThreenum):

    i = 0
    number = 0
    num = int(lastThreenum)
    while num:
        lastdigit = num % 10
        num = int(num / 10)
        number += lastdigit * 2 ** i
        i += 1
    return number

# this function is used in binary to hexa converter.
def BitoDe(lastfournum):

    i = 0
    number = 0
    num = int(lastfournum)
    while num:
        lastdigit = num % 10
        num = int(num / 10)
        number += lastdigit * 2 ** i
        i += 1

    if number == 10:
        number = "A"
    elif number == 11:
        number = "B"
    elif number == 12:
        number = "C"
    elif number == 13:
        number = "D"
    elif number == 14:
        number = "E"
    elif number == 15:
        number = "F"

    return number

def BinaryToOctal():

    octal = 0
    i = 1
    num = int(expression1)
    while num:
        lastThreenum = num % 1000
        value = BtoD(lastThreenum)
        num = int(num / 1000)
        octal += value * i
        i = i * 10
    expression2 = str(octal)
    equation2.set(expression2)
    label.configure(text="Completed.", fg="#075632", bg="#E6E6E6")
    label.after(3000, lambda: label.configure(text=""))

def BinaryToDecimal():

    i = 0  # variable which helps to continue the loop
    number = 0
    num = int(expression1) # Here i Convert string number to an integer.
    while num:  # while loop starts. condition provided tempnum != 0
        lastdigit = num % 10  # here i get the last digit of the number to perform (1 x 2 power i)
        num = int(num / 10)  # Here i update the number variable for the next iteration.
        # if u notice that here i typecast the tempnum into int though it was integer type, because in
        # python 11/10(as a example) gives result in float type and i need the result in integer type so.
        number += lastdigit * 2 ** i
        i += 1
    expression2 = str(number)
    equation2.set(expression2)
    label.configure(text = "Completed.", fg="#075632", bg="#E6E6E6")
    label.after(3000, lambda: label.configure(text=""))

def BinaryToHexa():

    global expression2
    my_list1 = []
    num = int(expression1)
    if num == 0:
        expression2 = str(num)
        equation2.set(expression2)
    else:
        while num:
            lastfournum = num % 10000
            value = BitoDe(lastfournum)
            num = int(num / 10000)
            my_list1.append(value)

        my_list1.reverse()
        my_string = "".join([str(elem) for elem in my_list1])
        expression2 = my_string
        equation2.set(expression2)
        label.configure(text="Completed.", fg="#075632", bg="#E6E6E6")
        label.after(3000, lambda: label.configure(text=""))


def OctalToBinary():

    global expression2
    value = 0
    num = int(expression1)  # store string as a integer.
    my_list = []  # creating an empty list.
    if num == 0:
        expression2 = str(num)
        equation2.set(expression2)
    else:
        while num:
            lastdigit = num % 10
            num = int(num / 10)
            if lastdigit == 0:
                value = "000"
            elif lastdigit == 1:
                value = "001"
            elif lastdigit == 2:
                value = "010"
            elif lastdigit == 3:
                value = "011"
            elif lastdigit == 4:
                value = "100"
            elif lastdigit == 5:
                value = "101"
            elif lastdigit == 6:
                value = "110"
            elif lastdigit == 7:
                value = "111"
            else:
                from tkinter import messagebox
                messagebox.showinfo("Error!", "Enter an octal number.")
            my_list.insert(0, value)

        my_string = "".join([str(elem) for elem in my_list])
        expression2 = my_string

        if variable1.get() == OptionList1[1] and variable2.get() == OptionList2[3]:
            return int(expression2)   # Here if part is use for octal to binary conversion for binary to hex
        else:
            equation2.set(expression2)
            label.configure(text="Completed.", fg="#075632", bg="#E6E6E6")
            label.after(3000, lambda: label.configure(text=""))

def OctalToDecimal():

    i = 0  # variable which helps to continue the loop
    number = 0
    num = int(expression1)  # Here i Convert string number to an integer.
    while num:  # while loop starts. condition provided tempnum != 0
        lastdigit = num % 10  # here i get the last digit of the number to perform (1 x 2 power i)
        num = int(num / 10)  # Here i update the number variable for the next iteration.
        # if u notice that here i typecast the tempnum into int though it was integer type, because in
        # python 11/10(as a example) gives result in float type and i need the result in integer type so.
        number += lastdigit * 8 ** i
        i += 1
    expression2 = str(number)
    equation2.set(expression2)
    label.configure(text="Completed.", fg="#075632", bg="#E6E6E6")
    label.after(3000, lambda: label.configure(text=""))

# def OctalToHexa(): this function is not used.

def DecimalToBinary():

    global expression2
    num = int(expression1)  # store string as a integer.
    my_list = []  # creating an empty list.

    if num == 0:
        expression2 = str(num)
        equation2.set(expression2)
    else:
        while num != 0:
            my_list.append(num % 2)
            num = num // 2  # this is floor division.
        my_list.reverse()
        my_string = "".join([str(elem) for elem in my_list])
        expression2 = my_string
        equation2.set(expression2)
        label.configure(text="Completed.", fg="#075632", bg="#E6E6E6")
        label.after(3000, lambda: label.configure(text=""))

def DecimalToOctal():

    global expression2
    num = int(expression1)  # store string as a integer.
    my_list = []  # creating an empty list.
    if num == 0:
        expression2 = str(num)
        equation2.set(expression2)
    else:
        while num != 0:
            my_list.append(num % 8)
            num = num // 8  # this is floor division.
        my_list.reverse()
        my_string = "".join([str(elem) for elem in my_list])
        expression2 = my_string
        equation2.set(expression2)
        label.configure(text="Completed.", fg="#075632", bg="#E6E6E6")
        label.after(3000, lambda: label.configure(text=""))

def DecimalToHexa():

    global expression2
    num = int(expression1)  # store string as a integer.
    my_list = []  # creating an empty list.
    if num == 0:
        expression2 = str(num)
        equation2.set(expression2)
    else:
        while num != 0:
            ele = num % 16
            if ele == 10:
                ele = "A"
            elif ele == 11:
                ele = "B"
            elif ele == 12:
                ele = "C"
            elif ele == 13:
                ele = "D"
            elif ele == 14:
                ele = "E"
            elif ele == 15:
                ele = "F"
            my_list.append(ele)
            num = num // 16  # this is floor division.
        my_list.reverse()
        my_string = "".join([str(elem) for elem in my_list])
        expression2 = my_string
        equation2.set(expression2)
        label.configure(text="Completed.", fg="#075632", bg="#E6E6E6")
        label.after(3000, lambda: label.configure(text=""))


def HexaToBinary():

    listOfnumber = list(expression1)
    length = len(listOfnumber)
    my_list = []
    value = ""
    for i in range(length):
        if listOfnumber[i] == "0":
            value = "0000"
        elif listOfnumber[i] == "1":
            value = "0001"
        elif listOfnumber[i] == "2":
            value = "0010"
        elif listOfnumber[i] == "3":
            value = "0011"
        elif listOfnumber[i] == "4":
            value = "0100"
        elif listOfnumber[i] == "5":
            value = "0101"
        elif listOfnumber[i] == "6":
            value = "0110"
        elif listOfnumber[i] == "7":
            value = "0111"
        elif listOfnumber[i] == "8":
            value = "1000"
        elif listOfnumber[i] == "9":
            value = "1001"
        elif listOfnumber[i] == "A":
            value = "1010"
        elif listOfnumber[i] == "B":
            value = "1011"
        elif listOfnumber[i] == "C":
            value = "1100"
        elif listOfnumber[i] == "D":
            value = "1101"
        elif listOfnumber[i] == "E":
            value = "1110"
        elif listOfnumber[i] == "F":
            value = "1111"
        else:
            from tkinter import messagebox
            messagebox.showinfo("Error!", "Enter an octal number.")
        my_list.append(value)
    my_string = "".join([str(elem) for elem in my_list])
    expression2 = my_string
    if variable1.get() == OptionList1[3] and variable2.get() == OptionList2[1]:
        return expression2
    else:
        equation2.set(expression2)
        label.configure(text="Completed.", fg="#075632", bg="#E6E6E6")
        label.after(3000, lambda: label.configure(text=""))

def HexaToDecimal():

    listOfnumber = list(expression1)
    length = len(listOfnumber)
    listOfnumber.reverse()
    number = 0
    for i in range(length):
        if listOfnumber[i] == "0":
            lastdigit = 0
            number += lastdigit * 16 ** i

        elif listOfnumber[i] == "1":
            lastdigit = 1
            number += lastdigit * 16 ** i

        elif listOfnumber[i] == "2":
            lastdigit = 2
            number += lastdigit * 16 ** i

        elif listOfnumber[i] == "3":
            lastdigit = 3
            number += lastdigit * 16 ** i

        elif listOfnumber[i] == "4":
            lastdigit = 4
            number += lastdigit * 16 ** i

        elif listOfnumber[i] == "5":
            lastdigit = 5
            number += lastdigit * 16 ** i

        elif listOfnumber[i] == "6":
            lastdigit = 6
            number += lastdigit * 16 ** i

        elif listOfnumber[i] == "7":
            lastdigit = 7
            number += lastdigit * 16 ** i

        elif listOfnumber[i] == "8":
            lastdigit = 8
            number += lastdigit * 16 ** i

        elif listOfnumber[i] == "9":
            lastdigit = 9
            number += lastdigit * 16 ** i

        elif listOfnumber[i] == "A":
            lastdigit = 10
            number += lastdigit * 16 ** i

        elif listOfnumber[i] == "B":
            lastdigit = 11
            number += lastdigit * 16 ** i

        elif listOfnumber[i] == "C":
            lastdigit = 12
            number += lastdigit * 16 ** i

        elif listOfnumber[i] == "D":
            lastdigit = 13
            number += lastdigit * 16 ** i

        elif listOfnumber[i] == "E":
            lastdigit = 14
            number += lastdigit * 16 ** i

        elif listOfnumber[i] == "F":
            lastdigit = 15
            number += lastdigit * 16 ** i

    expression2 = str(number)
    equation2.set(expression2)
    label.configure(text="Completed.", fg="#075632", bg="#E6E6E6")
    label.after(3000, lambda: label.configure(text=""))

OptionList1 = ["Binary", "Octal", "Decimal", "Hexadecimal"]
OptionList2 = ["Binary", "Octal", "Decimal", "Hexadecimal"]

mwindow = Tk()

mwindow.title("SysCal")
mwindow.geometry("612x390")
mwindow.configure(bg="#E4E4E4")

frame1 = Frame(mwindow, bg="#E4E4E4",)
frame1.grid(row=0, column=1, columnspan=2, pady=20, padx=50)

variable1 = StringVar()
variable1.set(OptionList1[0])
OptionMenu1 = OptionMenu(frame1, variable1, *OptionList1)
OptionMenu1.config(width=14, font=('fangsongti', 10), bd=1, bg="#DDDDDD" )
OptionMenu1.grid(row=1, column=0, padx=20)

equation1 = StringVar()
equation1.set("")
expression_field1 = Entry(frame1, textvariable=equation1, width=25, bd = 1, bg="#EBF7FE")
expression_field1.grid(row=2, column=0, columnspan=6, pady=15)


frame2 = Frame(mwindow, bg="#E4E4E4",)
frame2.grid(row=0, column=4, columnspan=2, padx=50, pady=20)

variable2 = StringVar()
variable2.set(OptionList2[0])
OptionMenu2 = OptionMenu(frame2, variable2, *OptionList2)
OptionMenu2.config(width=14, font=('fangsongti', 10), bd=1, bg="#DDDDDD")
OptionMenu2.grid(row=1, column=0, padx=20)

equation2 = StringVar()
equation2.set("")
resultlabel = Label(frame2, textvariable=equation2, width=25, bg="#EBF7FE")
resultlabel.grid(row=2, column=0, columnspan=6, pady=15)


frame4 = Frame(mwindow)
frame4.grid(row=1, column=0, columnspan=7, padx=0, pady=0)

fontStyle = tkFont.Font(family="papyrus", size=10, weight="bold")
label = Label(frame4, text="WelCome", padx=50, pady=5, fg="#075632", bg="#E6E6E6", font=fontStyle)
label.grid(row=0, column=0, columnspan=7)


frame3 = Frame(mwindow)
frame3.grid(row=3, column=0, columnspan=6, padx=0, pady=20)

button1 = Button(frame3, text="1", command=lambda: press(1), height=1, width=7, background="#04313D",
                 foreground="#FFFFFF", bd="2")
button1.grid(row=1, column=1)

button2 = Button(frame3, text="2", command=lambda: press(2), height=1, width=7, background="#04313D",
                 foreground="#FFFFFF", bd="2")
button2.grid(row=1, column=2)

button3 = Button(frame3, text="3", command=lambda: press(3), height=1, width=7, background="#04313D",
                 foreground="#FFFFFF", bd="2")
button3.grid(row=1, column=3)

button4 = Button(frame3, text="4", command=lambda: press(4), height=1, width=7, background="#04313D",
                 foreground="#FFFFFF", bd="2")
button4.grid(row=1, column=4)

button5 = Button(frame3, text="5", command=lambda: press(5), height=1, width=7, background="#04313D",
                 foreground="#FFFFFF", bd="2")
button5.grid(row=2, column=1)

button6 = Button(frame3, text="6", command=lambda: press(6), height=1, width=7, background="#04313D",
                 foreground="#FFFFFF", bd="2")
button6.grid(row=2, column=2)

button7 = Button(frame3, text="7", command=lambda: press(7), height=1, width=7, background="#04313D",
                 foreground="#FFFFFF", bd="2")
button7.grid(row=2, column=3)

button8 = Button(frame3, text="8", command=lambda: press(8), height=1, width=7, background="#04313D",
                 foreground="#FFFFFF", bd="2")
button8.grid(row=2, column=4)

button9 = Button(frame3, text="9", command=lambda: press(9), height=1, width=7, background="#04313D",
                 foreground="#FFFFFF", bd="2")
button9.grid(row=3, column=1)

button0 = Button(frame3, text="0", command=lambda: press(0), height=1, width=7, background="#04313D",
                 foreground="#FFFFFF", bd="2")
button0.grid(row=3, column=2)

buttonA = Button(frame3, text="A", command=lambda: press("A"), height=1, width=7, background="#04313D",
                 foreground="#FFFFFF", bd="2")
buttonA.grid(row=3, column=3)

buttonB = Button(frame3, text="B", command=lambda: press("B"), height=1, width=7, background="#04313D",
                 foreground="#FFFFFF", bd="2")
buttonB.grid(row=3, column=4)

buttonC = Button(frame3, text="C", command=lambda: press("C"), height=1, width=7, background="#04313D",
                 foreground="#FFFFFF", bd="2")
buttonC.grid(row=4, column=1)

buttonD = Button(frame3, text="D", command=lambda: press("D"), height=1, width=7, background="#04313D",
                 foreground="#FFFFFF", bd="2")
buttonD.grid(row=4, column=2)

buttonE = Button(frame3, text="E", command=lambda: press("E"), height=1, width=7, background="#04313D",
                 foreground="#FFFFFF", bd="2")
buttonE.grid(row=4, column=3)

buttonF = Button(frame3, text="F", command=lambda: press("F"), height=1, width=7, background="#04313D",
                 foreground="#FFFFFF", bd="2")
buttonF.grid(row=4, column=4)

frame5 = Frame(mwindow)
frame5.grid(row=2, column=0, columnspan=7, padx=0, pady=5)

convert = Button(frame5, text="Convert", command=Convert, height=1, width=7, background="#007312",
                 foreground="#FFFFFF", padx=20, bd="1")
convert.grid(row=3, column=5)

Reset = Button(frame5, text="Reset", command= reset, height=1, width=7, bd="1", background="#007B8B",foreground="#FFFFFF")
Reset.grid(row=3, column=2, columnspan=2, padx=5)

clear = Button(frame5, text="Clear", command=clear, height=1, width=7, background="#E60212", foreground="#FFFFFF",
               padx=20, bd="1")
clear.grid(row=3, column=0)

mwindow.mainloop()
