import pprint
import sys
import functools
from operator import itemgetter, attrgetter
#index = sys.argv[1]
global cv_res
global threshold
threshold=0
max_cv_res = {
    "positive_positive": 0,
    "positive_negative": 0,
    "negative_positive": 0,
    "negative_negative": 0,
    "contradictory": 0,
    "total": 0,
    "threshold": 0,
    "max_index":0,
    "max_sum":0,
    "max_accuracy":0,
}
index = 10;
i = 0
l_arr=[]
threshold=0.7
for i in range(0,20):
    max_index=11
    threshold=threshold+0.1
    for k in range(0,10):
        exec(compile(open("test_implication_changed.py", "rb").read(), "test_implication_changed.py", 'exec'), globals(), locals())
        max_cv_res=cv_res
        max_cv_res["threshold"]=threshold
        max_cv_res["max_sum"]=cv_res["positive_positive"] + cv_res["negative_negative"]
        max_cv_res["max_accuracy"]=max_cv_res["max_sum"]/max_cv_res["total"]
        l_arr.append(max_cv_res)
max_accuracy=0
#sorted(l_arr,key=itemgetter(0))
best_accuracy_index =0
for i in range(0, 200):
    if(max_accuracy<=l_arr[i]["max_accuracy"]):
        max_accuracy=l_arr[i]["max_accuracy"]
        best_accuracy_index=i;
    print(l_arr[i])
TP=l_arr[best_accuracy_index]["positive_positive"]
TN=l_arr[best_accuracy_index]["negative_negative"]
FP=l_arr[best_accuracy_index]["negative_positive"]
FN=l_arr[best_accuracy_index]["positive_negative"]
precision=TP/(FP+TP)
recall = TP/(TP+FN)
F1 = 2*precision*recall/(precision+recall)
print('True Positive :\t', TP)
print('True Negative :\t', TN)
print('False Positive :\t', FP)
print('False Negative :\t', FN)
print('True Positive Rate(TPR) :\t', TP/(TP+FN))
print('True Negative Rate(TNR) :\t', TN/(TN+FP))
print('Negative Predictive Value(NPV) :\t', TN/(TN+FN))
print('False Positive Rate(FPR :\t', FP/(FP+TN))
print('FDR :\t', FP/(FP+TP))
print('Accuracy :\t', (TP+TN)/(TP+TN+FP+FN))
print('PPV(precision) :\t', TP/(FP+TP))
print('F1 :\t', F1)
print('Recall :\t', TP/(TP+FN))
print('Max accuracy  :\t', max_accuracy, '\n')


for k, v in cv_res.items():
        max_cv_res[k]=0
threshold=l_arr[best_accuracy_index]["threshold"]
for i in range(0,11):
    max_index=i+1;
    for k in range(0,10):
        exec(compile(open("test_implication_changed.py", "rb").read(), "test_implication_changed.py", 'exec'), globals(), locals())
        max_cv_res=cv_res
        max_cv_res["threshold"]=threshold
        max_cv_res["max_sum"]=cv_res["positive_positive"] + cv_res["negative_negative"]
        max_cv_res["max_accuracy"]=max_cv_res["max_sum"]/max_cv_res["total"]
        l_arr.append(max_cv_res)

max_accuracy=0;
for i in range(0, 200):
    if(max_accuracy<=l_arr[i]["max_accuracy"]):
        max_accuracy=l_arr[i]["max_accuracy"]
        best_accuracy_index=i;
    print(l_arr[i])
TP=l_arr[best_accuracy_index]["positive_positive"]
TN=l_arr[best_accuracy_index]["negative_negative"]
FP=l_arr[best_accuracy_index]["negative_positive"]
FN=l_arr[best_accuracy_index]["positive_negative"]
precision=TP/(FP+TP)
recall = TP/(TP+FN)
F1 = 2*precision*recall/(precision+recall)
print('True Positive :\t', TP)
print('True Negative :\t', TN)
print('False Positive :\t', FP)
print('False Negative :\t', FN)
print('True Positive Rate(TPR) :\t', TP/(TP+FN))
print('True Negative Rate(TNR) :\t', TN/(TN+FP))
print('Negative Predictive Value(NPV) :\t', TN/(TN+FN))
print('False Positive Rate(FPR :\t', FP/(FP+TN))
print('FDR :\t', FP/(FP+TP))
print('Accuracy :\t', (TP+TN)/(TP+TN+FP+FN))
print('PPV(precision) :\t', TP/(FP+TP))
print('F1 :\t', F1)
print('Recall :\t', TP/(TP+FN))
print('Max accuracy  :\t', max_accuracy, '\n')

for k, v in cv_res.items():
    cv_res[k] = v * 1. / cv_res["total"]
