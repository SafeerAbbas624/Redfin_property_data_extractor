# print statement for reference and contact.
print("**\n***\n****\n*****\n******\n*******\n"
      "This bot is coded and developed by Mr.SAFEER ABBAS.\n "
      "https://safeerabbas624.github.io/safeerabbas/\n "
      "https://github.com/SafeerAbbas624\n"
      "*******\n******\n*****\n****\n***\n**")

from selenium.webdriver.common.by import By
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
import undetected_chromedriver as uc
from selenium import webdriver
import time
import csv
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import pandas.errors as Error
import urllib.request
# from fake_useragent import UserAgent


driver = Driver(uc=True, incognito=True)


res = []
# Reading input file 
df = pd.read_excel('input.xlsx')
for column in df.columns:
     
    # Storing the rows of a column 
    # into a temporary list
    li = df[column].tolist()
     
    # appending the temporary list
    res.append(li)
# Getting data from temporary list to different columns   
input_link = []
input_link.append(res[0])
input_link = input_link[0]
location = []
location.append(res[1])
location = location[0]
keyword = []
keyword.append(res[2])
keyword = keyword[0]
link_type = []
link_type.append(res[3])
link_type = link_type[0]

# Printing all column's list
print(input_link)
print(location)
print(keyword)
print(link_type)

# Opening link in browser in loop to get all one by one.
for link in input_link:
    
    
    # Opening browser
    
    driver.get(link)
    time.sleep(5)

    # Clicking on listings one by one
    for num in range(0, 100):

        # Dictionary for saving scraped data

        headings = {
                  'Location': [],
                  'Keyword': [],
                  'AgentName': [],
                  'AgentPhone': [],
                  'AgentEmail': [],
                  'Status': [],
                  'Address': [],
                  'Beds': [],
                  'Baths': [],
                  'SqFt': [],
                  'Price': [],
                  'EstPrice': [],
                  'Time on Redfin': [],
                  'MLS#': [],
                  'Lot Size': [],
                  'Property Type': [],
                  'Link': [], 
                  'Description': [],
                  'Images': [],
                  'Link Type': [],
                  }
        try:
            try:
                listing = driver.find_element(By.XPATH, f'//*[@id="MapHomeCard_{num}"]/div/div')
                listing.click()
                time.sleep(10)
            except NoSuchElementException:
                break
            driver.switch_to.window(driver.window_handles[1])
            headings['Location'] = location[num]
            headings['Keyword'] = keyword[num]
            headings['Link Type'] = link_type[num]
            time.sleep(8)
            # Scraping status
            status = driver.find_element(By.XPATH, '/html/body/div[1]/div[11]/div[2]/div[1]/div/div/div/div[1]/div[1]/span').text
            print(status)
            headings['Status'] = status
            # Scraping Agent details
            time.sleep(3)
            agentname = driver.find_element(By.XPATH, '//*[@class="agent-basic-details--heading"]/span').text
            print(agentname)
            headings['AgentName'] = agentname
            # Agent phone number
            try:
                time.sleep(3)
                agentphone = driver.find_element(By.XPATH, '//*[@class="listingContactSection"]').text
                agent_data = agentphone.split(':')
                # del agent_data[0]
                print(agent_data)
                agent_split = agent_data[1].split()
                print(agent_split)
                if '@' in agent_split[0]:
                    headings['AgentEmail'] = agent_split[0]
                    del agent_split[0]
                elif '@' in agent_split[-1]:
                    headings['AgentEmail'] = agent_split[-1]
                    del agent_split[-1]
                headings['AgentPhone'] = ' '.join(agent_split)
                time.sleep(3)
                print(headings['AgentPhone'])
                print(headings['AgentEmail'])
            except NoSuchElementException or IndexError:
                headings['AgentPhone'] = ''
                headings['AgentEmail'] = ''
                pass

            # Scraping Address
            try:
                time.sleep(3)
                address1 = driver.find_element(By.XPATH, '//*[@class="street-address"]').text
                address2 = driver.find_element(By.XPATH, '//*[@data-rf-test-id="abp-cityStateZip"]').text
                address = address1 + ' ' + address2
                headings['Address'] = address
                print(headings['Address'])
            except Exception:
                pass

            try:
                time.sleep(3)
                price = driver.find_element(By.XPATH, '//*[@data-rf-test-id="abp-price"]/div').text
                headings['Price'] = price
                print(headings['Price'])
            except Exception:
                pass
            

            try:
                time.sleep(3)
                est_price = driver.find_element(By.XPATH, '//*[@class="est-monthly-payment"]').text
                estprice = est_price.split()
                del estprice[0]
                headings['EstPrice'] = estprice
                print(headings['EstPrice'])
            except Exception:
                pass

            
            try:
                time.sleep(3)
                beds = driver.find_element(By.XPATH, '//*[@data-rf-test-id="abp-beds"]/div').text
                headings['Beds'] = beds
                print(headings['Beds'])
            except Exception:
                pass

            
            try:
                time.sleep(3)
                baths = driver.find_element(By.XPATH, '//*[@data-rf-test-id="abp-baths"]/div').text
                headings['Baths'] = baths
                print(headings['Baths'])
            except Exception:
                pass

            
            try:
                time.sleep(3)
                sqft = driver.find_element(By.XPATH, '//*[@data-rf-test-id="abp-sqFt"]/span').text
                headings['SqFt'] = sqft
                print(headings['SqFt'])
            except Exception:
                pass

            
            try:
                time.sleep(3)
                images = driver.find_element(By.XPATH, '//*[@id="photoPreviewButton"]/button/span[2]').text
                headings['Images'] = images
                print(headings['Images'])
            except Exception:
                pass

            
            try:
                time.sleep(3)
                page_link = driver.current_url
                headings['Link'] = page_link
                print(headings['Link'])
            except Exception:
                pass

            
            try:
                time.sleep(3)
                redfin = driver.find_element(By.XPATH, '//*[@id="content"]/div[11]/div[2]/div[9]/div/div/div/div/div/div[1]/div/div').text
                headings['Time on Redfin'] = redfin
                print(headings['Time on Redfin'])
            except Exception:
                pass


            
            try:
                time.sleep(3)
                mls = driver.find_element(By.XPATH, '//*[@class="ListingSource--mlsId"]').text
                headings['MLS#'] = mls
                print(headings['MLS#'])
            except Exception:
                pass


            try:
                time.sleep(3)
                lot_size = driver.find_element(By.XPATH, '//*[@id="basicInfo"]/div[1]/div/div[7]/div').text
                headings['Lot Size'] = lot_size
                print(headings['Lot Size'])
            except Exception:
                pass


            try:
                time.sleep(3)
                property_type = driver.find_element(By.XPATH, '//*[@id="content"]/div[11]/div[2]/div[9]/div/div/div/div/div/div[2]/div').text
                headings['Property Type'] = property_type
                print(headings['Property Type'])
            except Exception:
                pass


            try:
                time.sleep(3)
                description = driver.find_element(By.XPATH, '//*[@id="marketing-remarks-scroll"]/p/span').text
                headings['Description'] = description
                print(headings['Description'])
            except Exception:
                pass
            driver.close() # close the new tab
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(3)
        except Exception:
             pass


        for key in headings:
                if not headings[key]:
                    headings[key] = ['']
        all_data = pd.DataFrame.from_dict(headings)
        print(all_data)


        # Try Except condition not to get FileNotFoundError.
        try:
            # Opening Property data Excel file if present, and appending dataframe to it.
             with pd.ExcelWriter('Property_data.xlsx', mode='a', engine='openpyxl', if_sheet_exists="overlay") as writer:
                all_data.to_excel(writer, index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)
        except FileNotFoundError:
                # Writing new Court cases data file if not present in above code. Appending headers list also.
            with pd.ExcelWriter('Property_data.xlsx', mode='w') as writer:
                all_data.to_excel(writer, header=True, engine='openpyxl', index=False)
            


    if len(driver.window_handles) > 1:
            time.sleep(3)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(10)
    else:
        time.sleep(3)
        driver.quit()
        driver = Driver(uc=True, incognito=True)
    # driver.get(link)


driver.quit()
print('All data scraped against all links available in input file.')

        
