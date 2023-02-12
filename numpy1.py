import numpy as np
from scipy import stats as sts
arr=np.array([[1,3,5,7,9],[0,2,4,6,8],[4,6,7,8,9]])
print(arr)
print(type(arr))
print(arr.shape)
print(arr.size)
print(arr[1][3])
arr[2][2]=8
print(arr)
print(arr[1,4])
print(arr[1,-1])
print(arr[2][-3])
arr1=np.array(["Aryan","Giris","Sampath"])
print(arr1)
arr2=np.arange(0,50,3)
print(arr2)
arr3=np.linspace(0,50,100)
print(arr3)
arr4=np.random.rand(1,10)
print(arr4)
arr5=np.random.rand(3,4)
print(arr5)
print(np.zeros(20))
print(np.zeros((5,5)))
print(np.trace(arr))
print(np.ones((7,7)))
arr6=np.array([1,3,5,7])
print(np.repeat(arr6,4))
print(np.tile(arr6,3))
arr7=np.array([[1,2,3],[4,5,5],[7,8,9]])
print(arr7)
print(np.trace(arr7))
arr8=np.eye(7)
print(arr8)
print(np.diag([1,3,5,7]))
arr9=np.random.rand(4,4)
print(arr9)
print(np.diag(arr9))
print(arr.ndim)
arr10=np.random.randint(-20,25,8)
print(arr10)
print(arr9+10)
print(arr9*10)
print(np.exp(arr9))
print(np.log(arr9))
print(np.log2(arr9))
print(np.sin(arr9))
print(np.tan(arr9))
print(np.sum(arr7))
print(np.prod(arr7))
print(np.sum(arr7,axis=0))
print(np.sum(arr7,axis=1))
print(np.prod(arr7,axis=0))
print(np.prod(arr7,axis=1))
print(np.max(arr7))
print(np.max(arr7,axis=0))
print(np.max(arr7,axis=1))
print(np.min(arr7))
print(np.min(arr7,axis=0))
print(np.min(arr7,axis=1))
print(np.mean(arr7))
print(np.median(arr7))
print(sts.mode(arr7))
print(np.std(arr7))
print(np.var(arr7))
arr8=np.array([1,2,1,3,4])
print(sts.mode(arr8))
print(arr9[0:,1:3])
print(arr9[0:,1:2])
print(np.sort(arr9))
print(np.sort(arr9,axis=0))
print(np.sort(arr9,axis=1))
print(arr9)
print(arr9.T)
print(arr9[2:4,:].T)
print(arr9.flatten())
print(arr9[2:4,:].flatten())
arr11=np.array([1,3,5,7])
print(arr11)
arr12=np.append(arr11,9)
print(arr12)
arr13=np.insert(arr12,1,[2,4,6])
print(arr13)
arr14=np.delete(arr13,1)
print(arr14)
arr15=np.delete(arr14,[1,2])
print(arr15)
arr16=arr15.copy()
print(arr16)
arr17=np.array([[1,2,3,4],[1,2,3,4]])
arr18=np.array([[5,6,7,8],[5,6,7,8]])
print(np.concatenate((arr17,arr18),axis=0))
print(np.concatenate((arr17,arr18),axis=1))
cat1=np.hstack((arr17,arr18))
print(cat1)
cat2=np.vstack((arr17,arr18))
print(cat2)
print(np.unique(cat2))
uniques,counts=np.unique(cat2,return_counts=True)
print(uniques)
print(counts)
arr19=np.array([1,2,3,4,5])
arr20=np.array([3,4,5,6,7])
print(np.union1d(arr19,arr20))
print(np.intersect1d(arr19,arr20))
print(np.setdiff1d(arr19,arr20))
print(np.setxor1d(arr19,arr20))