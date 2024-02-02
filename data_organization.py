mport requests
from bs4 import BeautifulSoup
import pandas as pd

target_url = 'https://economictimes.indiatimes.com/wealth/insure/life-insurance/latest-life-insurance-claim-settlement-ratio-of-insurance-companies-in-india/articleshow/97366610.cms'

response = requests.get(target_url)

if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

            tables = soup.find_all('table')
                
                    if tables:
                                rows = tables[0].find_all('tr')
                                        df = pd.DataFrame(columns = [row.text.strip() for row in rows[2]])
                                                for row in rows[3:]:
                                                                 cells = row.find_all('td')
                                                                              row_data = [cell.text.strip() for cell in cells]
                                                                                           endpoint = len(df)
                                                                                                        df.loc[endpoint] = row_data
                                                                                                                print(df)
                                                                                                                    else:
                                                                                                                                print("Error: Table not found on the page.")

                                                                                                                            else:
                                                                                                                                    print(f"Error: Unable to retrieve the page. Status Code: {response.status_code}")

