from shopping_cart_unit_tests.shopping_cart import ShoppingCart
from unittest import TestCase, main


class ShoppingCartTests(TestCase):
    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart("Myshop", 10.0)

    def test_init(self):
        name = "Myshop"
        budget = 10.0
        shopping_cart = ShoppingCart(name, budget)
        self.assertEqual(name, shopping_cart.shop_name)
        self.assertEqual(budget, shopping_cart.budget)
        self.assertEqual({}, shopping_cart.products)

    def test_init_if_shop_name_does_not_start_with_uppercase_raise(self):
        with self.assertRaises(ValueError) as err:
            shop = ShoppingCart("name", 10.0)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(err.exception))

    def test_init_if_shop_name_does_not_contain_only_letters_raise(self):
        with self.assertRaises(ValueError) as err:
            shop = ShoppingCart("Name@23", 10.0)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(err.exception))

    def test_add_to_cart_if_product_price_greater_or_equal_to_100_raise(self):
        with self.assertRaises(ValueError) as err:
            shop = ShoppingCart("Name", 10.0)
            shop.add_to_cart("product_1", 100.0)
        self.assertEqual(f"Product product_1 cost too much!", str(err.exception))

        with self.assertRaises(ValueError) as err:
            shop = ShoppingCart("Name", 10.0)
            shop.add_to_cart("product_1", 101.0)
        self.assertEqual(f"Product product_1 cost too much!", str(err.exception))

    def test_add_to_cart_if_product_price_correct_returns_proper_string(self):
        actual = self.shopping_cart.add_to_cart("product_2", 99.0)
        expected = f"product_2 product was successfully added to the cart!"
        self.assertEqual(expected, actual)
        self.assertEqual({"product_2": 99.0}, self.shopping_cart.products)
        self.assertTrue("product_2" in self.shopping_cart.products)
        self.assertTrue(99.9, self.shopping_cart.products["product_2"])
        self.assertEqual(1, len(self.shopping_cart.products))

    def test_remove_if_product_exists(self):
        self.shopping_cart.add_to_cart("product_2", 99.0)
        product_to_remove = "product_2"
        actual = self.shopping_cart.remove_from_cart(product_to_remove)
        expected = f"Product {product_to_remove} was successfully removed from the cart!"
        self.assertEqual(expected, actual)
        self.assertTrue(product_to_remove not in self.shopping_cart.products)
        self.assertEqual(0, len(self.shopping_cart.products))

    def test_remove_if_product_does_not_exist_raise(self):
        with self.assertRaises(ValueError) as err:
            product_to_remove = "product_1"
            self.shopping_cart.remove_from_cart(product_to_remove)
        self.assertEqual(f"No product with name {product_to_remove} in the cart!", str(err.exception))

    def test_add_if_returns_new_cart(self):
        self.shopping_cart.add_to_cart("product_1", 2.0)
        new_shop = ShoppingCart("Another", 10.0)
        new_shop.add_to_cart("product_2", 1.0)
        new_shop_name = self.shopping_cart + new_shop
        result = {
            "product_1": 2.0,
            "product_2": 1.0
        }

        self.assertEqual("MyshopAnother", new_shop_name.shop_name)
        self.assertEqual(result, new_shop_name.products)

    def test_buy_products_if_total_sum_greater_than_budget_raises(self):
        self.shopping_cart.add_to_cart("product_1", 11.0)
        with self.assertRaises(ValueError) as err:
            self.shopping_cart.buy_products()
        self.assertEqual(f"Not enough money to buy the products! Over budget with 1.00lv!", str(err.exception))

    def test_buy_products_if_total_sum_less_than_budget(self):
        self.shopping_cart.add_to_cart("product_1", 5.0)
        actual = self.shopping_cart.buy_products()
        expected = f'Products were successfully bought! Total cost: 5.00lv.'
        self.assertEqual(expected, actual)

    def test_buy_products_if_total_sum_equal_budget(self):
        self.shopping_cart.add_to_cart("product_1", 10.0)
        actual = self.shopping_cart.buy_products()
        expected = f'Products were successfully bought! Total cost: 10.00lv.'
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
