import json
import pickle
from collections import defaultdict
data = open('./result-3.json').read()
data = json.loads(data)
data = data['result']
j=0
for i in data:
	i['seg']='/Users/shreyajain/Downloads/coco-caption/segmented/'+str(j)+'.png'
	j+=1
with open('result-new.json', 'w') as fp:
	json.dump(data, fp)	
# org_caps = open('./annotations/captions_val2014.json').read()
# org_caps = json.loads(org_caps)
# org = org_caps['annotations']
# fr = open('imageid.pkl','rb')
# img = pickle.load(fr)
# caps = defaultdict(list)
# new = data['result']
# f=[]
# # for i in org:
# # 	caps[i['image_id']].append(i['caption'])
# # p=0
# # for j in new:
# # 	print(p)
# # 	for k,v in img.items():
# # 		if str(j['ImageID'][38:]) ==k:
# # 			j['true_captions'] = caps[v]
# # 	p+=1
# # with open('result-3.json', 'w') as fp:
# #     json.dump(data, fp)

# #print(img)
# f1 = []
# f2 = []
# f3 = []
# new = data['result']
# j=0
# for i in new:
# 	print(j)
# 	for k,v in img.items():
# 		r1,r2,r3={},{},{}
# 		if str(i['ImageID'][38:]) ==k:
# 			r1['image_id']=v
# 			r1['caption']=i['cap1']
# 			r2['image_id']=v
# 			r2['caption']=i['cap2']
# 			r3['image_id']=v
# 			r3['caption']=i['cap3']
# 			f1.append(r1)
# 			f2.append(r2)
# 			f3.append(r3)
# 	j+=1
# with open('result-4.json', 'w') as fp:
# 	json.dump(f1, fp)	
# with open('result-5.json', 'w') as fq:
# 	json.dump(f2, fq)		
# with open('result-6.json', 'w') as fw:
# 	json.dump(f3, fw)				
# j=0
# for i in new:
# 	if i['cap2'] is None:
# 		if i['cap3'] is not None:
# 			i['cap2'] = i['cap3']
# 		else:
# 			i['cap2'] = i['cap1']
# 	if i['cap3'] is None:
# 		if i['cap2'] is not None:
# 			i['cap3'] = i['cap2']
# 		else:
# 			i['cap3'] = i['cap1']
# 	if i['cap2'] is not None:
# 		j+=1
# print(j)

# # 	i['ImageID'] = 'http://images.cocodataset.org/val2014/' + i['ImageID']
# with open('result-2.json', 'w') as fp:
#     json.dump(data, fp)