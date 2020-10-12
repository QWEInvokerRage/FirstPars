datas = {
    'username': '',
    'password': '',
    'loginbtn': ''
}

def datasGen(datas):
    for key in datas:
        datas[key] = input("Введите"+" " + key+":")

    return datas

datas = datasGen(datas)