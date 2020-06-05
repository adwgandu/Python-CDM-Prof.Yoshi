
"""# Aula 02 - CDM - 27/03/2020 - Lista 02"""

# Programa Exercicio 02 , Exemplo 01- Matplotlib - Fazer gráficos

#data: 27/03/2020
#Por: Yoshi

import numpy as np #biblioteca do matlab
import pandas as pd # biblioteca  R
import matplotlib.pyplot as plt # biblioteca de graficos


tp = [24.2, 24.6, 23.6, 21.1, 18.9, 16.7, 16.5, 16.9, 17.9, 19.6, 21.3, 23.0]; # criar uma list com 12 várias variáveis (temp média de floripa)

tp2 = np.array(tp); # converto minha list em um array (utilizo a biblioteca numpy para converter a list em um array)

mes=np.arange(1,13,1); # faz um array de 1 a 12 , com step de 1 

plt.plot(mes,tp2,linewidth=1.0, color='r',marker='.') # faço o gráfico da minha variável tp2

plt.title('Gráfico de temperatura média mensal - Floripa',fontsize=14) # insere título no gráfico com fonte de 14
plt.xlabel('Tempo [mês]',fontsize=14) # insere nome no eixo X com fonte de 14
plt.ylabel('Temperatura [$\circ C$]',fontsize=14) # insere o nome no eixo y com fonte de 14
plt.xticks(np.arange(0,13, step=2),fontsize=14) # defino a descrição da escala de 0 a 12 com step de 1
plt.yticks(np.arange(15,27, step=2),fontsize=14) # defino a descrição da escala de 15 a 27 com step de 2
plt.grid() # desenha as linhas de grade
plt.tight_layout() # ajusta para o tamanho da janela
plt.savefig('floripa.jpeg') #

# Exercício 02,  Exemplo 02 - Criar um gráfico com 2 variáveis (segundo eixo)

#data: 27/03/2020
#Por: Yoshi

import numpy as np #biblioteca do matlab
import pandas as pd # biblioteca  R
import matplotlib.pyplot as plt # biblioteca de graficos

#___________variáveis_____
tp = [24.2, 24.6, 23.6, 21.1, 18.9, 16.7, 16.5, 16.9, 17.9, 19.6, 21.3, 23.0]; # criar uma list com 12 várias variáveis (temp média de floripa)
tp2 = np.array(tp); # converto minha list em um array (utilizo a biblioteca numpy para converter a list em um array)

chuva = np.array([162.7, 196.9, 173.0, 92.8, 96.9, 89.5, 99.5, 95.3, 134.2, 109.8, 130.2, 137.0]); # cria um array dos valores de chuva mensal

mes=np.arange(1,13,1); # faz um array de 1 a 12 , com step de 1

#__________________Gráfico______________________________

fig, ax1 = plt.subplots() # defino o nome da minha figura (fig) e nome do meu eixo (ax1)
ax2 = ax1.twinx() # defino o nome do meu segundo eixo (ax2)

ax1.bar(mes,chuva, color='b',label = 'Precipitação') # faço o gráfico de precipitação no eixo (ax1), lado esquerdo
ax2.plot(mes,tp, color='r', linewidth=1,marker='o',label = 'Temperatura') # faço o gráfico de temperatura no eixo (ax2), lado direito

plt.title('Gráfico de Temp e Precipitação média mensal - Floripa',fontsize=14) # título do gráfico
ax1.set_xlabel('Tempo [mês]',fontsize=14) # eixo X é comum para as duas variáveis

ax1.set_ylabel('Precipitação [mm]',fontsize=14) # defino o título no eixo ax1
ax2.set_ylabel('Temperatura [$\circ C$]',fontsize=14) # defino o título no eixo ax2

# Ajusto a escala e a faixa da variável
ax1.xaxis.set(ticks=range(0,13,1),ticklabels=[' ','jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez','']) 
ax1.yaxis.set(ticks=range(0,220,20))
ax2.yaxis.set(ticks=range(15,30,2))


fig.legend(loc=(0.6,0.75)) # mostra a legenda

# faixa toda da variável
ax1.set_xlim((0,13))
ax2.set_ylim((15,29)) 
#ax1.grid()
plt.show()
plt.tight_layout()

# Exercício 02,  Exemplo 03 - Criar Multiplos gráficos (subplot)

#data: 27/03/2020
#Por: Yoshi

import numpy as np #biblioteca do matlab
import pandas as pd # biblioteca  R
import matplotlib.pyplot as plt # biblioteca de graficos

#___________variáveis_____
tp = np.array([24.2, 24.6, 23.6, 21.1, 18.9, 16.7, 16.5, 16.9, 17.9, 19.6, 21.3, 23.0]); # cria um array dos valores de temperatura mensal 
chuva = np.array([162.7, 196.9, 173.0, 92.8, 96.9, 89.5, 99.5, 95.3, 134.2, 109.8, 130.2, 137.0]); # cria um array dos valores de chuva mensal
pressao = np.array([1010.5, 1011.1, 1012.4, 1014.5, 1015.7, 1017.0, 1018.1, 1017.3, 1016.7,	1014.6,	1012.1,	1010.9]); # cria um array dos valores de pressao mensal
umidade = np.array([81.0, 82.0, 82.0, 82.0, 83.0, 83.0, 84.0, 83.0, 83.0, 81.0, 80.0, 80.0]);# cria um array dos valores de umidade mensal

mes=np.arange(1,13,1); # faz um array de 1 a 12 , com step de 1

fig , axes = plt.subplots(4,1); # defino a minha figura para 04 subplots (04 gráficos)

([ax1,ax2,ax3,ax4])=axes # definir o nome dos meus eixos em uma matriz de 4 x 1
#([ax1,ax2],[ax3,ax4])=axes # definir o nome dos meus eixos em uma matriz de 2 x 2

ax1.plot(mes,tp, color='r', linewidth=1,marker='o')
ax2.plot(mes,umidade, color='m',linewidth=1,marker='*')
ax3.plot(mes,pressao, color='g', linewidth=1,marker='+')
ax4.bar(mes,chuva, color='b')

ax1.set_title('Gráfico Climatologia - Floripa',fontsize=14) # Faz o Título do gráfico (somente no primeiro)
ax4.set_xlabel('Tempo [mês]',fontsize=10) # Faz a descrição nos eixos X

# Faz a descrição nos eixos Y 
ax1.set_ylabel('Temp [$\circ C $]',fontsize=10)
ax2.set_ylabel('UR [$\%$]',fontsize=10)
ax3.set_ylabel(r'$P_{atm}$ [$hPa$]',fontsize=10)
ax4.set_ylabel('Prec [$mm$]',fontsize=10)

# Define a escala de cada variável
ax1.yaxis.set(ticks=range(15,35,5))
ax2.yaxis.set(ticks=range(70,110,10))
ax3.yaxis.set(ticks=range(1005,1025,5))
ax4.yaxis.set(ticks=range(0,220,50))
ax4.xaxis.set(ticks=range(0,13))
ax4.xaxis.set(ticklabels=[' ','jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez',''])

#ax1.legend(['Média Temp']);
ax1.xaxis.set_visible(False)
ax2.xaxis.set_visible(False)
ax3.xaxis.set_visible(False)
ax4.xaxis.set_visible(True)

plt.show()
plt.tight_layout()

"""# Aula 03 - CDM - 30/03/2020 - Lista 03"""

# Exercício 02,  Exemplo 04 - Faz o gráfico de Correlação

#data: 30/03/2020
#Por: Yoshi

import numpy as np #biblioteca do matlab
import pandas as pd # biblioteca  R
import matplotlib.pyplot as plt # biblioteca de graficos

#___________variáveis_____
tp = np.array([24.2, 24.6, 23.6, 21.1, 18.9, 16.7, 16.5, 16.9, 17.9, 19.6, 21.3, 23.0]); # cria um array dos valores de temperatura mensal 
chuva = np.array([162.7, 196.9, 173.0, 92.8, 96.9, 89.5, 99.5, 95.3, 134.2, 109.8, 130.2, 137.0]); # cria um array dos valores de chuva mensal
pressao = np.array([1010.5, 1011.1, 1012.4, 1014.5, 1015.7, 1017.0, 1018.1, 1017.3, 1016.7,	1014.6,	1012.1,	1010.9]); # cria um array dos valores de pressao mensal
umidade = np.array([81.0, 82.0, 82.0, 82.0, 83.0, 83.0, 84.0, 83.0, 83.0, 81.0, 80.0, 80.0]);# cria um array dos valores de umidade mensal

mes=np.arange(1,13,1); # faz um array de 1 a 12 , com step de 1

fig = plt.figure()

x=tp; y=pressao # defino temperatura no eixo X e pressão no eixo Y
plt.scatter(x,y) # faz gráfico de correlação entre temperatura e pressão
coef = np.polyfit(x,y,1) # meus coeficientes angular a=-0.88 e linear b=1.03 (eq. linear y(x) = ax +b)
f = np.poly1d(coef) # cria a função f(x), ou y(x)
plt.plot(x,f(x),'r') # faz o gráfico da curva ajustada

plt.title('Gráfico de Correlação Temperatura vs. Pressão - Floripa',fontsize=14)

plt.ylabel('Pressão atmosférica [hPa]',fontsize=14)
plt.xlabel('Temperatura do ar [$\circ C$]',fontsize=14)
plt.yticks(np.arange(1010,1020, step=2),fontsize=14)
plt.xticks(np.arange(15,29, step=2),fontsize=14)
plt.legend(['Simulado','Observado']);
plt.xlim((15,27))
plt.ylim((1010,1019))
plt.grid()
plt.show()
plt.tight_layout()

# Exercício 02,  Exemplo 05 - Faz o gráfico de Histograma

#data: 30/03/2020
#Por: Yoshi

import numpy as np #biblioteca do matlab
import pandas as pd # biblioteca  R
import matplotlib.pyplot as plt # biblioteca de graficos

from numpy import genfromtxt # Faz a leitura de cada linha e converte a string no formato de array (números -float)

uri="https://raw.githubusercontent.com/sakagamiyoshiaki/CDM/master/IFSC-032010.txt" # endereço onde estão os dados histórico (amostra de março de 2011 da estação do IFSC)
# ano, mes, dia, hora, min, temp, umid, press, chuva, vel, dir

data = genfromtxt(uri, delimiter=',')

fig =plt.figure()

y=data[:,5] # temperatura
bins2=np.arange(1,30,0.5) # são minhas "classes" 

plt.hist(y,bins2); # Faz o gráfico de distribuição discreta (histograma)

plt.ylabel('Número de ocorrências [-]');

F=data[:,5]>15
y1=data[F,5]
        
plt.hist(y1,bins2); # Faz o gráfico de distribuição discreta (histograma) - com filtro temperatura <15 , excluído
     
count, bins, ignored = plt.hist(y1, 30, density=True)

#count8033* # tenho o total de ocorrências em cada bin

# Exercício 02,  Exemplo 06 - Faz o gráfico da curva normal

#data: 03/04/2020
#Por: Yoshi

count, bins, ignored = plt.hist(y1, 30, density=True)

mu=np.mean(y1); #media de y1 - temperatura filtrada
sigma=np.std(y1); #desvio padrão de y1 (temperatura filtrada acima de 15C)

YY=1/(sigma * np.sqrt(2*np.pi))*np.exp( - (bins2 - mu)**2/(2*sigma**2) ) # curva normal (gaussina)

plt.plot(bins2,YY,linewidth=2, color='r')

plt.ylabel('Frequencia [-]',fontsize=14)
plt.xlabel('Temperatura do ar [$\circ C$]',fontsize=14)
#plt.yticks(np.arange(0,0.2, step=0.05),fontsize=14)
plt.xticks(np.arange(12,31, step=2),fontsize=14)
plt.legend(['Simulado','Observado']);
plt.xlim((12,30))
plt.ylim((0,0.2))
#plt.grid()
plt.show()
plt.tight_layout()

"""# Aula 04 - CDM - 03/04/2020 - Lista 03"""

import numpy as np #biblioteca do matlab
import pandas as pd # biblioteca  R
import matplotlib.pyplot as plt # biblioteca de graficos

from numpy import genfromtxt # Faz a leitura de cada linha e converte a string no formato de array (números -float)


uri="https://raw.githubusercontent.com/sakagamiyoshiaki/CDM/master/IFSC-032010.txt" # endereço onde estão os dados histórico (amostra de março de 2011 da estação do IFSC)
# ano, mes, dia, hora, min, temp, umid, press, chuva, vel, dir

data = genfromtxt(uri, delimiter=',')

dir=data[:,10]
plt.plot(dir)

!pip install windrose
from windrose import WindroseAxes
ws=data[:,9]
wd=data[:,10]

ax = WindroseAxes.from_ax()
ax.bar(wd, ws, normed=True, opening=1, edgecolor='white')
ax.set_legend()

plt.hist(wd)

"""# Aula 05 - CDM - 06/04/2020 - Lista 04"""

#Lista Exercício 04 - Numpy Basic
#Cheat Sheet - Python Numpy  
#Por: Yoshi
#Data: 06/04/2020

#Principais bibliotecas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from numpy import genfromtxt

#!pip install windrose
#import meteorologia as mt #(tem que fazer um upload da arquivo no Colab)

#Criei um array 1D 
x0=np.arange(-3,10,1); 
x1=np.arange(0,10,0.01);
x2=np.arange(-3,3,0.1);

y0=x0           # função linear
y1=np.log(x1);  # função ln ( log natural)
y2=np.exp(x2);  # função e^x  (exponencial) 

plt.plot(x0,y0)
plt.plot(x1,y1)
plt.plot(x2,y2)

a=np.ones(10,dtype=np.int16)*np.nan # exemplo de criar um array nulo
a

np.linspace(0,10,5)

#%% Exemplo 02 - Criar uma função ( converter temperatura em kelvin)

tp=np.arange(15,30,1); 
#tp=np.ones((25,25),dtype=np.int16)*25

tk=tp+273. # Estrutura de função (1)

#Definir uma função no python

def ConverterTK(x): # Estrutura de função (2)
    y=x+273.15
    return y

a=np.arange(1,10,1)
b=np.arange(11,20,1)

c=a+b

def soma(x1,x2): # funcao de soma
    y=x1+x2
    return y

converterTK(tp)

soma(a,b)

TCK=lambda x:x+273.15 # Estrutura de função (3)

TCK(10)

import meteorologia as mt # Estrutura de função (4)

mt.TK(10)

"""# Aula 06 - CDM - 13/04/2020 - Lista 04"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from numpy import genfromtxt

tp=25
tk=tp+273

def converterTCK(x):
    y=x+273
    return y

converterTCK(30)

TK2= lambda x: x+273
TK2(25)

import meteorologia as mt

mt.TK(40)

tp=25; po=1013; p=920;

alt=-(287*TK2(tp)/9.81)*np.log(p/po)
np.round(alt)

# Definido a funcao para calcular a espessura da camada
def deltaH3(x1,x2,x3,x4):
    yy=-(287*TK2(x1)/x4)*np.log(x2/x3)
    return yy

deltaH3(tp,p,po,9.81)

def reduzir(a1,a2,a3):
    y2=a3*np.exp((9.81*a2)/(287*TK2(a1)))
    return y2

reduzir(25,800,920)

uri='https://raw.githubusercontent.com/sakagamiyoshiaki/CDM/master/ATMpadrao.txt'

#data = genfromtxt(uri, delimiter='\t')
data = genfromtxt(uri, delimiter='\t')

# altura, temp, gravidade, pressao, densidade
data

# Exercício 05 - Calcular a altitude 

TK2= lambda x: x+273.15

# Definido a funcao para calcular a espessura da camada
def deltaH3(x1,x2,x3,x4):
    yy=-((287*TK2(x1))/x4)*np.log(x2/x3)
    return yy


altitude=data[:,0]     # altutude 
temp=data[:,1]         # tempe
g=data[:,2]
pressao=data[:,3]*100  # 

alt2=deltaH3(temp,pressao,1013,g) # calculo da altitude pela Hipsométrica

plt.scatter(pressao,altitude) # gráfico da tabela da atm padrão

plt.plot(pressao,alt2)        # gráfico calculado

#%% Exemplo 05 - calcule a densidade do ar 
altitude=data[:,0];
pressao=data[:,3]*10000;
tp=data[:,1];

rho=pressao/(287*(tp+273.15))

plt.scatter(data[:,4],data[:,0])

plt.plot(rho,altitude)

#%% Exemplo 05 - calculae a densidade do ar 

rho=pressao/(287*TK2(tp))

plt.scatter(data[:,4],data[:,0])

plt.plot(rho,altitude)

plt.scatter(tp,altitude)

plt.scatter(g,altitude)

"""# Aula 07 - CDM - 17/04/2020 - Lista 05"""

#Lista Exercício 05 - Numpy Basic
#Cheat Sheet - Python Numpy  
#Por: Yoshi
#Data: Jan/2020

#Principais bibliotecas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from numpy import genfromtxt

# endereço do arquivo de dados
uri='https://raw.githubusercontent.com/sakagamiyoshiaki/CDM/master/dados-vento.csv'


data = genfromtxt(uri, delimiter=';') # abrir e ler o arquivo

vel=data[:,0]; # seleciona os dados de velocidade 
teta=data[:,1]; # seleciona os dados de direcao

#!pip install mpld3
import mpld3
mpld3.enable_notebook()

plt.plot(vel)
plt.plot(teta)

plt.plot(teta)

vv=8;
dd=30;

#Decompisição do vento - anemometro de copo e biruta
u=-vel*np.sin(teta*np.pi/180)
v=-vel*np.cos(teta*np.pi/180)

plt.plot(u)
plt.plot(v)

# Composição do vento do anemometro Sonico

uu=data[:,2]; # componente u ( direcao leste-oeste)
vv=data[:,3]; # componente v ( direção norte-sul)

plt.plot(u)
plt.plot(uu)

wind=np.sqrt(uu**2+vv**2)
plt.plot(wind)
plt.plot(vel)

#Composição da direção do vento - Utilizando a estrutura condicional (IF)

uu[uu==0]=np.nan # excluo valores de uu=0 => uu=NaN (dado invalido)
vv[vv==0]=np.nan # excluo valores de vv=0 => vv=NaN (dado invalido)


def comp(x1,x2):
    y0=np.arctan(x1/x2)*180/np.pi;
    if (x1>0 and x2>0):               # Q1 - primeiro quadrante
      y=y0+180
      return y
    elif (x1<0 and x2>0):              # Q2 - segundo quadrante
      y=y0+180
      return y
    elif (x1<0 and x2<0):              # Q3 - terceiro quadrante
      y=y0
      return y 
    elif (x1>0 and x2<0):              # Q4 - quarto quadrante
      y=y0+360
      return y

composicao=np.vectorize(comp); # vetorizar (calcular celula a celula), senão o IF considera toda a coluna 

direcao=composicao(uu,vv)

plt.plot(direcao)
plt.plot(teta)

"""# Aula 08 - CDM - 20/04/2020 - Lista 06"""

#Principais bibliotecas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from numpy import genfromtxt

# endereço do arquivo de dados
uri='https://raw.githubusercontent.com/sakagamiyoshiaki/CDM/master/dados-vento.csv'


data = genfromtxt(uri, delimiter=';') # abrir e ler o arquivo

vel=data[:,0]; # seleciona os dados de velocidade 
teta=data[:,1]; # seleciona os dados de direcao

# Simbolos de condicional:
#  == igual
#  != diferente
# > maior
# < menor
# >= maior e igual
# <= menor e igual
# ( x>5  and  x<10 )  - intersecção
# ( x<5  or   x<10 )  - uniao

a=np.array([1,4,2,6,3,4,5,6,7,8,8,10,12,5])
b=a.copy()

for i in range(0,14):    # loop 
  if (a[i]>5):           # condicional
    b[i]=0
  else:              # senao
    b[i]=1

print(b)

len(vel) # te informa o tamanho do array (sequencia de numeros)

vel=data[:,0]; # valores de velocidade

v2=vel.copy() # fiz uma copia

for i in range(0,1440):   # looping
  if (vel[i]<1 or vel[i]>3 ):            # se velocidade maior que 3
    v2[i]=vel[i]          # entao v2 vai ser nula
  else:                   # senao v2 é a vel 
    v2[i]=np.nan

v2

plt.plot(vel)
plt.plot(v2,color='r')

x = np.ones(10)*np.nan

for i in range(0,10):  # looping - faz uma iteracao de 0 a 9 
  x[i]=i      # constroi uma sequencia de 0 a 9
x

# converter m/s em km/h elemento por elemento
x = np.ones(1440)*np.nan

for i in range(0,1440):
  x[i]=vel[i]*3.6

plt.plot(x)

y = vel*3.6 
plt.plot(y)

x = np.ones(120)*np.nan

i=0
while i < 10:
  print(i)
  i += 1        # contador ( ele soma +1 a cada iteracao)

x = np.ones(1440)*np.nan

i=0
while i < 1440:
  x[i]=vel[i]*3.6
  i += 1        # contador ( ele soma +1 a cada iteracao)

plt.plot(x)

"""# Aula 09 - CDM - 24/04/2020 - Lista 06"""

# relembrando a estrutura de FOR (loop) e IF (condicional)
vel2=vel.copy()

for i in range(0,1440):
  if (vel[i]>3):
    vel2[i]=np.nan

plt.plot(vel)
plt.plot(vel2)

#Lista Exercício 06 - Looping
#Cheat Sheet - Python Numpy  
#Por: Yoshi
#Data: Jan/2020

#Principais bibliotecas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from numpy import genfromtxt
from matplotlib import cm

uri='https://raw.githubusercontent.com/sakagamiyoshiaki/CDM/master/chuva.dat'


A = genfromtxt(uri, delimiter=',')
#A = genfromtxt('chuva.dat', delimiter=',')

ano=A[:,0]
mes=A[:,1]
dia=A[:,2]
chuva=A[:,3]

plt.plot(chuva)

chuva1980=chuva.copy()

for i in range(0,11294):
  if ano[i]==1980:
    chuva1980[i]=chuva[i]
  else:
    chuva1980[i]=0  

plt.plot(chuva1980)

chuvaAno=np.ones(31)*np.nan
year=np.arange(1980,2011)

for i in range(0,31):
  chuvaAno[i]=np.nansum(chuva[ano==1980+i])

plt.bar(year,chuvaAno)

year

#Lista 06 , Exercicio 02
chuvaMes=np.ones(12)*np.nan
month=np.arange(1,13)

for i in range(0,12):
  chuvaMes[i]=np.nansum(chuva[mes==i+1])/30
  
plt.bar(month,chuvaMes);
plt.xticks(np.arange(0,13, step=1));

#Lista 06 Exercicio 03-  anomalia anual

for i in range(0,31):
  chuvaAno[i]=np.nansum(chuva[ano==1980+i])

chuvaAno[chuvaAno==0]=np.nan

chuvaTm=np.nanmean(chuvaAno) # media de 30 de chuva 
chuvaTm
anomalia = chuvaAno-chuvaTm

plt.bar(year,100*(anomalia/chuvaTm))

chuvaTm

plt.hist(chuvaAno);

x1=chuvaAno

count, bins, ignored = plt.hist(x1, 5, density=True)
mu=np.nanmean(x1);
sigma=np.nanstd(x1);

YY=1/(sigma * np.sqrt(2*np.pi))*np.exp( - (bins - mu)**2/(2*sigma**2) )
plt.plot(bins,YY,linewidth=1, color='r');

# Lista 06 - Ex 05 total de chuva de cada mes e cada ano 
chuvaT = np.ones((12,31))
nulostt = np.ones((12,31))

for i in range(0,31):
  for j in range(0,12):
    chuvaT[j][i]=np.nansum(chuva[(ano==1980+i) & (mes==j+1)])/30
    nulostt[j][i]=np.sum(np.isnan(chuva[(ano==1980+i) & (mes==j+1)]))

chuvaT[chuvaT==0]=np.nan

plt.contourf(chuvaT);

plt.contourf(nulostt);

#Lista 06 - exercicio 04
chuva[0:10]
np.isnan(chuva[0:10])
np.sum(np.isnan(chuva)) #total 3505 dados Nan
nulos = np.ones(12)
tt = np.ones(12)

month=np.arange(1,13)
                
for i in range(0,12):
  nulos[i]=np.sum(np.isnan(chuva[mes==i+1]))
  tt[i]=len(chuva[mes==i+1])

plt.bar(month,100*nulos/tt)

#Lista 06 - exercicio 04

nulosY=np.ones(31)*np.nan
year=np.arange(1980,2011)
ttY = np.ones(31)

for i in range(0,31):
  nulosY[i]=np.sum(np.isnan(chuva[ano==1980+i]))
  ttY[i]=len(chuva[ano==1980+i])

plt.bar(year,100*nulosY/ttY)

"""# Aula 10 - CDM - 27/04/2020 - Lista 06"""

#Principais bibliotecas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from numpy import genfromtxt
from matplotlib import cm

#Avaliacao 01 - exercicio 03

uri='https://origin.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/detrend.nino34.ascii.txt'

A = genfromtxt(uri)

dd=np.arange('1950-01', '2020-05', dtype='datetime64[M]')

plt.plot(dd,A[1:,4])
plt.grid()

"""# Aula 11 - CDM - 08/05/2020 - Lista 07"""

#Bom Dia, Vamos começar a aula as 9:45h


#Principais bibliotecas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from numpy import genfromtxt
from matplotlib import cm

#A1 = np.loadtxt('CR1000_saida1min.dat', delimiter=',',skiprows=1,dtype=float)
#A = genfromtxt(uri)

# 'df" é meu dataframe

df = pd.read_csv('CR1000_saida1min.dat',header=1,skiprows=[2,3]);

df.dtypes

df[df=='NAN']=np.nan
df

plt.plot(np.arange(0,100, step=1),df['Tagua_Avg'][150:250].astype(float));
plt.plot(np.arange(0,100, step=1),df['Tterra_Avg'][150:250].astype(float));
plt.legend(['Tagua','Tterra']);
plt.title('Gráfico de Experimento - Terra-agua',fontsize=14);
plt.xlabel('Tempo [min]',fontsize=14)
plt.ylabel('Temperatura [$\circ C$]',fontsize=14)
plt.xticks(np.arange(0,110, step=10),fontsize=14);
plt.yticks(np.arange(20,50, step=5),fontsize=14);

plt.grid()

"""# Aula 12 - CDM - 13/05/2020 - Lista 07"""

#Principais bibliotecas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from numpy import genfromtxt

#%% Exemplo 01 - Importar arquivo texto sem cabeçalho

uri='https://raw.githubusercontent.com/sakagamiyoshiaki/CDM/master/saida2010.txt'

A1 = np.loadtxt(uri, delimiter=',',skiprows=1,dtype=float) # abrir um arquivo de dados pela biblioteca Numpy

plt.plot(A1[:,6])

A=np.loadtxt('saida2010.txt',delimiter=',')
A

I=A[:,8]>900
plt.plot(A[I,8])

df1 = pd.read_csv(uri,header=None); # abrir um arquivo pela biblioteca pandas - df (dataframe)

df1

uri= 'https://raw.githubusercontent.com/sakagamiyoshiaki/CDM/master/IFSC_IFSC60.dat'

df=pd.read_csv(uri,skiprows=[0,2,3])
df.dtypes

#plt.plot(df.iloc[:,3])
plt.plot(df['Precipitacao_Tot'])

df.columns

#%% Exemplo 03 Importar dados Merra (netcdf)

#wget --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies --content-disposition -i url.txt
#https://disc.gsfc.nasa.gov/datasets/M2T1NXSLV_5.12.4/summary?keywords=%22MERRA-2%22
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#!pip install netcdf4 # executar pelo menos uma vez
import xarray as xr
import  netCDF4

nc = netCDF4.Dataset('AirTEMP_BuenosAires.nc');

nc

h = nc.variables['T2M']
hs = pd.Series(h[:,0,0])
plt.plot(hs)

h = nc.variables['T2M']
times = nc.variables['time']
jd = np.array(netCDF4.num2date(times[:],times.units), dtype='datetime64[s]')
hs = pd.Series(h[:,0,0],index=jd)
plt.plot(hs)

#%% Exercio extra 07

uri='https://github.com/sakagamiyoshiaki/CDM/blob/master/Temperatura-Media-Compensada_NCB_1961-1990.xls?raw=true'
#uri='Temperatura-Media-Compensada_NCB_1961-1990.xls'

dfx = pd.read_excel(uri,header=3);
dfx=dfx.replace('-',np.nan)

dfx

plt.plot(dfx['Janeiro'])

plt.plot(dfx[(dfx['Nome da Estação']=='Florianópolis')].iloc[:,3:15].T)

"""# Aula 13 - CDM - 15/05/2020 - Lista 08"""

#Lista Exercício 08 - Introdução ao Pandas
#Cheat Sheet - Pandas Basics
#Por: Yoshi
#Data: Maio/2020

#Principais bibliotecas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#!pip install mpld3
#import mpld3
#mpld3.enable_notebook()

#Exemplo do exercicio da Avaliação 01

df = pd.read_csv('radiosonda.csv',header=0, delimiter=';'); # o comando pd.read_ já tranforma em dataframe
df

df.columns

plt.scatter(df['THTA'],df['HGHT'])

df.tail(10)

df.describe()

df.shape

df.index

#%% Exemplo 01 - abrir um arquivo e transformar em Dataframe

uri='https://raw.githubusercontent.com/sakagamiyoshiaki/CDM/master/InmetFloripa2020.txt'

df = pd.read_csv(uri,header=0); # o comando pd.read_ já tranforma em dataframe

plt.plot(df['temp_inst'])

df

df.dtypes

a=df.to_numpy()
plt.plot(a[:,5])

df.T

df.sort_index(axis=0, ascending=False) # Ordenar o índice de forma ascendente

df.sort_values(by='temp_inst', ascending=False) # Ordenar pela coluna temp_inst

df

df['timestamp'] = pd.to_datetime(df['data'].astype(str) + ' ' + df['hora'].astype(str), format='%d/%m/%Y %H')

df.dtypes

df.index=df['timestamp']

plt.plot(df.temp_inst)

df=df.sort_index(axis=0, ascending=True)

plt.plot(df.temp_inst)

df.index

plt.plot(df['2020-02-10 00:00:00':'2020-02-15 00:00:00']['temp_inst'])

plt.plot(df.iloc[1:100,3:6])

df.columns

plt.plot(df['2020-02-10 00:00:00':'2020-02-15 00:00:00'][['temp_inst','temp_max','temp_min']])

df2=df.iloc[0:100,[3,6,9]]# seleção por posicionamento - coluna especifica

df2

df2.to_csv('saida.csv') # salva os dados em um arquivo csv

"""# Aula 14 - CDM - 18/05/2020 - Lista 09"""

#Lista Exercício 09 - Introdução ao Pandas II
#Cheat Sheet - Pandas Basics
#Por: Yoshi
#Data: Maio/2020

#Principais bibliotecas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#!pip install mpld3
#import mpld3
#mpld3.enable_notebook()

uri='https://raw.githubusercontent.com/sakagamiyoshiaki/CDM/master/InmetFloripa2020.txt'
df = pd.read_csv(uri,header=0); # o comando pd.read_ já tranforma em dataframe
df['timestamp'] = pd.to_datetime(df['data'].astype(str) + ' ' + df['hora'].astype(str), format='%d/%m/%Y %H')
df.index=df['timestamp']
df=df.sort_index(axis=0, ascending=True) # Ordenar o índice de forma ascendente

plt.plot(df['2020-02-01 23:00:00':'2020-02-15 23:00:00']['precipitacao'])

#df['precipitacao'].hist()
df.hist('temp_inst')

df['tk']=df['temp_inst']+273

f=lambda x:x+273.15 # função definda (coverte temperatura Celsius em kelvin)
df['temp_inst']=df['temp_inst'].apply(f) # aplica uma função em um Dataframe

df2=df['2020-02-01 23:00:00':'2020-02-15 23:00:00'][['temp_inst','precipitacao','pressao']]

df2['tc']=df2['temp_inst']-273

df2['tk']=df2['temp_inst']+273

df2.drop(['tk'],axis=1,inplace=True) # exclui uma coluna atualiza o dataframe
df2=df2.drop(['tk'],axis=1)

df2

df2.drop(df2.index[1:4])

df3=df.iloc[0:20,1:7]
df3

df3['temp_inst'][df3['temp_inst']>29]=np.nan; exluindo valores acima 29 graus e sustituindo por NaN
df3

df3['temp_inst'][(df3['temp_inst']>25) & (df3['temp_inst']<30)]=np.nan; #exluindo valores acima de 25 e abaixo de 29 graus e sustituindo por NaN
df3

df3['temp_inst'][(df3['temp_inst']<26) | (df3['temp_inst']>30)]=np.nan; #exluindo valores acima de 25 e abaixo de 29 graus e sustituindo por NaN
df3

df4=df.iloc[0:20,1:7]
df4

df8=df.iloc[0:20,1:7]

df9=df8.copy() # copia do dataframe (não modufica quando df altera)
df10=df8       # clone do dataframe (modifica junto com o df)

df8.loc[(df8['temp_inst']<25.5) | (df8['temp_inst']>30),'temp_inst']=np.nan
df9

df5=df4.copy() # copia do dataframe (não modufica quando df altera)

df5

df6=df4       # clone do dataframe (modifica junto com o df)

df6

df4['temp_inst']=0

df6

dt=pd.date_range(start='2010-03-01 00:00:00',end='2010-03-31 23:55:00',freq='05min');
dt

"""# Aula 15 - CDM - 22/05/2020 - Lista 10"""

#Principais bibliotecas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#!pip install mpld3
#import mpld3
#mpld3.enable_notebook()

#Abrir o arquivo csv 
uri='https://raw.githubusercontent.com/sakagamiyoshiaki/CDM/master/IFSC-032010.txt'

df = pd.read_csv(uri,header=None); # Faz a leitura sem  e sem index

df.head()

!pip install mpld3
import mpld3
mpld3.enable_notebook()

df.columns=['year','month','day','hour','minute','tp','rh','pre','chuva','vel','dir']
df.columns

df.head()

df['date']=pd.to_datetime(df[['year','month','day','hour','minute']])

df2=df.copy()
df2=df2.drop(range(1000,2000,1))  # exclusão de 1000 linhas

df.index=df['date']
#df2.index=df2['date']

df2=df2.drop(['date'],axis=1)

df2.head()

plt.plot(df.tp)
plt.plot(df2.tp)

df2['date']=pd.to_datetime(df2[['year','month','day','hour','minute']])
df2.index=df2['date']

plt.plot(df2.tp)

df2['tp'].to_csv('saida.txt') # ver a saída de dados com linhas vazias

#criar uma serie artifical completa

dt=pd.date_range(start='2010-03-01 00:00:00',end='2010-03-31 23:55:00',freq='05min'); # criar uma série temporal inteira
idx=pd.DatetimeIndex(dt) # serie temporal e transforma em index
df2 = df2.reindex(idx) # reindexar

plt.plot(df2.tp)
df2['tp'].to_csv('saida2.txt') # ver a saída de dados com linhas vazias

np.isnan(df2.tp)

# dados duplicados

df3=df2.copy()
df4=pd.concat([df3.loc['2010-03-20 00:00:00':'2010-03-20 00:00:00',:]]*2000, ignore_index=False) # replicando linhas
df5=pd.concat([df4,df3],axis=0)
df5=df5.sort_index()
df5.head(15)
plt.plot(np.arange(0,len(df5),1),df5.tp)
plt.plot(np.arange(0,len(df2),1),df2.tp)

df6=df5.loc[~df5.index.duplicated(keep='last')] # separa apenas os dados não duplicados
plt.plot(np.arange(0,len(df6),1),df6.tp)
plt.plot(np.arange(0,len(df2),1),df2.tp)

df3=df2.loc['2010-03-01 00:15:00':'2010-03-01 00:30:00'].copy()
df4=pd.concat([df3,df2],axis=0)
df4.head(15)

df4=df4.sort_index()
df4.head(15)

df4.index.duplicated() # verificar se há indices duplicados
df4.loc[df4.index.duplicated(keep='first')] # mantenha o primeiro

# remover os dados manualmente

df6=df2.copy()
plt.plot(df6.tp)

df6.tp['2010-03-12 07:00:00':'2010-03-14 14:00:00']=np.nan

plt.plot(df5.tp)
plt.plot(df6.tp)

df6['tp'].to_csv('saida3.txt') # ver a saída de dados com linhas vazias

plt.plot(df5.tp)
plt.plot(df6.tp)

# preeecher a serie

df7=df6.fillna(0) # preencher com zero todo o dataframe
plt.plot(df7.tp)


df7['tp'].to_csv('saida4.txt') # ver a saída de dados com linhas vazias

df8=df6.fillna(method='bfill') # preencher com os dados anterior
plt.plot(df8.tp)

df8['tp'].to_csv('saida5.txt') # ver a saída de dados com linhas vazias

df10=df6.interpolate() # preencher fazendo interpolação
plt.plot(df10.tp)

df10=df6.interpolate(method='time') # fazendo a interpolação com o tempo
plt.plot(df10.tp)

"""# Aula 16 - CDM - 25/05/2020 - Lista 11"""

#Principais bibliotecas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Abrir o arquivo csv 
uri='https://raw.githubusercontent.com/sakagamiyoshiaki/CDM/master/IFSC-032010.txt'

df = pd.read_csv(uri,header=None); # Faz a leitura sem  e sem index

df

df.columns=['year','month','day','hour','minute','tp','rh','pre','chuva','vel','dir']

plt.plot(df[2000::][['tp','rh','vel']])

df.index

df['date']=pd.to_datetime(df[['year','month','day','hour','minute']])

df.index=df['date']
#df=df.drop(['date'],axis=1)
df

plt.plot(df['2010-03-10 00:00:00':'2010-03-15 00:00:00'].tp)

#Exemplo index - nome das estacoes


uri='https://github.com/sakagamiyoshiaki/CDM/blob/master/Temperatura-Media-Compensada_NCB_1961-1990.xls?raw=true'
#uri='Temperatura-Media-Compensada_NCB_1961-1990.xls'

dfx = pd.read_excel(uri,header=3);

dfx=dfx.replace('-',np.nan)

dfx.index=dfx['Nome da Estação']

dfx[dfx['Nome da Estação']=='Florianópolis']

dfx.iloc[1:5,3:15]

dfx[dfx['Nome da Estação']=='Florianópolis']

plt.plot(dfx.loc['Ubatuba'][3:15])

dfx

plt.plot(dfx[dfx['UF']=='SC'].iloc[:,3:15].T);

dfx[dfx['UF']=='SC'].iloc[:,3:15]

# Juntar os dataframes

#Exemplo 01 - juntar dados de estações do INMET

#Lista Exercício 11 - Manipulando Dataframes - Parte II
#Cheat Sheet - Pandas  Join, Merge e Concat I
#Por: Yoshi
#Data: Abril/2020

#Principais bibliotecas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#!pip install mpld3
#import mpld3
#mpld3.enable_notebook()

#Abrir o arquivo csv 
uri='https://raw.githubusercontent.com/sakagamiyoshiaki/CDM/master/InmetFloripa2020.txt'
uri2='https://raw.githubusercontent.com/sakagamiyoshiaki/CDM/master/InmetSaoMigheldoOeste2020.txt'
uri3='https://raw.githubusercontent.com/sakagamiyoshiaki/CDM/master/InmetsSantaVitoriaPalmar2020.txt'
uri4='https://raw.githubusercontent.com/sakagamiyoshiaki/CDM/master/InmetSaoPedroSaoPaulo2020.txt'


df1 = pd.read_csv(uri,header=0); # o comando pd.read_ já tranforma em dataframe
df2 = pd.read_csv(uri2,header=0); # o comando pd.read_ já tranforma em dataframe
df3 = pd.read_csv(uri3,header=0); # o comando pd.read_ já tranforma em dataframe
df4 = pd.read_csv(uri4,header=0); # o comando pd.read_ já tranforma em dataframe

df1.index = pd.to_datetime(df1['data'].astype(str) + ' ' + df1['hora'].astype(str), format='%d/%m/%Y %H') # faz a indexação do tempo (coluna data e hora )
df1=df1.sort_index(axis=0, ascending=True) # Ordenar o índice de forma ascendente
df1 #df.index

df2.index = pd.to_datetime(df2['data'].astype(str) + ' ' + df2['hora'].astype(str), format='%d/%m/%Y %H') # faz a indexação do tempo (coluna data e hora )
df2=df2.sort_index(axis=0, ascending=True) # Ordenar o índice de forma ascendente
df2 #df.index

df3.index = pd.to_datetime(df3['data'].astype(str) + ' ' + df3['hora'].astype(str), format='%d/%m/%Y %H') # faz a indexação do tempo (coluna data e hora )
df3=df3.sort_index(axis=0, ascending=True) # Ordenar o índice de forma ascendente
df3 #df.index

df4.index = pd.to_datetime(df4['data'].astype(str) + ' ' + df4['hora'].astype(str), format='%d/%m/%Y %H') # faz a indexação do tempo (coluna data e hora )
df4=df4.sort_index(axis=0, ascending=True) # Ordenar o índice de forma ascendente
df4 #df.index

df1

dfr1=df1.iloc[0:10,3:6]
dfr2=df2.iloc[3:15,3:6] # deixar desencontrado
dfr3=df3.iloc[0:16,3:6]
dfr4=df4.iloc[0:15,3:6]

dfr2

dfr1

#dfr1.join(dfr2,how='outer', lsuffix='_flo',rsuffix='_smo') # join (how= left, right, inner, outer)

dfr1.join(dfr2,how='outer', lsuffix='_flo',rsuffix='_smo')

pd.merge(dfr1,dfr2, how='right',left_index=True, right_index=True) # "merge" colunas com mesmo nome , merge pelo index

df=pd.concat([dfr1,dfr2,dfr3,dfr4],keys=['FLO','SMO','SVP','SPS'],axis=1) # mantem os nomes das colunas (level=0), faz um Multipindex level=1
df

df['SMO'].temp_inst