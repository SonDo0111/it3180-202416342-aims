import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestDiscount(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("Test DVD", cost=100.0))

    def test_discount_20_percent(self):
        self.assertAlmostEqual(self.cart.total_cost_with_discount(20), 80.0)

    def test_invalid_percent(self):
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(150)


if __name__ == "__main__":
    unittest.main()