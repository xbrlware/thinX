#!/usr/bin/env python

import unittest
from thinX import namespace
from thinX import xbrl


class Concepts(unittest.TestCase):

    def setUp(self):
        instance_file = "assets/abc-20130331.xml"
        xsd = xbrl.get_linkbase(instance_file, "xsd")
        pre_linkbase = xbrl.get_linkbase(instance_file, "pre")
        def_linkbase = xbrl.get_linkbase(instance_file, "def")
        cal_linkbase = xbrl.get_linkbase(instance_file, "cal")
        lab_linkbase = xbrl.get_linkbase(instance_file, "lab")
        xsd_tree = namespace.parse_xmlns(xsd)
        pre_tree = namespace.parse_xmlns(pre_linkbase)
        def_tree = namespace.parse_xmlns(def_linkbase)
        cal_tree = namespace.parse_xmlns(cal_linkbase)
        lab_tree = namespace.parse_xmlns(lab_linkbase)
        self.xsd_root = xsd_tree.getroot()
        self.pre_root = pre_tree.getroot()
        self.def_root = def_tree.getroot()
        self.cal_root = cal_tree.getroot()
        self.lab_root = lab_tree.getroot()
        self.schema = "abc-20130331.xsd"

    def test_clean_concepts(self):
        expected_concept = "abc_RemoveMe"

        removed_concepts = xbrl.clean_concepts(
            self.xsd_root,
            self.pre_root,
            self.def_root,
            self.cal_root,
            self.lab_root,
            self.schema
        )

        concepts_without_references = len(removed_concepts)

        self.assertEqual(2, concepts_without_references)
        self.assertIn(expected_concept, removed_concepts)
