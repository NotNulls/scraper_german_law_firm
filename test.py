from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import selenium.common.exceptions as exception
import time
from selenium.webdriver.common.action_chains import ActionChains

option = Options()
option.headless = True
option.add_argument('window-size=1600x1000')

driver = webdriver.Firefox(options=option)
driver.get('https://www.sozialgerichtsbarkeit.de/entscheidungen?combine=&field_etyp_value=All&field_land_value=All&field_sozialgericht_value%5B0%5D=BSG&field_sozialgericht_value%5B1%5D=LSG%20FSB&field_sozialgericht_value%5B2%5D=LSG%20HES&field_sozialgericht_value%5B3%5D=LSG%20BWB&field_sozialgericht_value%5B4%5D=LSG%20BRB&field_sozialgericht_value%5B5%5D=LSG%20SAA&field_sozialgericht_value%5B6%5D=LSG%20HAM&field_sozialgericht_value%5B7%5D=LSG%20MVP&field_sozialgericht_value%5B8%5D=LSG%20NSB&field_sozialgericht_value%5B9%5D=LSG%20NRW&field_sozialgericht_value%5B10%5D=LSG%20RPF&field_sozialgericht_value%5B11%5D=LSG%20SAN&field_sozialgericht_value%5B12%5D=LSG%20FSS&field_sozialgericht_value%5B13%5D=LSG%20SHS&field_sozialgericht_value%5B14%5D=LSG%20FST&field_sozialgericht_value%5B15%5D=SG%20AC&field_sozialgericht_value%5B16%5D=SG%20AGB&field_sozialgericht_value%5B17%5D=SG%20A&field_sozialgericht_value%5B18%5D=SG%20AUR&field_sozialgericht_value%5B19%5D=SG%20BT&field_sozialgericht_value%5B20%5D=SG%20B&field_sozialgericht_value%5B21%5D=SG%20BS&field_sozialgericht_value%5B22%5D=SG%20HB&field_sozialgericht_value%5B23%5D=SG%20C&field_sozialgericht_value%5B24%5D=SG%20CB&field_sozialgericht_value%5B25%5D=SG%20DA&field_sozialgericht_value%5B26%5D=SG%20DE&field_sozialgericht_value%5B27%5D=SG%20LIP&field_sozialgericht_value%5B28%5D=SG%20DO&field_sozialgericht_value%5B29%5D=SG%20DD&field_sozialgericht_value%5B30%5D=SG%20DU&field_sozialgericht_value%5B31%5D=SG%20D&field_sozialgericht_value%5B32%5D=SG%20F&field_sozialgericht_value%5B33%5D=SG%20FF&field_sozialgericht_value%5B34%5D=SG%20FR&field_sozialgericht_value%5B35%5D=SG%20FD&field_sozialgericht_value%5B36%5D=SG%20SB&field_sozialgericht_value%5B37%5D=SG%20GE&field_sozialgericht_value%5B38%5D=SG%20GI&field_sozialgericht_value%5B39%5D=SG%20GTH&field_sozialgericht_value%5B40%5D=SG%20HAL&field_sozialgericht_value%5B41%5D=SG%20HH&field_sozialgericht_value%5B42%5D=SG%20H&field_sozialgericht_value%5B43%5D=SG%20HN&field_sozialgericht_value%5B44%5D=SG%20HI&field_sozialgericht_value%5B45%5D=SG%20IZ&field_sozialgericht_value%5B46%5D=SG%20KA&field_sozialgericht_value%5B47%5D=SG%20KS&field_sozialgericht_value%5B48%5D=SG%20KI&field_sozialgericht_value%5B49%5D=SG%20KO&field_sozialgericht_value%5B50%5D=SG%20K&field_sozialgericht_value%5B51%5D=SG%20KN&field_sozialgericht_value%5B52%5D=SG%20LA&field_sozialgericht_value%5B53%5D=SG%20L&field_sozialgericht_value%5B54%5D=SG%20HL&field_sozialgericht_value%5B55%5D=SG%20LG&field_sozialgericht_value%5B56%5D=SG%20MD&field_sozialgericht_value%5B57%5D=SG%20MZ&field_sozialgericht_value%5B58%5D=SG%20MA&field_sozialgericht_value%5B59%5D=SG%20MR&field_sozialgericht_value%5B60%5D=SG%20SM&field_sozialgericht_value%5B61%5D=SG%20M&field_sozialgericht_value%5B62%5D=SG%20MS&field_sozialgericht_value%5B63%5D=SG%20NB&field_sozialgericht_value%5B64%5D=SG%20NP&field_sozialgericht_value%5B65%5D=SG%20NDH&field_sozialgericht_value%5B66%5D=SG%20N&field_sozialgericht_value%5B67%5D=SG%20OL&field_sozialgericht_value%5B68%5D=SG%20OS&field_sozialgericht_value%5B69%5D=SG%20P&field_sozialgericht_value%5B70%5D=SG%20R&field_sozialgericht_value%5B71%5D=SG%20RT&field_sozialgericht_value%5B72%5D=SG%20HRO&field_sozialgericht_value%5B73%5D=SG%20SL&field_sozialgericht_value%5B74%5D=SG%20SN&field_sozialgericht_value%5B75%5D=SG%20SP&field_sozialgericht_value%5B76%5D=SG%20STD&field_sozialgericht_value%5B77%5D=SG%20SDL&field_sozialgericht_value%5B78%5D=SG%20HST&field_sozialgericht_value%5B79%5D=SG%20S&field_sozialgericht_value%5B80%5D=SG%20row&field_sozialgericht_value%5B81%5D=SG%20UL&field_sozialgericht_value%5B82%5D=SG%20WI&field_sozialgericht_value%5B83%5D=SG%20WUE&field_sachgebiet_value=KR&keys=&page=1')

suchen = driver.find_element(By.ID,'edit-submit-entscheidungen')
suchen.click()

wait = WebDriverWait(driver, 1)



cell_collector = []




try:
    count = 0
    while count < 3:
        
        try:
            driver.maximize_window()
            time.sleep(1)
            button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/button[1]')
            print ('BUTTON')
            ActionChains(driver).move_to_element(button).click(button).perform()
        except exception.NoSuchElementException:
            # The cookie popup was not found, or there's no need to accept cookies
            pass


        table_rows = driver.find_elements(By.XPATH, '//tr')
        print (len(table_rows))
        # ActionChains(driver).move_to_element(table_rows)

        

        for row_cell in table_rows:

            

            row_cell = driver.find_elements(By.TAG_NAME,'td')

            cell_data = []
            

            for cell in row_cell:
                
                if cell.find_elements(By.TAG_NAME, 'a'):
                    href = cell.find_element(By.TAG_NAME, 'a')
                    href_attribute = href.get_attribute("href")
                    pdf_link = href_attribute.replace('#suchwort=','') + '/pdf'
                    cell_data.append(href_attribute)
                    cell_data.append(pdf_link)
                else:
                    text = cell.text
                    cell_data.append(text)
                    
                
            print(cell_data) 
            
            
            try:
                next_button = driver.find_element(By.XPATH, '//*[@title="Zur nächsten Seite"]')
                if next_button:
                    next_button.click()
                    count += 1
            except Exception as e:
                print("No more pages to visit")
                break  # Break the loop when no more pages are available
            
            
        
            cell_collector.append(cell_data[1:])   
    
    print (count)

        

finally:
    driver.quit

data_collector = list(row_cells[3:] for row_cells in cell_collector[1:])
            
print (data_collector)


#labels = ['Erste Instanz','Aktenzeichen (1. Instanz)','Datum (1. Instanz)','Zweite Instanz', 'PAGE_URL','Aktenzeichen (2. Instanz)', 'PDF_URL','Datum (2. Instanz)','Aktenzeichen (3. Instanz)','Datum (3. Instanz)','Gericht', 'Erstellt']

df = pd.DataFrame(cell_collector)
df.to_csv('scraped_data.csv',index=False)



