import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

L = 1 #Comprimento do fio
q = 10**(-5) #Carga em Coulombs

#Função para gerar linhas de campo. Retorna linhas para cada ponto em âx e ây ou i e j
def E(lamb, x, y): 
    epsilon = 1*10**(-9)/36*np.pi # valor de ε0
    common = lamb/np.pi*4*(epsilon) #λ/4πε0 
	#formula para ax 
    i = common*(1/np.sqrt((x - 0.5)**2 + y**2) - 1/np.sqrt((x + 0.5)**2 + y**2)) 
	#formula para ay
    j = (common/y)*(-(x-0.5)/np.sqrt((x-0.5)**2 + y**2) + (x + 0.5)/np.sqrt((x + 0.5)**2 + y**2)) 
    return i, j 

nx, ny = 64, 64
#Define o intervalo no eixo X e Y. Ou seja, de -2 até 2. 
#Sendo dividido em 64 partes para cada unidade
x = np.linspace(-2, 2, nx) 
y = np.linspace(-2, 2, ny) 
#Retorna uma matriz de coordenadas vetoriais. 
X, Y = np.meshgrid(x, y) 

#Zera cada ponto das coordenadas na matriz. 
Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx)) 
ex, ey = E(q*L, x=X, y=Y)
Ex += ex
Ey += ey

fig = plt.figure() #INSTANCIANDO OBJETO DE FIGURA
ax = fig.add_subplot(111) #GERANDO FIGURA COM 1 LINHA; 1 COLUNA; 1 INDEX

#PLOTANDO AS LEGENDAS PARA EIXO X E Y
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_aspect('equal')

#PLOTANDO AS LINHAS DE ACORDO DO A FORÇA DO CAMPO NO PONTO EM QUESTÃO
color = 2 * np.log(np.hypot(Ex, Ey)) 
ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=3, arrowstyle='->', arrowsize=1.5)

#Plotando retangulo 
ax.add_artist(Rectangle((-0.5,0), 1, 0.1, 0.0, color='#000800'))
plt.show()