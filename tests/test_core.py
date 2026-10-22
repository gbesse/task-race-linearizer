import unittest
from task_race_linearizer import run
class DomainTests(unittest.TestCase):
 def test_conflicting_terminal_winners(self):
  self.assertFalse(run({'operations':[{'id':'c','op':'cancel','call':0,'return':4,'result':'cancelled'},{'id':'f','op':'complete','call':1,'return':5,'result':'completed'}]})['linearizable'])
 def test_cancel_can_win_overlap(self):
  r=run({'operations':[{'id':'f','op':'complete','call':0,'return':5,'result':'cancelled'},{'id':'c','op':'cancel','call':1,'return':4,'result':'cancelled'}]});self.assertEqual(r['order'],['c','f'])
 def test_real_time_order_enforced(self):
  r=run({'operations':[{'id':'p','op':'poll','call':0,'return':1,'result':'completed'},{'id':'f','op':'complete','call':2,'return':3,'result':'completed'}]});self.assertFalse(r['linearizable'])
 def test_input_roundtrip(self):
  r=run({'operations':[{'id':str(i),'op':op,'call':i*2,'return':i*2+1,'result':state} for i,(op,state) in enumerate([('request_input','input_required'),('resume','working'),('complete','completed')])]});self.assertTrue(r['linearizable'])
 def test_zero_length_interval_rejected(self):
  with self.assertRaises(ValueError):run({'operations':[{'id':'p','op':'poll','call':0,'return':0,'result':'working'}]})
