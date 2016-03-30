import sys, operator

def tokenize(s, glen):
  g2 = set()
  for i in xrange(len(s)-(glen-1)):
    g2.add(s[i:i+glen])
  return g2

def dice_grams(g1, g2): return (2.0*len(g1 & g2)) / (len(g1)+len(g2))

def dice(n, s1, s2): return dice_grams(tokenize(s1, n), tokenize(s2, n))

def main():
  print("TEST")
  GRAM_LEN = 4
  scores = {}
  for i in xrange(1,len(sys.argv)):
    for j in xrange(i+1, len(sys.argv)):
      s1 = sys.argv[i]
      s2 = sys.argv[j]
      score = dice(GRAM_LEN, s1, s2)
      scores[s1+":"+s2] = score
  for item in sorted(scores.iteritems(), key=operator.itemgetter(1)):
    print(item)
