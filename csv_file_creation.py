mport requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

target_url = 'https://economictimes.indiatimes.com/wealth/insure/life-insurance/latest-life-insurance-claim-settlement-ratio-of-insurance-companies-in-india/articleshow/97366610.cms'

response = requests.get(target_url)

if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

            tables = soup.find_all('table')

                if tables:
                            rows = tables[0].find_all('tr')
                                    df = pd.DataFrame(columns = [row_data.text.strip() for row_data in rows[2]])

                                            for row in rows[3:]:
                                                            cells = row.find_all(['td'])
                                                                        row_data = [cell.text.strip() for cell in cells]
                                                                                    endpoint = len(df)
                                                                                                df.loc[endpoint] = row_data

                                                                                                        csv_file_path = 'scraped_data.csv'
                                                                                                               
                                                                                                                       df.to_csv(csv_file_path, index=False, header=False)
                                                                                                                               print(df)

                                                                                                                                       print(f"Data has been saved to {csv_file_path}")

                                                                                                                                           else:
                                                                                                                                                       print("Error: Table not found on the page.")

                                                                                                                                                   else:
                                                                                                                                                           print(f"Error: Unable to retrieve the page. Status Code: {response.status_code}")

