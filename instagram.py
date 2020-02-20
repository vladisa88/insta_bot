from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class InstaBot:

    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        

    def _login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(3)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_elements_by_tag_name('button')[1].click()
        sleep(3)
        self.driver.find_element_by_xpath('//button[contains(text(), "Не сейчас")]').click()
        sleep(5)
    
    def _open_user_page(self):
        # open user page 
        self.driver.find_element_by_xpath('//a[contains(@href, "/{}")]'.format(self.username)).click()
        sleep(4)

    def _open_user_page_not_login(self, username):
        self.driver.get('https://instagram.com/{}'.format(username))
        sleep(3)

    def _get_following(self):
        # number of following
        max = int(self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text)
        # open "following" window
        self.driver.find_element_by_xpath('//a[contains(@href,"/following")]').click()
        sleep(4)
        # get "following" element 
        followingList = self.driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowingInList = len(followingList.find_elements_by_css_selector('li'))
        # focus on "following"
        followingList.click()
        actionChain = webdriver.ActionChains(self.driver)
        sleep(2)
        while (numberOfFollowingInList < max):
            # do until reached number of following  
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()        
            numberOfFollowingInList = len(followingList.find_elements_by_css_selector('li'))
            sleep(1.5)
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            # focus on "following"
            followingList.click()          
            sleep(1)
        
        following = []
        for user in followingList.find_elements_by_css_selector('li'):
            # get following links
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            following.append(userLink)
            if (len(following) == max):
                break
        # close dialog window
        followingList.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
        return following

    def _get_followers(self):
        sleep(4)
        # number of followers
        max = int(self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text)
        # open "followers" window
        self.driver.find_element_by_xpath('//a[contains(@href,"/followers")]').click()
        sleep(4)
        # get "followers" dialog window 
        followersList = self.driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
        # focus on "followers"
        followersList.click()
        actionChain = webdriver.ActionChains(self.driver)
        sleep(2)
        while (numberOfFollowersInList < max-1):
            # do until reached number of followers 
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            sleep(2)
            print(max)        
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)
            sleep(2)
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            # focus on "followers"
            sleep(2)
            followersList.click()          
            sleep(2)
        
        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            print('i am here')
            # get followers links
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            followers.append(userLink)
            print('heeere')
            if (len(followers) == max):
                break
        # close dialog window
        followersList.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
        return followers

    def get_unfollowers(self, login=True, username=None):
        self._login()
        self._open_user_page_not_login(username) if login is False else self._open_user_page()
        following = self._get_following()
        followers = self._get_followers()
        bitches = []
        for i in following:
            if i not in followers:
                bitches.append(i)
        return bitches




