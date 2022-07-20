import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(120, 50, 100) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.infer_breach(70, 50, 100) == 'NORMAL')

  def test_passive_cooling_as_per_coolingType(self):
      self.assertTrue(typewise_alert.passive_cooling('PASSIVE_COOLING') == (0,45))
      self.assertTrue(typewise_alert.passive_cooling('MED_ACTIVE_COOLING') == None)
      self.assertTrue(typewise_alert.passive_cooling('HI_ACTIVE_COOLING') == None)
  
  def test_hi_active_cooling_as_per_coolingType(self):
      self.assertTrue(typewise_alert.hi_active_cooling('PASSIVE_COOLING') == None)
      self.assertTrue(typewise_alert.hi_active_cooling('MED_ACTIVE_COOLING') == None)
      self.assertTrue(typewise_alert.hi_active_cooling('HI_ACTIVE_COOLING') == (0,35))
      
  def test_med_active_cooling_as_per_coolingType(self):
      self.assertTrue(typewise_alert.med_active_cooling('PASSIVE_COOLING') == None)
      self.assertTrue(typewise_alert.med_active_cooling('MED_ACTIVE_COOLING') == (0,40))
      self.assertTrue(typewise_alert.med_active_cooling('HI_ACTIVE_COOLING') == None)

  def test_classify_temperature_breach_as_per_coolingType_temperature(self):
      self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 25) == 'NORMAL')
      self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 50) == 'TOO_HIGH')
      self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', -5) == 'TOO_LOW')
      self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 25) == 'NORMAL')
      self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 50) == 'TOO_HIGH')
      self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', -5) == 'TOO_LOW')
      self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 25) == 'NORMAL')
      self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 50) == 'TOO_HIGH')
      self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', -5) == 'TOO_LOW')

  def test_is_alertcontroller(self):
      self.assertTrue(typewise_alert.is_alertcontroller('TO_CONTROLLER', 'TOO_HIGH') == 0) 
      self.assertTrue(typewise_alert.is_alertcontroller('TO_CONTROLLER', 'TOO_LOW') == 0)
      self.assertTrue(typewise_alert.is_alertcontroller('TO_CONTROLLER', 'NORMAL') == 0)
      self.assertTrue(typewise_alert.is_alertcontroller('TO_EMAIL', 'TOO_HIGH') == None)
      self.assertTrue(typewise_alert.is_alertcontroller('TO_EMAIL', 'TOO_LOW') == None)
      self.assertTrue(typewise_alert.is_alertcontroller('TO_EMAIL', 'NORMAL') == None)
      
  def test_is_alertemail(self):
      self.assertTrue(typewise_alert.is_alertemail('TO_EMAIL', 'TOO_HIGH') == 0)
      self.assertTrue(typewise_alert.is_alertemail('TO_EMAIL', 'TOO_LOW') == 0)
      self.assertTrue(typewise_alert.is_alertemail('TO_EMAIL', 'NORMAL') == 0)
      self.assertTrue(typewise_alert.is_alertemail('TO_CONTROLLER', 'TOO_HIGH') == None)
      self.assertTrue(typewise_alert.is_alertemail('TO_CONTROLLER', 'TOO_LOW') == None)
      self.assertTrue(typewise_alert.is_alertemail('TO_CONTROLLER', 'NORMAL') == None)
      


if __name__ == '__main__':
  unittest.main()

