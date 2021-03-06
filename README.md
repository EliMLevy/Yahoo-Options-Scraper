# Yahoo Options Scraper

A tool to monitor/collect basic data on options using Yahoo Finance.

## Instructions
1. clone the repository and install dependencies 
```bash
$ git clone https://github.com/EliMLevy/Yahoo-Options-Scraper.git
$ cd Yahoo-Options-Scraper
$ pip3 install -r requirements.txt
```
2. Run the main file and input the desired symbols as command line arguments
```bash
python3 main.py <symbols>
```
3. Input the desired output directory (if the directory entered doesnt exist, it will be created) or press enter for the default "data" directory
```
Data output directory? (data)
```
Note: the collected data will be stored within a directory with todays date. In other words, if you plan on collecting data over several days, you can reuse an output directory.

Folder structure:

```
Yahoo-Options-Scraper
|
│   Project Files   
│
└───{Output directory}
│   │
│   └───{dd-mm-yy}
│       │   {symbol1}_calls.csv
│       │   {symbol1}_puts.csv
│       │   {symbol2}_calls.csv
│       │   {symbol2}_puts.csv
│       │   ...
|       ...
```

Note: The script waits 10 seconds between each HTTP request. Furthermore, a new HTTP request is made to collect data on each expiration period of an underlying. Therefore, an underlying with many expirations (or a set of underlyings) may take several minutes to complete data collection.

## Output Format
For each symbol entered, the script will (if Yahoo Finance has the data) create two csv files, one for the calls contracts and one for the puts. Both types follow the same format:
 
|                   | Contract1     | Contract2   | ...    |
| -------------     |-------------: | -----:      |------: |
|  Strike Price     | 15.00         |18.00        |...     |
| Last Price        | 10.3          |  6.3        |...     |
| Bid               | 11.1          |   5.6       |...     |
|  Ask              | 11.3          | 6.25        |...     |
| Open Interest     |6.0            |   30.0      |...     |
| Implied Volatility| 490.63        |     384.38  |...     |