import unittest

import jvav
from jvav_compat import JavBusUtil as CompatibleJavBusUtil


class Jvav30CompatibilityTest(unittest.TestCase):
    def test_expected_jvav_version(self):
        self.assertEqual(jvav.__version__, "3.0.0")

    def test_all_existing_utilities_accept_keyword_proxy_and_cache_options(self):
        utility_classes = (
            jvav.BaseUtil,
            jvav.DmmUtil,
            jvav.JavDbUtil,
            jvav.JavLibUtil,
            jvav.SukebeiUtil,
            jvav.TransUtil,
            jvav.WikiUtil,
            jvav.AvgleUtil,
        )
        for utility_class in utility_classes:
            with self.subTest(utility=utility_class.__name__):
                utility = utility_class(proxy_addr="http://127.0.0.1:7890", use_cache=False)
                self.assertEqual(utility.proxy_addr, "http://127.0.0.1:7890")
                self.assertFalse(utility.use_cache)

    def test_javbus_new_bus_auth_parameter_does_not_consume_proxy(self):
        utility = CompatibleJavBusUtil(
            bus_auth="test-cookie",
            proxy_addr="http://127.0.0.1:7890",
            use_cache=False,
        )
        self.assertEqual(utility.bus_auth, "test-cookie")
        self.assertEqual(utility.proxy_addr, "http://127.0.0.1:7890")
        self.assertFalse(utility.use_cache)
        self.assertEqual(utility.get_headers().get("Cookie"), "bus_auth=test-cookie;")

    def test_new_jvav_30_exports_are_available(self):
        self.assertTrue(hasattr(jvav, "RankUtil"))
        self.assertTrue(hasattr(jvav.JavDbUtil, "fuzzy_search_stars"))
        self.assertTrue(hasattr(jvav.RankUtil, "get_av_250_rank"))


if __name__ == "__main__":
    unittest.main()
