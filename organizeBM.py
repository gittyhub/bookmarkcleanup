def read_html(x):
  html = open(x,'r',encoding='utf-8')
  h = html.read()
  return h

def get_all_bm(html):
  l = []
  s = 1
  ff_anchor = 1
  while ff_anchor > 0:
    ff_anchor=html.find('A HREF="',s)
    fe_anchor=html.find('"',ff_anchor+8)
    bm = html[ff_anchor+8:fe_anchor]
    l.append(bm)
    s = ff_anchor+9
  return l

def list_only_dup(x):
  dup = set([d for d in x if x.count(d)>1])
  return dup

def rep(re,s): 
  for i in re:     
  s = (str(s).replace(i,'',1))  
  return s 


