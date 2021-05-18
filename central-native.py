# Count 
import statistics 
values=[47,95,88,73,88,84]
count=len(values)
print (count)

# Sum
sum=sum(values)
print (sum)

# Mean
mean=sum/count
print (mean)

# Median 
n = len(values)
values.sort()
  
if n % 2 == 0:
    median1 = values[n//2]
    median2 = values[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = values[n//2]
print("Median is: " + str(median))

# Mode
def mode(values):
    frequency={}
    for number in values:
        frequency.setdefault(number, 0) 
        frequency [number]+=1
    highestFrequency=max(frequency.values())
    highestFreqLst=[] 
    for number, freq in frequency.items():
        if freq == highestFrequency: 
            highestFreqLst.append(number)
    return highestFreqLst
print (mode(values))
