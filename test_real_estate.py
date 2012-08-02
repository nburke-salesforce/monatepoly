import unittest
import real_estate as re

class TestColoredProperty(unittest.TestCase):
	def setUp(self):
		self.purps = re.ColoredPropertyGroup((1, 2))
	def test_init(self):
		#make sure shit is set up correctly
		self.assertEqual(self.purps.building_materials["houses"], 32)
		self.assertEqual(self.purps.building_materials["hotels"], 12)
	def test_monopoly(self):
		self.assertFalse(self.purps.is_monopoly())
	def test_build(self):
		self.purps.location_dict[1] = "bill"
		self.purps.location_dict[2] = "bill"
		self.assertFalse(self.purps.build(1, "ted")[0])
		self.assertEquals(self.purps.build(1, "ted")[1], "You don't own this property.")
if __name__ == '__main__':
	unittest.main()
		
