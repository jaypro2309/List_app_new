from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
import time


class SetData():

    def __init__(self, driver):
        self.driver = driver

    def case1(self): #This is for splash screen and plan screen.
        try:
            for i in range(3):
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable
                                                     ((AppiumBy.ID, "com.l:id/next_page_button"))).click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable
                                                     ((AppiumBy.ID, "com.l:id/premium_close_iv"))).click()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable
                                                     ((AppiumBy.ID, "com.l:id/button_agree"))).click()
        except:
            print("skip the case1.")

    def case2(self, name): #this is for create the main list name.

        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                                ((AppiumBy.CLASS_NAME,"android.view.ViewGroup"))).click()

        except:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable
                                                ((AppiumBy.ID, "com.l:id/list_of_list_fab"))).click()
            self.driver.hide_keyboard()
            name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                                 ((AppiumBy.ID, "com.l:id/create_list_et"))).send_keys(name)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                                 ((AppiumBy.ID, "com.l:id/create_list_create_btn"))).click()

    def case4(self): #this is for adding alrady present item in the list.
        try:
            # self.driver.hide_keyboard()j
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable
                                                ((AppiumBy.ID, "com.l:id/item_list_main_layout"))).click()
        except:
            print("skip the case4.")

    def case5(self): #this is for add select item in the list.
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable
                                                ((AppiumBy.ID, "com.l:id/shopping_list_fab"))).click()
        except:
            print("Skip the case5.")

    def case6(self): #this is for select items.
        try:
            for j in range(2):
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable
                                                ((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]"))).click()
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable
                                                ((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]"))).click()
        except:
            print("Skip the case6.")

    def case7(self): #to add in the list.
        try:
            self.driver.hide_keyboard()
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable
                                                ((AppiumBy.ID, "com.l:id/add_product_fab"))).click()
        except:
            print("Skip the case7.")

    def d_case1(self): #for remove the item list.
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                                 ((AppiumBy.ID, "com.l:id/item_prompter_quantity_bar_2"))).click()
        except:
            print("Delete function skip.")

    def check_list(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                                 ((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.ImageView[1]"))).click()
        except:
            print("check button does not work.")