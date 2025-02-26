def converte(b, c, d):
    def a(x):
        return b(c(d(x)))
    return a

def dias_em_hora(time):
    return time * 24

def horas_em_minutos(time):
    return time * 60

def minutos_em_segundos(time):
    return time * 60

conversor_dias_para_segundos = converte(minutos_em_segundos, horas_em_minutos, dias_em_hora)

print(conversor_dias_para_segundos(5))