
InputArray=[]


NoOfElements=input('Please input No. of Elements:')
for i in range(int(NoOfElements)):
    ArrayElement=input('Please input an element:')
    InputArray.append(ArrayElement)

print(InputArray)

def countDuplicates(inputArray):
 HaveComparedFrontList=[]
 duplicate_count=0
 counter=1
 array_length=len(inputArray)
 for i in range(array_length):
  #duplicate_count=duplicate_count-1
  HaveComparedFrontList.append(inputArray[i])
  for j in range((i+1),array_length,1):
    ##if j>(i+1):
    # for k in range(i-1):
    #  if j>i:
    #      if inputArray[k]==inputArray[i]:
    #       duplicate_count=duplicate_count+1
    # for l in range((i+1),j,1):
    #  #if (i+1)<j:
    #  if inputArray[l]==inputArray[i]:
    #   duplicate_count=duplicate_count+1
    #while i!=j:
     
     if inputArray[i] not in HaveComparedFrontList:
       if inputArray[j]==inputArray[i]:
           duplicate_count=duplicate_count+1
 #duplicate_count=duplicate_count-array_length+1
 return duplicate_count

print(countDuplicates(InputArray))

             
#hello, this is a test file for git local repository 

#Test changes

 
