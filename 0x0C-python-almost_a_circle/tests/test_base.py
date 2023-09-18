#!/usr/bin/python3
"""Base Class unittest"""
import unittest
import json
import os
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestBaseclass(unittest.Testcase):

    def test_class(self):
        """base class unittest"""
        b0 = Base()
        self.assertIsInstance(b0, base)

    def test_base_id(self):
        """unittest for base class ids"""
        b1 = base()
        b2 = base()
        self.assertEqual(b1.id, 5)
        self.assertEqual(b2.id, 6)

    def test_custom_id(self):
        """test base custom id"""
        b3 = base(12)
        self.assertEqual(b3.id, 12)

    def test_to_json_string(self):
        """test to_json_string method"""
        r = Rectangle(12, 8, 4, 6)
        r_dict = r.to_dictionary()
        json_str = Base.to_json_string([r_dict])
        self.assertEqual(json_str, json.dumps([r_dict])
            
    def test_from_json_string(self):
        """test from_json_string"""
        r = rectangle(12, 8, 4, 6)
        r_dict = self.r.to_dictionary()
        json_str = Base.to_json_string
        obj_list = base.from_jsom_string(jsnon_str)
        self.assertEqual(obj_list, [r_dict])

    def test_save_to_file(self):
        """Test save to file method"""
        filename = "Rectangle.json"
        Rectangle.save_to_file([self.r])
        with open(filename, 'r') as f:
            file_contents = f.read()
        self.assertEqual(file_contents, Base.to_json_string([self.r]))

    def test_load_from_file(self):
        """test load from_file method"""
        filename = "Rectangle.json"
        os.remove(filename)
        Rectangle.save_to_file([self.rect])
        rect_list = Rectangle.load_from_file()
        self.assertEqual(rect_list[0].to_dictionary(),
                        self.rect.to_dictionary())


if __name__ == '__main__':
    unittest.main()
