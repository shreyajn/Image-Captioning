
from pycocotools.coco import COCO
from pycocoevalcap.eval import COCOEvalCap
import matplotlib.pyplot as plt
import skimage.io as io
import pylab


import json
from json import encoder
encoder.FLOAT_REPR = lambda o: format(o, '.3f')

# set up file names and pathes


coco_captions ='./annotations/captions_val2014.json'
predict_captions = './result-5.json'

# download Stanford models
#!./get_stanford_models.sh

coco = COCO(coco_captions)
cocoRes = coco.loadRes(predict_captions)

# create cocoEval object by taking coco and cocoRes
cocoEval = COCOEvalCap(coco, cocoRes)

# evaluate on a subset of images by setting
# cocoEval.params['image_id'] = cocoRes.getImgIds()
# please remove this line when evaluating the full validation set
cocoEval.params['image_id'] = cocoRes.getImgIds()

# evaluate results
# SPICE will take a few minutes the first time, but speeds up due to caching
cocoEval.evaluate()

# print output evaluation scores
for metric, score in cocoEval.eval.items():
	print '%s: %.3f'%(metric, score)

# for eva in cocoEval.evalImgs:
# 	print 'ground truth captions'
# 	imgId = evals[0]['image_id']
# 	print(imgId)
# 	annIds = coco.getAnnIds(imgIds=imgId)
# 	anns = coco.loadAnns(annIds)
# 	coco.showAnns(anns)
# 	print 'CIDEr score %0.1f'%(evals[0]['CIDEr'])
# 	print 'Bleu_4 score %0.1f'%(evals[0]['Bleu_4'])
# 	print 'METEOR %0.1f'%(evals[0]['CIDEr'])
# 	print 'Generated Caption'
	# annIds = cocoRes.getAnnIds(imgIds=imgId)
	# anns = cocoRes.loadAnns(annIds)
	# coco.showAnns(anns)

