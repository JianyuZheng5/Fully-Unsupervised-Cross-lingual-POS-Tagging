'''
基于pre_process1的改版，如果一个词被标记了'***'，则进行多语言校准
若标记了词性，那就应该是这个词性
'''


src1 = 'DE'
src2 = 'EN'
src3 = 'DE'
src4 = 'FR'
tgt = 'AF'


def read_file(file):
    with open(file, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
        lines = [line.strip() for line in lines]
    return lines

def process(line1, line2, line3, line4):
    word_pos_count = dict()
    line = line1 + ' ' + line2 + ' ' + line3 + ' ' + line4
    line = line.strip().split()
    for word_pos in line:
        word, pos = word_pos.rsplit('_', 1)
        if word not in word_pos_count.keys():
            word_pos_count[word] = dict()
        word_pos_count[word][pos] = word_pos_count[word].get(pos, 0) + 1

    newline = ''
    for word_pos in line1.strip().split():
        word, pos = word_pos.rsplit('_', 1)
        if pos !='***':
            token = word + '_' + key
            newline = newline + ' '+ token

        else:
            if '***' in word_pos_count[word].keys():
                del word_pos_count[word]['***']
            if list(word_pos_count[word].keys()) == []:
                token = word + '_***'
            elif max(word_pos_count[word].values())==1:
                token = word + '_***'    #这里可以再细化一下，若word_pos_count[word].keys() ==1 就把那个词性给它
            else:
                max_value = 0
                for key in word_pos_count[word].keys():
                    if key !='***' and word_pos_count[word][key] >max_value:
                        max_value = word_pos_count[word][key]
                for key in word_pos_count[word].keys():
                    if word_pos_count[word][key] == max_value:
                        token = word + '_' + key
                        break
            newline = newline + ' ' + token


    return newline.strip()


lines1 = read_file(src1+'-'+tgt+'-target_annot.txt')
lines2 = read_file(src1+'-'+tgt+'-target_annot.txt')
lines3 = read_file(src1+'-'+tgt+'-target_annot.txt')
lines4 = read_file(src1+'-'+tgt+'-target_annot.txt')


results = []
for i in range(len(lines1)):
    line1 = lines1[i]
    line2 = lines2[i]
    line3 = lines3[i]
    line4 = lines4[i]

    newline = process(line1, line2, line3, line4)
    results.append(newline)

newfile = src1+'-'+tgt+'-target_annot_new.txt'
with open(newfile, 'w', encoding='utf-8') as fp:
    for line in results:
        fp.write(line+'\n')



