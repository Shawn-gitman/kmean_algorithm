import numpy as np

def mm_normalize(data):
  # min-max
  (rows, cols) = data.shape  # (20,4) for demo
  mins = np.zeros(shape=(cols), dtype=np.float32)
  maxs = np.zeros(shape=(cols), dtype=np.float32)
  for j in range(cols):
    mins[j] = np.min(data[:,j])
    maxs[j] = np.max(data[:,j])

  result = np.copy(data)
  for i in range(rows):
    for j in range(cols):
      result[i,j] = (data[i,j] - mins[j]) / (maxs[j] - mins[j])
  return (result, mins, maxs)

def distance(item, mean):
  # Euclidean distance from a data item to a mean
  sum = 0.0
  dim = len(item)
  for j in range(dim):
    sum += (item[j] - mean[j]) ** 2
  return np.sqrt(sum)

def update_clustering(norm_data, clustering, means):
  # given a (new) set of means, assign new clustering
  # return False if no change or bad clustering
  n = len(norm_data)
  k = len(means)

  new_clustering = np.copy(clustering)  # proposed new clustering
  distances = np.zeros(shape=(k), dtype=np.float32)  # from item to each mean

  for i in range(n):  # walk thru each data item
    for kk in range(k):
      distances[kk] = distance(norm_data[i], means[kk])
    new_id = np.argmin(distances)
    new_clustering[i] = new_id
  
  if np.array_equal(clustering, new_clustering):  # no change so done
    return False

  # make sure that no cluster counts have gone to zero
  counts = np.zeros(shape=(k), dtype=np.int)
  for i in range(n):
    c_id = clustering[i]
    counts[c_id] += 1
  
  for kk in range(k):  # could use np.count_nonzero
    if counts[kk] == 0:  # bad clustering
      return False

  # there was a change, and no counts have gone 0
  for i in range(n):
   clustering[i] = new_clustering[i]  # update by ref
  return True

def update_means(norm_data, clustering, means):
  # given a (new) clustering, compute new means
  # assumes update_clustering has just been called
  # to guarantee no 0-count clusters
  (n, dim) = norm_data.shape
  k = len(means)
  counts = np.zeros(shape=(k), dtype=np.int)
  new_means = np.zeros(shape=means.shape, dtype=np.float32)  # k x dim

  for i in range(n):  # walk thru each data item
    c_id = clustering[i]
    counts[c_id] += 1
    for j in range(dim):
      new_means[c_id,j] += norm_data[i,j]  # accumulate sum

  for kk in range(k):  # each mean
    for j in range(dim):
      new_means[kk,j] /= counts[kk]  # assumes not zero

  for kk in range(k):  # each mean
    for j in range(dim):
      means[kk,j] = new_means[kk,j]  # update by ref

  

def initialize(norm_data, k):
  (n, dim) = norm_data.shape
  clustering = np.zeros(shape=(n), dtype=np.int)  # index = item, val = cluster ID
  for i in range(k):
    clustering[i] = i
  for i in range(k, n):
    clustering[i] = np.random.randint(0, k) 

  means = np.zeros(shape=(k,dim), dtype=np.float32)
  update_means(norm_data, clustering, means)
  #print(means)
  return(clustering, means) 
  
def cluster(norm_data, k, iter_num):

  (clustering, means) = initialize(norm_data, k)
  

  ok = True  # if a change was made and no bad clustering
  sanity_ct = 1
  iter_count = int(0)
  while sanity_ct <= iter_num:
    ok = update_clustering(norm_data, clustering, means)  # use new means
    if ok == False:
      break  # done

    update_means(norm_data,clustering, means)  # use new clustering
    print("centroids",int(iter_count+1),':',means*1000)
    iter_count += 1
    sanity_ct += 1

  return clustering, means

def display(raw_data, clustering, k):
  (n, dim) = raw_data.shape
  count = int(0)
  #print("-------------------")
  for kk in range(k):  # group by cluster ID
    for i in range(n):  # scan the raw data
      c_id = clustering[i]  # cluster ID of curr item
      if c_id == kk:  # curr item belongs to curr cluster so . . 
        #print("%4d " % i, end=""); print(raw_data[i])
        count+=1
      
    print("# of vectors in cluster", kk+1, ':', count)

    #print("-------------------")
    count = int(0)  


def main():
  #print("\nBegin k-means clustering demo \n")
  np.set_printoptions(precision=4, suppress=True)
  np.random.seed(2)

  cluster_num = input("Type the number of clusters:")
  iteration_num = input("Type the number of iteration:")
  print("-------------------")
  print("# of actual iterations:",iteration_num)
  raw_data = np.loadtxt("resource2.txt", dtype=np.float32,
    delimiter=" ", skiprows=0, usecols=[0,1,2,3,4])
  (n, dim) = raw_data.shape

  #print("Raw data:")
  for i in range(n):
    #print("%4d " % i, end=""); print(raw_data[i])  
    pass

  (norm_data, mins, maxs) = mm_normalize(raw_data)
  

  k = int(cluster_num)
  #print("\nClustering normalized data with k=" + str(k))
  (clustering, means) = cluster(norm_data, k, int(iteration_num))

  #print("\nDone. Clustering:")
  #print(clustering)
  
  

  #print("\nRaw data grouped by cluster: ")
  display(raw_data, clustering, k)

  #print("\nEnd k-means demo ")


if __name__ == "__main__":
  main()
