from project.gallery import Gallery
from unittest import TestCase, main

class GalleryTests(TestCase):
    def setUp(self):
        self.gallery = Gallery("TestGallery", "TestCity", 100)

    def test_init(self):
        self.assertEqual("TestGallery", self.gallery.gallery_name)
        self.assertEqual("TestCity", self.gallery.city)
        self.assertEqual(100, self.gallery.area_sq_m)
        self.assertEqual(True, self.gallery.open_to_public)
        self.assertEqual({}, self.gallery.exhibitions)

    def test_gallery_name_setter(self):
        self.gallery.gallery_name = "NewName"
        self.assertEqual("NewName", self.gallery.gallery_name)
        with self.assertRaises(ValueError) as ex:
            self.gallery.gallery_name = "!@#$%^&*()"
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

    def test_city_setter(self):
        self.gallery.city = "NewCity"
        self.assertEqual("NewCity", self.gallery.city)
        with self.assertRaises(ValueError) as ex:
            self.gallery.city = "1City"
        self.assertEqual("City name must start with a letter!", str(ex.exception))

    def test_area_sq_m_setter(self):
        self.gallery.area_sq_m = 200
        self.assertEqual(200, self.gallery.area_sq_m)
        with self.assertRaises(ValueError) as ex:
            self.gallery.area_sq_m = -10
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

    def test_add_exhibition(self):
        self.assertEqual({}, self.gallery.exhibitions)
        self.assertEqual('Exhibition "TestExhibition" added for the year 2023.', self.gallery.add_exhibition("TestExhibition", 2023))
        self.assertEqual({"TestExhibition": 2023}, self.gallery.exhibitions)
        self.gallery.add_exhibition("AnotherExhibition", 2024)
        self.assertEqual({"TestExhibition": 2023, "AnotherExhibition": 2024}, self.gallery.exhibitions)
        self.assertEqual('Exhibition "TestExhibition" already exists.', self.gallery.add_exhibition("TestExhibition", 2023))

    def test_remove_exhibition(self):
        self.assertEqual({}, self.gallery.exhibitions)
        self.gallery.add_exhibition("TestExhibition", 2023)
        self.assertEqual({"TestExhibition": 2023}, self.gallery.exhibitions)
        self.assertEqual('Exhibition "AnotherExhibition" not found.', self.gallery.remove_exhibition("AnotherExhibition"))
        self.assertEqual('Exhibition "TestExhibition" removed.', self.gallery.remove_exhibition("TestExhibition"))
        self.assertEqual({}, self.gallery.exhibitions)

    def test_list_exhibitions(self):
        self.gallery.add_exhibition("TestExhibition1", 2025)
        self.gallery.add_exhibition("TestExhibition2", 2026)
        self.assertEqual(f"TestExhibition1: 2025\nTestExhibition2: 2026", self.gallery.list_exhibitions())
        self.gallery.open_to_public = False
        self.assertEqual('Gallery TestGallery is currently closed for public! Check for updates later on.', self.gallery.list_exhibitions())

if __name__ == '__main__':
    main()