def horas_e_minutos(minutos):
    h = minutos // 60
    m = minutos % 60
    s = minutos // 60
    return "%d:%d:%d" % (h, m, s)

print(horas_e_minutos(876))