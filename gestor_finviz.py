import os
import requests
from bs4 import BeautifulSoup
import openpyxl

def normalize_content(content):
    # Eliminar espacios en blanco adicionales y saltos de línea
    return ''.join(content.split())

def generar_excels(rows):
    # Escribir los encabezados de columna
    headers = [th.text.strip() for th in rows[0].find_all('th')]
    print("headers:", headers)

    # Crear libros de trabajo de Excel para 'Buy' y 'Sale'
    workbook_buy = openpyxl.Workbook()
    worksheet_buy = workbook_buy.active
    worksheet_buy.append(headers)

    workbook_sale = openpyxl.Workbook()
    worksheet_sale = workbook_sale.active
    worksheet_sale.append(headers)

    # Escribir los datos de las filas
    for row in rows[1:]:
        cols = [col.text.strip() for col in row.find_all('td')]

        # Verificar si la columna 'Transaction' está presente
        if 'Transaction' in headers:
            transaction_index = headers.index('Transaction')
            # Verificar si el índice está dentro de los límites de la lista cols
            if transaction_index < len(cols):
                if cols[transaction_index] == 'Option Exercise':
                    continue  # Omitir esta fila

        # Formatear las columnas numéricas
        for i, col in enumerate(cols):
            if headers[i] in ['Cost']:
                cols[i] = float(col)

            if headers[i] in ['#Shares', 'Value ($)', '#Shares Total']:
                col = col.replace(',', '')
                cols[i] = float(col)

        # Escribir la fila en el archivo Excel correspondiente
        if 'Transaction' in headers:
            transaction_index = headers.index('Transaction')
            if transaction_index < len(cols):
                if cols[transaction_index] == 'Buy':
                    worksheet_buy.append(cols)
                elif cols[transaction_index] == 'Sale':
                    worksheet_sale.append(cols)

    # Guardar los libros de trabajo en archivos
    workbook_buy.save('./salidas/latest-insiders-trading-Buy.xlsx')
    workbook_sale.save('./salidas/latest-insiders-trading-Sale.xlsx')
    print("Datos guardados en ./salidas/latest-insiders-trading-Buy.xlsx y ./salidas/latest-insiders-trading-Sale.xlsx")
    

def get_latest_insiders_trading_info():
    print("Ejecutando gestor_finviz.get_latest_insiders_trading_info()")

    url = "https://finviz.com/insidertrading.ashx"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        res = requests.get(url, headers=headers)
        print("res:", res)
        res.raise_for_status()
    except Exception as e:
        print(f"Error: {e}")
    else:
        soup = BeautifulSoup(res.text, 'html.parser')        
        table = soup.find('table', {'class': 'styled-table-new is-rounded is-condensed mt-2 w-full'})

        if table:
            # Crear directorios de salida si no existen
            os.makedirs('salidas', exist_ok=True)
            os.makedirs('auxiliar', exist_ok=True)

            # Obtener las filas de la tabla
            rows = table.find_all('tr')            
            contenido_actual = normalize_content(str(rows))
            
            fich_aux = './auxiliar/latest-insiders-transaction-rows.html'

            if os.path.isfile(fich_aux):
                with open(fich_aux, 'r', encoding='utf-8') as f:
                    contenido_previo = normalize_content(f.read())
                
                print("Longitud de contenido_previo:", len(contenido_previo))
                print("Longitud de contenido_actual:", len(contenido_actual))
                
                if contenido_previo == contenido_actual:
                    hay_cambios = False
                else:
                    hay_cambios = True
                    with open(fich_aux, 'w', encoding='utf-8') as f:
                        f.write(str(rows))
            else:
                hay_cambios = True
                with open(fich_aux, 'w', encoding='utf-8') as f:
                    f.write(str(rows))

            if hay_cambios:
                # Continuar con el tratamiento de los datos
                generar_excels(rows)
            else:
                print("No hay nuevos datos. Omitiendo el tratamiento.")

        else:
            print("No se encontró la tabla en la página.")

def main():
    get_latest_insiders_trading_info()

if __name__ == '__main__':
    main()
