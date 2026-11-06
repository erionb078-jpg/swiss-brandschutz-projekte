import sys,importlib.util
target,tfile=sys.argv[1],sys.argv[2]
spec=importlib.util.spec_from_file_location('t',tfile);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
s=open(target).read();miss=0
for de,en in m.T:
    c=s.count(de)
    if c==0: print('MISS:',de[:90]);miss+=1;continue
    s=s.replace(de,en)
open(target,'w').write(s);print(target,'pairs',len(m.T),'miss',miss)
