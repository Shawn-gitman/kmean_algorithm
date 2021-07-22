# <Kmean_algorithm , 강태규 201614729>, This description is written in Korean. Please check English translated interpretation below.

Kmean_algorithm 실행 방법은 다음과 같습니다. 

1. ctrl+마우스 오른쪽 클릭 후, windows powershell를 실행시킵니다.
2. 다음 명령어를 입력합니다 "python kmean_algorithm.py"

제가 만든 kmean 알고리즘은 다음과 같은 순서를 따르고 있습니다.

1. 텍스트파일로 5차원 벡터 데이터셋을 받는다
2. iteration 횟수와 cluster갯수를 int값으로 받는다.
3. cluster 갯수와 상응하는 렌덤한 centroid 5차원 벡터들을 생성한다.
4. centroid과 다른 벡터들과 거리를 구하고 최소의 값을 가진 함수를 해당 cluster에 편입한다.
5. iteration 횟수가 2이상이라면 centroid값을 다시 변경시키고 4번의 과정을 반복한다.
6. 해당 cluster들에 할당된 벡터들의 갯수를 int값으로 받아본다. 

다음은 Kmean 알고리즘을 구현하는데 정의한 함수들입니다.

1. mm_normalize : 기존의 5차원 데이터셋을 받아서 0-1사이의 minimun과 maximum 값을 종합해 해당 cluster에 할당할 수 있도록 데이터셋을 조정합니다.
2. distance : 각 벡터들 사이의 절대적인 거리 값을 구합니다.
3. update_clustering : clustering 데이터들을 업데이트합니다. 
4. update_means : means를 업데이트 합니다. 
5. initialize : Means와 clustering 데이터들을 초기화합니다. 
6. cluster : iteration 횟수를 받아서 기존에 할당된 cluster들을 업데이트합니다.
7. display : 각 cluster들에 할당된 벡터들의 갯수를 나타냅니다.
8. main : 모든 코드를 운용합니다. 


# <Kmean_algorithm by Taekyu Kang>

Here is the way to execute a program.

1. Click Ctrl+right button of mouse and execute windows powershell
2. Type following command "python Kmean_algorithm.py"

The source code that I make for kmean algorithm follows procedures below.

1. Read 5-vector dataset by .txt file.
2. Input the number of iterations and clusters by int.
3. Create a consistent number of 5-vector centroids as an iteration number.
4. Analyze distanace between centroid and vectors and assign vectors to clusters that has minimum cost.
5. Modify the cost of centroid if the iteration is repetitive over twice.
6. Get a result of clusters by int that has following vectors. 

Next, there are various functions that work for Kmean algorithm.

1. mm_normalize : Transfer original 5-vecotr dataset to another that includes maximum and minimum values around 0-1.
2. distance : Return distance between individual vectors.
3. update_clustering : Update clustering data.
4. update_means : Update means.
5. initialize : Initialize Means and clustering data.
6. cluster : Update original clusters to new as follow the number of iterations.
7. display : Return the number of clusters and assigned vectors.
8. main : Operate entire source.
