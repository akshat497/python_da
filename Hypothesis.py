import numpy as np

total=100
heads=54
p=0.5
expected=total*p


print(expected)


std=np.sqrt(expected*(1-p))
z=(heads-expected)/std

if z>1.96:
    print("biased flips")
else:
    print("fair decision")
    
    
    