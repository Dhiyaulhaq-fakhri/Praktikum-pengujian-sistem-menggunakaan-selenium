import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestInventory:
    """Kumpulan kasus uji fitur inventory & shopping cart."""

    def test_add_backpack_to_cart(self, driver):
        """
        TC-04: Login sebagai standard_user, tambah Backpack ke cart.
        Expected: badge keranjang menampilkan '1'.
        """
        # 1. Login dulu
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # 2. Tambah barang ke keranjang
        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack_to_cart()

        # 3. Assertion: badge cart harus '1'
        actual_badge = inventory_page.get_cart_badge_count()
        assert actual_badge == "1", (
            f"Badge cart tidak sesuai. Diharapkan '1', diterima '{actual_badge}'"
        )

    def test_logout_flow(self, driver):
        """
        TC-05: Login, lalu logout via burger menu.
        Expected: kembali ke halaman login dan tombol login tampil.
        """
        # 1. Login dulu
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # 2. Logout
        inventory_page = InventoryPage(driver)
        inventory_page.logout()

        # 3. Assertion 1: URL kembali ke login page
        expected_url = "https://www.saucedemo.com/"
        actual_url = inventory_page.get_current_url()
        assert actual_url == expected_url, (
            f"Logout gagal. Diharapkan '{expected_url}', diterima '{actual_url}'"
        )

        # 4. Assertion 2: tombol login tampil lagi
        assert login_page.find_element(LoginPage.LOGIN_BUTTON).is_displayed() is True, (
            "Tombol Login tidak tampil setelah logout!"
        )