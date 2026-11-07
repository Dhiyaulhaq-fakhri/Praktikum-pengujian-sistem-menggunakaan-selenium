from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object untuk halaman Inventory SauceDemo."""

    URL = "https://www.saucedemo.com/inventory.html"

    # ============================================================
    # ELEMENT LOKATOR (Menggunakan Relative XPath)
    # ============================================================
    ADD_BACKPACK_BUTTON = (
        By.XPATH,
        "//button[contains(@data-test, 'add-to-cart-sauce-labs-backpack')]",
    )
    CART_BADGE = (By.XPATH, "//span[@class='shopping_cart_badge']")
    BURGER_MENU_BUTTON = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    LOGOUT_LINK = (By.XPATH, "//a[@id='logout_sidebar_link']")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        """Membuka halaman inventory secara langsung."""
        self.driver.get(self.URL)

    def add_backpack_to_cart(self):
        """Menambahkan produk Sauce Labs Backpack ke keranjang."""
        self.click(self.ADD_BACKPACK_BUTTON)

    def get_cart_badge_count(self) -> str:
        """Mengambil teks angka di badge keranjang belanja."""
        return self.get_text(self.CART_BADGE)

    def logout(self):
        """Klik burger menu lalu pilih Logout."""
        self.click(self.BURGER_MENU_BUTTON)
        # Tambahkan explicit wait khusus untuk memastikan menu sidebar sudah muncul
        self.wait.until(EC.visibility_of_element_located(self.LOGOUT_LINK))
        self.click(self.LOGOUT_LINK)