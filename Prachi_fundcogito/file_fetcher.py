from selenium import webdriver
from getpass import getpass  # to get password if we use command line login and password
import time
import zipfile
import os
import csv
from selenium.common.exceptions import NoSuchElementException
import shutil




XPATH_TO_CLICKABLE_FOLDERS = '//*[@id="content"]/div[1]/div[2]/div/div/div[2]/table/tbody/tr/td[3]/div/div'
XPATH_TO_FOLDER_TITLE = '//*[@id="content"]/div[1]/div[1]/div[2]/h2'
XPATH_TO_FOLDER_CHECK_ALL = '//*[@id="content"]/div[1]/div[2]/div/div[1]/div[2]/table/thead/tr/th[1]/label/div/span'
XPATH_TO_FOLDER_DOWNLOAD = '//*[@id="content"]/div[1]/div[2]/div/div[1]/div[1]/div/div[1]/div/span[1]/div'
FOLDER_PATH='/temp_file'

from cred_driver import prachi_credentials


# Objective 3 from the doc
def write_into_csv():
    '''
    This function peforms the retreval of the zip donwloaded in previous function
    It also unzip the folder and segrate the downloaded files
    This function writes the paths into the file.
    :return:
    '''

    if not os.path.exists('temp_file'):
        os.makedirs('temp_file')

    files = []
    for file in os.listdir("temp_file"):
        if file.endswith(".zip"):
            if os.path.isdir((os.path.abspath(os.getcwd())+'/'+file.replace('.zip','')+'/')):
                try:
                    print("Folder present Trying to place updated folder")
                    shutil.rmtree((os.path.abspath(os.getcwd())+'/'+file.replace('.zip','')+'/'))
                except:
                    print("Error while deleting directory ")
            zipfile.ZipFile(os.path.abspath(os.getcwd())+'/'+FOLDER_PATH+'/'+file).extractall(file.replace('.zip',''))
            FOLDER_NAME = file.replace('.zip','')
            # # r=root, d=directories, f = files
            for r, d, f in os.walk(FOLDER_NAME):
                for file in f:
                        files.append(os.path.join(r, file))
                        # This function can take care of uploading the files into S3 bucket
                        # simulation we can call the function here Objective 3

            try:
                os.remove(os.path.abspath(os.getcwd())+'/'+FOLDER_PATH+'/'+FOLDER_NAME+".zip")
            except:
                print("Error while deleting file ", FOLDER_NAME)


    with open('Folder_map.csv', mode='w') as path_file:
        map_writer = csv.writer(path_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for f in files:
            map_writer.writerow([f])

#objective 2
def scrape_share_folder(driver):
    '''
    This function helps to login into the page and calls other function to populate the main folder File_Store
    :return: No return just populate the folder
    '''


    print("Logged in successfully")
    print("Waiting for site to load...")
    print("scrapping folders now")
    scrape_folders(driver)

    # waits for all the files to be completed and returns the paths
    print("Waiting for files to download...")
    time.sleep(15)  # Add explicit wait, in case files are too small
    while True:
        downloading = wait_for_downloads(driver)
        if (len(downloading) == 0):
            break

    print("Downloading Finished")
    write_into_csv()


# Objective 2 maintaining root structures
def scrape_folders(driver):
    '''
    Function helps in the Lookup and pulling out the information within
    all the nested folders

    :param driver: Chroomium driver
    :return:
    '''
    folder_no = -1
    while True:
        clickable_folders = driver.find_elements_by_xpath(XPATH_TO_CLICKABLE_FOLDERS)
        driver.implicitly_wait(15)
        total_folders = len(clickable_folders)
        folder_no = folder_no + 1
        if (folder_no >= total_folders):
            break
        clickable_folders[folder_no].click()
        download_entire_folder(driver)
        driver.back()


def download_entire_folder(driver):
    '''
    This function helps in checking subpaths and downloadable folder

    :param driver: Chromium driver
    :return:
    '''
    try:
        folder_name = driver.find_elements_by_xpath(XPATH_TO_FOLDER_TITLE)[0].text
        driver.implicitly_wait(25)
        print("Scrapping '{}' folder".format(folder_name))
        check_all = driver.find_elements_by_xpath(XPATH_TO_FOLDER_CHECK_ALL)
        driver.implicitly_wait(25)
        check_all[0].click()
        download_button = driver.find_elements_by_xpath(XPATH_TO_FOLDER_DOWNLOAD)
        driver.implicitly_wait(25)
        download_button[0].click()
        print("Downloading '{}' as a zip...".format(folder_name))
    except:
        print("No folders to download in '{}'".format(folder_name))


def wait_for_downloads(driver):
    '''
    :param driver: Chromium driver
    :return: It exceutes the javascript.
    '''
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    return driver.execute_script("""
        return document.querySelector('downloads-manager')
        .shadowRoot.querySelector('#downloadsList')
        .items.filter(e => e.state === "IN_PROGRESS")
        .map(e => e.filePath || e.file_path || e.fileUrl || e.file_url);
        """)


# objective 1
def login_system():
    '''
    This file reads the credentials from the class and object declared in cred_driver.py file
    Try to login into the system on failure it exist the script displaying error
    if everything is successful it returns driver
    :return: driver with succesful login is returned
    '''

    username_get = prachi_credentials.username
    password = prachi_credentials.password
    sharefile_company_url = "https://fundcogito.sharefile.com"

    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': os.path.abspath(os.getcwd()) + '/temp_file'}
    chrome_options.add_experimental_option('prefs', prefs)

    # to download in the specifc folder
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(sharefile_company_url + "/home/shared")
    driver.implicitly_wait(15)

    try:

        username = driver.find_element_by_id("credentials-email")
        username.clear()
        username.send_keys(username_get)
        user_password = driver.find_element_by_id("credentials-password")
        user_password.clear()
        user_password.send_keys(password)
        driver.find_element_by_id("start-button").click()
        time.sleep(10)
    except NoSuchElementException:
        print("Elements could not be located in the Page")  # we can also log these errors in Production ready code
        driver.close()


    try:
        data=driver.find_element_by_xpath('//*[@id="applicationHost"]/div/div/form/div[2]/div')
        print("error"+str(data.text))

        driver.close()
        exit()
    except NoSuchElementException:
        ## error element is not found hence return the driver and succeful login

        return driver





if __name__ == '__main__':
    driver=login_system()
    scrape_share_folder(driver)
    driver.close()


