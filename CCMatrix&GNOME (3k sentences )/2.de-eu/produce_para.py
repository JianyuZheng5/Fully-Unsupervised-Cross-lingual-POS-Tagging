#一定要确认好源语言和目标语言都是谁！！！
import random

random.seed(825)

src_file = r'GNOME.de-eu.de'
tgt_file = r'GNOME.de-eu.eu'
sen_num = 3000




with open(src_file, 'r', encoding='utf-8') as f1:
    src_lines = f1.readlines()
with open(tgt_file, 'r', encoding='utf-8') as f2:
    tgt_lines = f2.readlines()


NUM = [i for i in range(len(src_lines))] 
random.shuffle(NUM)


src_results, tgt_results = [], []
for idd in NUM:
    src_line = src_lines[idd].strip()
    tgt_line = tgt_lines[idd].strip()
    if 50>=len(src_line.split())>= 5 and 50>=len(tgt_line.split())>= 5 and \
    src_line not in src_results and tgt_line not in tgt_results and \
    'www' not in src_line and 'www' not in tgt_line:
        src_results.append(src_line)
        tgt_results.append(tgt_line)
    if len(src_results) == sen_num*2:
        break

#write
with open("dev.de.sgm", 'w', encoding='utf-8') as fp:
    for line in src_results[:sen_num]:
        fp.write(line+'\n')
        
with open("test.de.sgm", 'w', encoding='utf-8') as fp:
    for line in src_results[sen_num:]:
        fp.write(line+'\n') 
        
with open("dev.eu.sgm", 'w', encoding='utf-8') as fp:
    for line in tgt_results[:sen_num]:
        fp.write(line+'\n')
        
with open("test.eu.sgm", 'w', encoding='utf-8') as fp:
    for line in tgt_results[sen_num:]:
        fp.write(line+'\n')     
    




