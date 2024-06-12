import requests
from bs4 import BeautifulSoup
import openpyxl
import os


def get_info():
    print("Ejecutando latest_insiders_trading.get_info()")

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
            os.makedirs('./salidas', exist_ok=True)

            # Obtener las filas de la tabla
            rows = table.find_all('tr')            

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

                # Verificar si la columna 'Transaction' es 'Option Exercise'
                if 'Transaction' in headers and cols[headers.index('Transaction')] == 'Option Exercise':
                    continue  # Omitir esta fila

                # Formatear las columnas numéricas
                for i, col in enumerate(cols):
                    if headers[i] in ['Cost']:
                        cols[i] = float(col)

                    if headers[i] in ['#Shares', 'Value ($)', '#Shares Total']:
                        col = col.replace(',', '')
                        cols[i] = float(col)

                # Escribir la fila en el archivo Excel correspondiente
                if 'Transaction' in headers and cols[headers.index('Transaction')] == 'Buy':
                    worksheet_buy.append(cols)
                elif 'Transaction' in headers and cols[headers.index('Transaction')] == 'Sale':
                    worksheet_sale.append(cols)

            # Guardar los libros de trabajo en archivos
            workbook_buy.save('./salidas/latest-insiders-trading-Buy.xlsx')
            workbook_sale.save('./salidas/latest-insiders-trading-Sale.xlsx')
            print("Datos guardados en ./salidas/latest-insiders-trading-Buy.xlsx y ./salidas/latest-insiders-trading-Sale.xlsx")
        else:
            print("No se encontró la tabla en la página.")


def main():
    get_info()

if __name__ == '__main__':
    main()
