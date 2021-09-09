import sys
from scraper import scraper
from tqdm import tqdm
from datetime import date
import os

symbols = sys.argv[1:]

def main():
  print("Data output directory? (data)")
  outdir = input()
  if outdir == "":
    outdir = "data/" + str(date.today())
  else:
    outdir += "/" + str(date.today())

  if not os.path.exists(outdir):
    os.makedirs(outdir)

  
  for symbol in tqdm(symbols):
    print(">>>>>" + symbol + "<<<<<")
    calls, puts = scraper(symbol)
    if len(calls.columns) > 0 or len(puts.columns) > 0:
      calls.to_csv(outdir + "/" + symbol.upper() + "_calls.csv")
      puts.to_csv(outdir + "/" + symbol.upper() + "_puts.csv")

if __name__ == "__main__":
  main()