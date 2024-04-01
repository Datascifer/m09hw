import unittest
from magazinelover import MagazineLover

class MagazineLoverTestSuite(unittest.TestCase):
    
    def test_1_add_magazine(self):
        bl = MagazineLover('Mike', 'test@gmail.com', 'Fiction')
        bl.add_magazine('Jane Eyre', 4)
        self.assertIn('Jane Eyre', bl.book_list['book_name'].values)

    def test_2_add_magazine(self):
        bl = MagazineLover('Susan', 'test@gmail.com', 'Fiction')
        bl.add_magazine('Jane Eyre', 4)
        bl.add_magazine('Jane Eyre', 4)  # Attempt to add the same book twice
        self.assertEqual(len(bl.magazine_list), 1)  # Book should only appear once

    def test_3_has_read(self):
        bl = MagazineLover('Brenda', 'test@gmail.com', 'Fiction')
        bl.add_magazine('Jane Eyre', 4)
        self.assertTrue(bl.has_read('Jane Eyre'))

    def test_4_has_read(self):
        bl = MagazineLover('Jerry', 'test@gmail.com', 'Fiction')
        self.assertFalse(bl.has_read('Moby Dick'))  # Checking a book not in the list

    def test_5_num_magazines_read(self):
        bl = MagazineLover('Adam', 'test@gmail.com', 'Fiction')
        bl.add_magazine('Jane Eyre', 4)
        bl.add_magazine('Moby Dick', 3)
        self.assertEqual(bl.num_magazines, 2)  # Verifies the number of magazines read matches

    def test_6_fav_magazines(self):
        bl = MagazineLover('Martin', 'test@gmail.com', 'Fiction')
        bl.add_magazine('Jane Eyre', 4)
        bl.add_magazine('Moby Dick', 3) 
        bl.add_magazine('War and Peace', 5)
        fav_magazines = bl.fav_magazines()
        self.assertTrue(all(book['magazine_rating'] > 3 for index, magazine in fav_magazine.iterrows()))  # Checks if all favorite magazines have a rating above 3
        self.assertIn('War and Peace', fav_magazines['book_name'].values)
        self.assertNotIn('Moby Dick', fav_magazines['book_name'].values)

if __name__ == '__main__':
    unittest.main(verbosity=3)
    