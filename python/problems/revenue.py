class RevTracker(object):

  def __init__(self):
    self.next_customer_id = 0
    self.customer_rev = {}
    self.rev_customer = TreeMap()

  def insert(self, revenue):
    customer_id = self.next_customer_id
    self.next_customer_id += 1
    self.customer_rev[customer_id] = revenue
    if revenue not in self.rev_customer:
      self.rev_customer[revenue] = {customer_id}
    else:
      self.rev_customer[revenue].add(customer_id)
    return customer_id

  def insert(self, revenue, referrerID):
    if referrerID >= self.next_customer_id:
      raise Exception('unknown referrrID')

    old_rev = self.customer_rev[referrerID]
    self.rev_customer[old_rev].remove(referrerID)

    new_rev = old_rev + revenue
    self.customer_rev[referrerID] = new_rev
    self.rev_customer[new_rev].add(referrerID)
    return self.insert(revenue)


  def getKLowestRevenue(self, k, targetRevenue):
    ret = []
    if k == 0:
      return ret
    cur_tar = targetRevenue
    while True:
      cur_tar = self.rev_customer.higherKey(cur_tar)
      if cur_tar is None:
        break
      for customer_id in self.rev_customer[cur_tar]:
        ret.append(customer)
        if len(ret) == k:
          return ret

    return ret
