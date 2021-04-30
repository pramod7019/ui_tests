from selenium.webdriver.common.by import By
from uitests.src.Helpers.LocatorDatabase.Locators import Locators


class MyAccountPageInfoSectionElements(Locators):

    def __init__(self):
        Locators.__init__(self, "MyAccountPageInfoSectionLocators")

    def get_page_header_title_text(self):
        return self.get_page_element(By.XPATH, "pageHeaderTitle")

    def get_info_title_text(self):
        return self.get_page_element(By.XPATH, "infoTitle")

    def get_aldo_personal_info_title_text(self):
        return self.get_page_element(By.XPATH, "aldoPersonalInfoTitle")

    def get_edit_info_button(self):
        return self.get_page_element(By.XPATH, "editInfoButton")

    def get_first_name(self):
        return self.get_page_element(By.XPATH, "firstName")

    def get_last_name(self):
        return self.get_page_element(By.XPATH, "lastName")

    def get_email(self):
        return self.get_page_element(By.XPATH, "email")

    def get_change_password(self):
        return self.get_page_element(By.XPATH, "changePassword")

    def get_forgot_password_modal_title(self):
        return self.get_page_element(By.XPATH, "forgotPasswordModalTitle")

    def get_sign_in_link_on_forgot_password_modal(self):
        return self.get_page_element(By.XPATH, "signInLinkForgotPasswordModal")

    def get_email_on_forgot_password_modal(self):
        return self.get_page_element(By.XPATH, "emailForgotPasswordModal")

    def get_reset_password_button(self):
        return self.get_page_element(By.XPATH, "resetPasswordButton")

    def get_reset_password_email_validation_text(self):
        return self.get_page_element(By.XPATH, "resetEmailValidationText")

    def get_reset_password_green_banner_text(self):
        return self.get_page_element(By.XPATH, "resetPasswordGreenBannerText")

    def get_reset_password_green_banner_close_button(self):
        return self.get_page_element(By.XPATH, "resetPaswdGreenBannerCloseButton")

    def get_close_forgot_password_modal(self):
        return self.get_page_element(By.XPATH, "closeForgotPasswordModal")

    def get_phone(self):
        return self.get_page_element(By.XPATH, "phone")

    def get_phone_extension(self):
        return self.get_page_element(By.XPATH, "phoneExtension")

    def get_dob_day(self):
        return self.get_page_element(By.XPATH, "dobDay")

    def get_dob_month(self):
        return self.get_page_element(By.XPATH, "dobMonth")

    def get_dob_year(self):
        return self.get_page_element(By.XPATH, "dobYear")

    def get_size(self):
        return self.get_page_element(By.XPATH, "sizeField")

    def get_first_name_validation_text(self):
        return self.get_page_element(By.XPATH, "firstnameValidationText")

    def get_last_name_validation_text(self):
        return self.get_page_element(By.XPATH, "lastNameValidationText")

    def get_phone_number_validation_text(self):
        return self.get_page_element(By.XPATH, "phoneNumberValidationText")

    def get_current_password(self):
        return self.get_page_element(By.XPATH, "currentPassword")

    def get_show_password(self):
        return self.get_page_element(By.XPATH, "showPassword")

    def get_update_button(self):
        return self.get_page_element(By.XPATH, "updateButton")

    def get_cancel_button(self):
        return self.get_page_element(By.XPATH, "cancelButton")

    def get_edit_password_button(self):
        return self.get_page_element(By.XPATH, "editPasswordButton")

    def get_old_password(self):
        return self.get_page_element(By.XPATH, "oldPassword")

    def get_new_password(self):
        return self.get_page_element(By.XPATH, "newPassword")

    def get_confirm_password(self):
        return self.get_page_element(By.XPATH, "confirmPassword")

    def get_edit_btn(self):
        return self.get_page_element(By.XPATH, "editbtn")

    def get_save_btn(self):
        return self.get_page_element(By.CSS_SELECTOR, "savebtn")

    def get_fn_ln(self):
        return self.get_page_element(By.CSS_SELECTOR, "fnln")

    def get_fn_ln_cis(self):
        return self.get_page_element(By.CSS_SELECTOR, "fnlncis")

    def get_size_p(self):
        return self.get_page_element(By.CSS_SELECTOR, "sizep")
