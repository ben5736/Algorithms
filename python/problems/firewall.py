class FirewallRule(object):

  def __init__(self, address, is_allow):
    self.is_allow = is_allow

    # TODO: validate address format
    if '/' in address:
      self.address, self.mask_length = self.parse_cidr(address)
    else:
      self.mask_length = 32
      self.address = self.to_int(address)

  def parse_cidr(self, cidr):
    parts = cidr.split('/')
    mask_length = int(parts[1])
    address = self.to_int(parts[0])
    shift = 32 - mask_length
    address = address >> shift << shift
    return address, mask_length

  def to_int(self, address):
    parts = address.split('.')
    ip_int = 0
    for part in parts:
      int_part = int(part)
      ip_int = (ip_int << 8) | int_part
    return ip_int

  def examine(self, address):
    if '/' in address:
      return self.examine_cidr(address)
    else:
      return self.examine_ip(address)

  def examine_cidr(self, address):
    ip, mask_length = self.parse_cidr(address)
    if mask_length < self.mask_length:
      return None
    shift = 32 - self.mask_length
    ip = ip >> shift << shift
    if ip != self.address:
      return None
    else:
      return "ALLOW" if self.is_allow else "DENY"

  def examine_ip(self, address):
    ip_int = self.to_int(address)
    shift = 32 - self.mask_length
    ip_int = ip_int >> shift << shift
    if ip_int != self.address:
      return None
    else:
      return "ALLOW" if self.is_allow else "DENY"

class Firewall(object):

  def __init__(self, rules=[]):
    self.rules = rules

  def add_rule(self, rule):
    self.rules.append(rule)

  def examine(self, address):
    for rule in self.rules:
      outcome = rule.examine(address)
      if outcome:
        return outcome
    return "ALLOW"

import unittest

class Test(unittest.TestCase):

  def test1(self):
    f = Firewall([
      FirewallRule("192.168.100.0/24", True),
      FirewallRule("192.168.0.5/30", True),
      FirewallRule("8.8.8.8/0", False),
      FirewallRule("1.2.3.4", True)
      ])

    self.assertEqual(f.examine("192.168.100.1"), "ALLOW")
    self.assertEqual(f.examine("8.8.8.8"), "DENY")
    self.assertEqual(f.examine("192.168.100.54"), "ALLOW")
    self.assertEqual(f.examine("192.168.0.3"), "DENY")
    self.assertEqual(f.examine("192.168.0.4"), "ALLOW")
    self.assertEqual(f.examine("192.168.0.5"), "ALLOW")
    self.assertEqual(f.examine("192.168.0.6"), "ALLOW")
    self.assertEqual(f.examine("192.168.0.7"), "ALLOW")
    self.assertEqual(f.examine("192.168.0.8"), "DENY")

    self.assertEqual(f.examine("192.168.100.132/28"), "ALLOW")
    self.assertEqual(f.examine("192.16.100.132/28"), "DENY")

if __name__ == '__main__':
    unittest.main()