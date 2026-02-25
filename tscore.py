import numpy as np

data=np.array([30,40,55,65,80])
mu=500
mean=np.mean(data)
s=np.std(data, ddof=1)
n=len(data)
uc=s/np.sqrt(n)

t_score=(mean-mu)/uc
print("T-score:", t_score)

if abs(t_score)>2.776:
    print("Reject the null hypothesis")
else:
    print("accept the null hypothesis")