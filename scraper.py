from bs4 import BeautifulSoup
import time
import pandas as pd
import http.client


#############################
#############################

httpwaittime = 10

def scraper(ticker):
    time.sleep(httpwaittime)
    conn = http.client.HTTPSConnection("finance.yahoo.com")
    payload = ''
    headers = {
        'Cookie': 'B=951oehhg4dp7e&b=3&s=bt'
    }
    conn.request("GET", "/quote/"+ticker +
                 "/options?p="+ticker, payload, headers)
    res = conn.getresponse()
    data = res.read()

    soup = BeautifulSoup(data, 'lxml')
    try:
        expirations = soup.find_all("select")[0].findChildren('option')
    except IndexError:
        print("couldn'd find expirations for " + ticker)
        return pd.DataFrame(), pd.DataFrame()
    calls_df = pd.DataFrame(
        index=["Strike Price", "Last Price", "Bid", "Ask", "Open Interest", "Implied Volatility"])
    puts_df = pd.DataFrame(
        index=["Strike Price", "Last Price", "Bid", "Ask", "Open Interest", "Implied Volatility"])

    for expiry in expirations:
        date_of_expiry = pd.to_datetime(
            expiry["value"], unit='s').to_pydatetime()

        print(str(date_of_expiry) +
              ' [' + str(expirations.index(expiry) + 1) + '/' + str(len(expirations)) + "]")

        time.sleep(httpwaittime)
        conn = http.client.HTTPSConnection("finance.yahoo.com")
        payload = ''
        headers = {
            'Cookie': 'B=951oehhg4dp7e&b=3&s=bt'
        }
        conn.request("GET", "/quote/"+ticker+"/options?date=" +
                     str(expiry["value"])+"&p=" + ticker, payload, headers)
        res = conn.getresponse()
        data = res.read()

        soup = BeautifulSoup(data, 'lxml')
        try:
            callsTable = soup.find_all("table", {"class": "calls"})[
                0].findChildren('tbody')[0]
            putsTable = soup.find_all("table", {"class": "puts"})[
                0].findChildren('tbody')[0]
        except IndexError:
            print("index error")
            continue
        
        populateTable(callsTable, calls_df)
        populateTable(putsTable, puts_df)
      
    return calls_df, puts_df


def populateTable(tbl, df):
  currentContract = ""  
  for row in tbl:
      row_td = []
      colNum = 0
      # if "in-the-money" in row.attrs['class']:
      #     continue
      for td in row:
          if colNum == 0 and td.text != "Contract Name":
              currentContract = td.text
          if colNum == 2:
              row_td.append(td.text)
          if colNum == 3:
              row_td.append(float(td.text.replace(',', '')))
          if colNum == 9:
              if td.text != '-':
                  row_td.append(float(td.text.replace(',', '')))
              else:
                  row_td.append(0)
          if colNum == 4:
              if td.text != '-':
                  row_td.append(float(td.text.replace(',', '')))
              else:
                  row_td.append(0)
          if colNum == 5:
              if td.text != '-':
                  row_td.append(float(td.text.replace(',', '')))
              else:
                  row_td.append(0)
          if colNum == 10:
              if td.text != '-':
                  row_td.append(float(td.text.replace('%', '')))
              else:
                  row_td.append(0)

          colNum += 1
      df[currentContract] = row_td
  