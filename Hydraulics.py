import math

from scipy.special import lambertw
gravedad = 9.806

def colebrook(reynolds, diametro, rugosidad):
    a = 2.51 / reynolds
    b = rugosidad / (3.7*diametro)
    p = 1/math.sqrt(10)
    lnp = math.log(p)
    x = -lambertw(-lnp/a * math.pow(p, -b/a))/lnp - b/a
    if x.imag != 0:
        raise ValueError('x is complex')
    f = 1/x.real**2
    return f/4

def propiedades():
    densidad = float(input("Densidad en kg/m3:"))
    viscosidad = float(input("Densidad en cP:"))
    return densidad,viscosidad

def calcular(caudal=None,m=None,diametro=None):
    area = math.pi*diametro**2/4
    densidad,viscosidad = propiedades()
    if caudal is not None and m is None:
        longitud = float(input("Ingrese largo de cañeria: "))
        velocidad = caudal/area
        reynolds = velocidad*diametro*densidad/(viscosidad/1000)
        f = colebrook(reynolds,diametro,0.000046)
        m = 4*f*longitud/diametro*velocidad**2/(2*gravedad)
        return m
    if m is not None and caudal is None:
        longitud = float(input("Ingrese largo de cañeria: "))
        velocidad_old = math.sqrt(m/(0.004*longitud*4)*(2*gravedad*diametro))
        error = 1
        while error > 1e-10:
            velocidad = velocidad_old
            reynolds = velocidad*diametro*densidad/(viscosidad/1000)
            f = colebrook(reynolds,diametro,0.000046)
            velocidad = math.sqrt(m / (f * longitud * 4) * (2 * gravedad*diametro))
            error = velocidad_old - velocidad
            velocidad_old = velocidad
        return velocidad_old*area*3600

def altura(final=None,inicial=None,h = 1):
    if final == None:
        return inicial + h
    else:
        return final - h

def elegir():
    hacer = int(input("Diga que hacer: 1-Altura 2-Caudal:"))
    if hacer == 1:
        caudal = (float(input('Ingrese caudal en m3/h: '))/3600)
        diametro = (float(input('Ingrese diámetro en mm: '))/1000)
        deltap = calcular(caudal ,None, diametro)
        return str(round(deltap,2))+ ' m'
    else:
        deltap = float(input('Ingrese altura en m: '))
        diametro = (float(input('Ingrese diámetro en mm: '))/1000)
        caudal = calcular(None, deltap, diametro)
        return str(round(caudal,2)) + ' m3/h'

def main():
    resultado = elegir()
    print(resultado)

if __name__ == '__main__':
    main()




