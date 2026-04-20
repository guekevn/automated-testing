from selenium.webdriver.common.by import By
from src.core.base_page import BasePage

class CommonPopups(BasePage):
    # Locator Standard Android Permission
    BTN_ALLOW = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")
    BTN_ALLOW_FOREGROUND = (By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")

    def grant_runtime_permissions(self, max_prompts=4):
        print("[STEP] Handling permission...")
        for _ in range(max_prompts):
            if self.is_visible(self.BTN_ALLOW, timeout=5):
                self.click(self.BTN_ALLOW)
            elif self.is_visible(self.BTN_ALLOW_FOREGROUND, timeout=5):
                self.click(self.BTN_ALLOW_FOREGROUND)
            else:
                break
