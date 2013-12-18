# -*- coding: utf-8
from HTMLParser import HTMLParser

class FortuneHTMLParser(HTMLParser):
  body = []

  valid = '<!DOCTYPE html><html><head><title>Fortunes</title></head><body><table><tr><th>id</th><th>message</th></tr><tr><td>11</td><td>&lt;script&gt;alert(&quot;This should not be displayed in a browser alert box.&quot;);&lt;/script&gt;</td></tr><tr><td>4</td><td>A bad random number generator: 1, 1, 1, 1, 1, 4.33e+67, 1, 1, 1</td></tr><tr><td>5</td><td>A computer program does what you tell it to do, not what you want it to do.</td></tr><tr><td>2</td><td>A computer scientist is someone who fixes things that aren\'t broken.</td></tr><tr><td>8</td><td>A list is only as strong as its weakest link. — Donald Knuth</td></tr><tr><td>0</td><td>Additional fortune added at request time.</td></tr><tr><td>3</td><td>After enough decimal places, nobody gives a damn.</td></tr><tr><td>7</td><td>Any program that runs right is obsolete.</td></tr><tr><td>10</td><td>Computers make very fast, very accurate mistakes.</td></tr><tr><td>6</td><td>Emacs is a nice operating system, but I prefer UNIX. — Tom Christaensen</td></tr><tr><td>9</td><td>Feature: A bug with seniority.</td></tr><tr><td>1</td><td>fortune: No such file or directory</td></tr><tr><td>12</td><td>フレームワークのベンチマーク</td></tr></table></body></html>'

  def handle_decl(self, decl):
    self.body.append("<!{d}>".format(d=decl))

  def handle_entityref(self, name):
    self.body.append("&{n};".format(n=name))

  def handle_starttag(self, tag, attrs):
    self.body.append("<{t}>".format(t=tag))

  def handle_data (self, data):
    self.body.append("{d}".format(d=data.strip()))

  def handle_endtag(self, tag):
    self.body.append("</{t}>".format(t=tag))

  def isValidFortune(self):
    print "Valid: {v}\n".format(v=self.valid)
    print "Input: {i}\n".format(i=''.join(self.body))
    print "Equal: {e}\n".format(e=str(self.valid == self.body))

    return self.valid == ''.join(self.body)