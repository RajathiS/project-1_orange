from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.ID, "menu_pim_viewPimModule")     # Update element locator if necessary
        self.employee_list = (By.ID, "menu_pim_viewEmployeeList")  # Update element locator
        self.search_button = (By.ID, "searchBtn")             # Update element locator
        self.delete_button = (By.ID, "btnDelete")             # Update element locator
        self.confirm_delete = (By.ID, "dialogDeleteBtn")      # Update element locator
        self.success_message = (By.CSS_SELECTOR, ".message.success")  # Success message

    def navigate_to_pim(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.pim_menu)
        ).click()

    def delete_employee(self, employee_id):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//a[text()='{employee_id}']"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delete_button)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.confirm_delete)
        ).click()

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.success_message)
        ).text
