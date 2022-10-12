add = '+'
minus = '-'
times = '*'
div = '/'
oper_list = [add, minus, times, div]
memory = 0.0
mssg = ["Enter an equation\n",
       "Do you even know what numbers are? Stay focused!",
       "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
       "Yeah... division by zero. Smart move...",
       "Do you want to store the result? (y / n):",
       "Do you want to continue calculations? (y / n):",
       " ... lazy",
       " ... very lazy",
       " ... very, very lazy",
       "You are",
       "Are you sure? It is only one digit! (y / n)",
       "Don't be silly! It's just one number! Add to the memory? (y / n)",
       "Last chance! Do you really want to embarrass yourself? (y / n)"]

def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) is True and is_one_digit(v2) is True:
        msg += mssg[6]
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += mssg[7]
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += mssg[8]
    if msg != '':
        msg = mssg[9] + msg
    else:
        pass
    print(msg)

def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer():
        return True
    return False


while True:
    print(mssg[0])
    calc = input()
    x, oper, y = calc.split(' ')

    if x == 'M':
        x = memory
    if y == 'M':
        y = memory

    try:
        x, y = float(x), float(y)
    except ValueError:
        print(mssg[1])
        continue

    if oper not in oper_list:
        print(mssg[2])
        continue
    check(x, y, oper)
    if oper == add:
        result = x + y
    elif oper == minus:
        result = x - y
    elif oper == times:
        result = x * y
    elif oper == div and y != 0:
        result = x / y
    else:
        print(mssg[3])
        continue

    print(result)
    print(mssg[4])
    if input() == "n":
        memory = 0
    else:
        if result > -10 and result < 10 and result.is_integer():
            msg_index = 10
            while True:
                print(mssg[msg_index])
                answer = input()
                if answer == 'y':
                    if msg_index < 12:
                        msg_index = msg_index + 1
                    else:
                        memory = result
                        break
                else:
                    break
        else:
            memory = result
    print(mssg[5])
    if input() == 'y':
        pass
    else:
        break
