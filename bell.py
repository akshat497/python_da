import numpy as np
import matplotlib.pyplot as plt

# Population: marks of 1000 students
population = np.random.randint(0, 100, 100000)
print(population)
sample_means = []

for i in range(5000):
    sample = np.random.choice(population, size=30)
    mean=np.mean(sample)
    
    sample_means.append(mean)

plt.hist(sample_means, bins=25)
print("mean of sample means:", np.mean(sample_means))
plt.title("Distribution of Sample Means")
plt.show()


#erf and cdf 
# error function and cumulative distribution function
import numpy as np
import math


# z=2
# ef=(z/np.sqrt(2))
# erf=math.erf(ef)
# cdf=0.5*(1+erf)
# p_value=2*(1-cdf)
# print(p_value)
# if p_value<=0.05:
#     print("Reject the null hypothesis")
# else:   
#     print("Fail to reject the null hypothesis")


# array=np.array([30,40,55,65,800])

# mean=np.mean(array)

# var=np.var(array)
# std=np.sqrt(var)
# for x in array:
#     z_score=(x-mean)/std
#     if (abs(z_score)>1.96):
#         print(f"{x} claim is rejected")
#     else:
#         print(f"{x} claim is accepted")
    
#     print(f"Z-score for {x}: {z_score}")
# print(var)
# print(std)

