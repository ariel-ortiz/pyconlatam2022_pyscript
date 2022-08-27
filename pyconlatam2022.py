def espita(d):
    """Regresa una lista con los primeros d dígitos
       de pi utilizando el algoritmo de espita
       diseñado por Jeremy Gibbons. Implementación
       de John Zelle con ligeras alteraciones por
       Ariel Ortiz.
       http://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf
    """
    x = []
    q, r, t, k, n, l_ = 1, 0, 1, 1, 3, 3
    while len(x) < d:
        if 4*q+r-t < n*t:
            x.append(n)
            q, r, t, k, n, l_ = (
                10*q, 10*(r-n*t), t, k,
                (10*(3*q+r))//t-10*n, l_)
        else:
            q, r, t, k, n, l_ = (
                q*k, (2*q+r)*l_, t*l_, k+1,
                (q*(7*k+2)+r*l_)//(t*l_), l_+2)
    return x


def agrupa(una_lista):
    """Regresa una cadena formada por renglones, cada
       renglón compuesto por 5 grupos separados por
       espacios, cada grupo con 10 caracteres tomados
       a partir de elementos de una_lista convertidos
       a cadenas de caracteres.
    """
    cadena = ''.join(str(d) for d in una_lista)
    grupos1 = [cadena[i:i+10]
               for i in range(0, len(cadena), 10)]
    grupos2 = [' '.join(grupos1[i:i+5])
               for i in range(0, len(grupos1), 5)]
    return '\n'.join(grupos2)


if __name__ == '__main__':
    print(agrupa(espita(500)))
