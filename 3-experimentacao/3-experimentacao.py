import time
import random
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from selenium import webdriver

def main():
    get_ativos()
    cotacoes_ativos_fechamento = get_cotacoes()
    percentual_acumulado = tratando_cotacoes(cotacoes_ativos_fechamento)
    carteira = gerando_carteira_aleatoria(percentual_acumulado)
    
    print(carteira)


def get_ativos():
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory":"<seu_path>"}

    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(executable_path='<seu_path>chromedriver', chrome_options=options)

    driver.get("https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br")

    btn_download = driver.find_element_by_partial_link_text('Download')
    btn_download.click()

    time.sleep(3)

    driver.close()
    
    
def get_cotacoes():
    df = pd.read_csv('IBOVDia_<dd-MM-yy>.csv', sep=';', skiprows=1)

    ativos = list(df.index[:-2])
    ativos = map(lambda a: f"{a}.SA", ativos)
    ativos_sa = " ".join(list(ativos))

    yf.pdr_override()

    cotacoes_ativos = yf.download(tickers=ativos_sa, period='1y')
    
    return cotacoes_ativos['Adj Close']


def tratando_cotacoes(cotacoes_ativos_fechamento):
    cotacoes_ativos_fechamento.dropna(how='all', inplace=True)
    cotacoes_ativos_fechamento.dropna(axis=1, inplace=True, thresh=248)
    
    percentual_alteracao = cotacoes_ativos_fechamento.pct_change()
    percentual_acumulado = (1 + percentual_alteracao).cumprod()
    percentual_acumulado.iloc[0] = 1
    
    return percentual_acumulado


def gerando_carteira_aleatoria(percentual_acumulado):
    
    carteira = random.choices(percentual_acumulado.columns, k=5)
    
    carteira_ativos = percentual_acumulado.loc[:, carteira]
    
    carteira_ativos = 1000 * carteira_ativos
    carteira_ativos['saldo'] = carteira_ativos.sum(axis=1)
    
    carteira_ativos['saldo'].plot(figsize=(18,10), label="carteira")
    plt.legend()
    
    return carteira_ativos
    

if __name__ == '__main__':
    main() 
