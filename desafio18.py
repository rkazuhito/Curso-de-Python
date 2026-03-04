import math
an=float(input('Informe o ângulo a ser calculado: '))
sin=math.sin(math.radians(an))
cos=math.cos(math.radians(an))
tan=math.tan(math.radians(an))
print('o ângulo {} tem seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(an,sin, cos, tan))