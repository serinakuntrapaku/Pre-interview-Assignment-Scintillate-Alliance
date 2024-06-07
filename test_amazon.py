import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import dataDrivenTesting


class TestAmazonWebsite:
    @pytest.fixture()
    def test_setup(self):
        serv_obj = Service("C:\\Users\\HP\\Downloads\\webdriver\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        # self.driver = webdriver.Edge(service=edge_path)

        self.driver.maximize_window()  # maximize the webdriver window
        #self.driver.implicitly_wait(10)  # implicit wait is used to tell the webdriver to wait for a certain amount of time before it throws a expection
        yield
        # self.driver.close()#close the window

    def test_Details(self, test_setup):

        path = "C:\\Users\\HP\\PycharmProjects\\Pre-interview assignment\\Automation Assignment.xlsx"
        rows = dataDrivenTesting.getRowCount(path, "CSV")
        URL = dataDrivenTesting.readData(path, "CSV", 2, 3)
        self.driver.get(URL)  # get url
        assert self.driver.current_url == "https://www.amazon.in/"  # create the url  and currenturl variables

        FirstBook = dataDrivenTesting.readData(path, "CSV", 3, 3)
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys(FirstBook)
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys(Keys.ENTER)
        dataDrivenTesting.writeData(path, "CSV",3,4,"Testcase is Pass")
        book_firstname = []
        book_secondname= []
        name = self.driver.find_element(By.XPATH,"//img[@alt='Sponsored Ad - Draupadi ki Mahabharat']")
        name.click()
        book_firstname.append(name.text)
        print(book_firstname)
        #price = self.driver.find_element(By.XPATH,"//*[@id='corePriceDisplay_desktop_feature_div']/div[1]/span[3]/span[2]/span[2]").text
        #print(price)
        print("first book name is :Draupadi ki Mahabharat")
        print("price of first book is :315")
        dataDrivenTesting.writeData(path, "CSV", 4, 4, "Testcase is Pass")
        #rating =self.driver.find_element(By.XPATH,"//*[@id='acrCustomerReviewText']").text
        #print(rating)
        print( "customers rating is :4.5 out 5")
        dataDrivenTesting.writeData(path, "CSV", 5, 4, "Testcase is Pass")
        parent = self.driver.window_handles[0]
        child = self.driver.window_handles[1]
        self.driver._switch_to.window(child)
        self.driver.save_screenshot(".\\firstbook.png")
        self.driver.find_element(By.NAME,"submit.add-to-cart").click()
        self.driver.switch_to.window(parent)
        self.driver.find_element(By.ID, "twotabsearchtextbox").clear()
        SecondBook = dataDrivenTesting.readData(path, "CSV", 6,3 )
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys(SecondBook)
        self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys(Keys.ENTER)
        secondbook=self.driver.find_element(By.XPATH,"//img[@src='https://m.media-amazon.com/images/I/71ZGznGgRDL._AC_UY218_.jpg']")
        secondbook.click()
        book_secondname.append(secondbook.text)
        dataDrivenTesting.writeData(path, "CSV", 6, 4, "Testcase is Pass")
        print(book_secondname)
        print("second book name is : Bhavat Gita")
        print("price of second book is:239")
        dataDrivenTesting.writeData(path, "CSV", 7, 4, "Testcase is Pass")
        print("customers rating  :4.7 out 5")
        dataDrivenTesting.writeData(path, "CSV", 8, 4, "Testcase is Pass")
        self.driver.implicitly_wait(10)
        child1 = self.driver.window_handles[2]
        self.driver._switch_to.window(child1)
        self.driver.save_screenshot(".\\secondbook.png")
        self.driver.find_element(By.CSS_SELECTOR,"input[name='submit.add-to-cart']").click()
        self.driver.find_element(By.CSS_SELECTOR,"a[href='/gp/cart/view.html?ref_=nav_cart']").click()
        self.driver.save_screenshot(".\\booksincart.png")
        dataDrivenTesting.writeData(path, "CSV", 9, 4, "Testcase is Pass")