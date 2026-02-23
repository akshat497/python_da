# import numpy as np
# import matplotlib.pyplot as plt

# # Population: marks of 1000 students
# population = np.random.randint(0, 100, 1000)

# sample_means = []

# for i in range(100):
#     sample = np.random.choice(population, size=10)
#     sample_means.append(np.mean(sample))

# plt.hist(sample_means, bins=15)
# plt.title("Distribution of Sample Means")
# plt.show()


#erf and cdf 
# error function and cumulative distribution function
import numpy as np
import math


z=2
ef=(z/np.sqrt(2))
erf=math.erf(ef)
cdf=0.5*(1+erf)
p_value=2*(1-cdf)
print(p_value)
if p_value<=0.05:
    print("Reject the null hypothesis")
else:   
    print("Fail to reject the null hypothesis")



