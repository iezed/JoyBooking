import os
import tempfile
import unittest

from database import init_db, create_booking, get_bookings_paginated, get_services


class TestDatabase(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.NamedTemporaryFile(
            prefix='joybooking_test_', suffix='.db', delete=False
        )
        self.db_path = tmp.name
        tmp.close()
        init_db(self.db_path)

    def tearDown(self):
        try:
            os.unlink(self.db_path)
        except OSError:
            pass

    def test_init_populates_services(self):
        services = get_services(self.db_path)
        self.assertGreaterEqual(len(services), 1)

    def test_create_and_paginate_booking(self):
        ok = create_booking('Alice', '123', 1, '2025-10-23 10:00', db_path=self.db_path)
        self.assertTrue(ok)
        bookings, total = get_bookings_paginated(1, 10, db_path=self.db_path)
        self.assertEqual(total, 1)
        self.assertEqual(len(bookings), 1)
        self.assertEqual(bookings[0]['client_name'], 'Alice')


if __name__ == '__main__':
    unittest.main()
