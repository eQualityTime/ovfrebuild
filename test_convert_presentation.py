#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from pptx import Presentation
import convert_presentation 

class TestConvertPresentation(unittest.TestCase):

    def test_read_number_of_slides(self):
        prs = Presentation("tests/testinputs/CK20V2.pptx")
        self.assertEqual(len(prs.slides), 104)

    def test_name(self): 
        slide = Presentation("tests/testinputs/CK20V2.pptx").slides[0]
        self.assertEqual(convert_presentation.get_name(slide), u"Top page")

    def test_name2(self): 
        slide = Presentation("tests/testinputs/CK20V2.pptx").slides[2]
        self.assertEqual(convert_presentation.get_name(slide), u"")

    def test_inside(self): 
        slide = Presentation("tests/testinputs/CK20V2.pptx").slides[3]
        shapeA=slide.shapes[1]
        shapeB=slide.shapes[0]
        self.assertEqual(True,convert_presentation.is_first_inside_second(shapeA,shapeB))

    def test_outside(self): 
        slide = Presentation("tests/testinputs/CK20V2.pptx").slides[4]
        shapeA=slide.shapes[1]
        shapeB=slide.shapes[0]
        self.assertEqual(False,convert_presentation.is_first_inside_second(shapeA,shapeB))
 
    def test_how_many_shapes_arent_inside_in_order(self):
        slide = Presentation("tests/testinputs/CK20V2.pptx").slides[2]
        containers=convert_presentation.get_containers(slide)
        self.assertEqual(20,len(containers))
    
    def test_how_many_shapes_arent_inside_in_order_speed(self):
        for slide in Presentation("tests/testinputs/CK20V2.pptx").slides:
            print "here"
            containers=convert_presentation.get_containers(slide)
        self.assertEqual(19,len(containers))
        
        
#Todo - blank names 
        

if __name__ == '__main__':
    unittest.main()
