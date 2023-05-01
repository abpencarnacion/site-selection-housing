from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Listing:

    def __init__(self, url):
        
        ## Initialize the url to the housing listing
        ## NOTE: This only works for now for housinganywhere.com ##
        self.url = url
    

    def initiate_driver(self):

        ## Initiate webdriver so we can use selenium to access URL
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--disable-dev-shm-using")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    
    def get_listing(self):

        ## Activate the selenium driver to access URL
        self.driver = self.initiate_driver()
        self.driver.implicitly_wait(5)

        ## Open url
        self.driver.get(self.url)

    
    def get_listing_price(self):

        ## Look for the monthly rent listed for the property
        self.price = self.driver.find_element_by_xpath('//*[@data-test-locator="Listing/Price/Price"]').text
    

    def get_listing_address(self):

        ## Look for the address/street of the property
        self.address = self.driver.find_element_by_xpath('//*[@data-test-locator="Redesign/Listing/ListingInfo/street"]').text
    

    def listing_main(self):

        self.get_listing()
        self.get_listing_price()
        self.get_listing_address()