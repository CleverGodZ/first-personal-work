import jieba
import io

# fp1=r'D:/python/a.txt'
# outph=r'D:/python/out.txt'
# f=open(fp1,'r',encoding='utf-8')
# txt=f.read().strip()
# f.close()
#
# words=jieba.lcut(txt)
# f=open(outph,'w',encoding='utf-8')
# for word in words:
#     f.write(word)
#     f.write('\n')
# f.close()
txt = io.open("评论.txt","r",encoding='utf-8').read()
#第二题去标点，统计词频
bd='[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+，。！？“”《》：、． '
counts={ }
for i in bd:
    txt=txt.replace(i,'')   #字符串替换去标点符号
words=jieba.lcut(txt)  #分词
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1   #所有词全统计
items=list(counts.items())

items.sort(key=lambda x:x[1],reverse=True)
for i  in range(50):
    word,count=items[i]
    print("{0:>10}:{1:<5}".format(word,count))