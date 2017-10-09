"""

"""

################# Figures 06_01 - 06_03 #################
"""

"""
import numpy as np
import matplotlib
#matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt

# Create the data
x = []
y = []
for centroid in [(2, 2), (8, 2), (2, 8), (8, 8)]:
    print centroid
    for i in range(10):
        x.append(np.random.normal(centroid[0]))
        y.append(np.random.normal(centroid[1]))

# Plot the data
plt.scatter(x, y, color='k', marker='o', s=200)
plt.grid()
plt.show()


# Plot two clusters
plt.figure()
x_clusters = zip(*(iter(x),) * 10)
y_clusters = zip(*(iter(y),) * 10)
plt.scatter(x_clusters[0], y_clusters[0], color='k', marker='o', s=200)
plt.scatter(x_clusters[1], y_clusters[1], color='r', marker='s', s=200)
plt.scatter(x_clusters[2], y_clusters[2], color='k', marker='o', s=200)
plt.scatter(x_clusters[3], y_clusters[3], color='r', marker='s', s=200)
plt.grid()
plt.show()


# Plot four clusters
plt.figure()
x_clusters = zip(*(iter(x),) * 10)
y_clusters = zip(*(iter(y),) * 10)
plt.scatter(x_clusters[0], y_clusters[0], color='k', marker='o', s=200)
plt.scatter(x_clusters[1], y_clusters[1], color='r', marker='s', s=200)
plt.scatter(x_clusters[2], y_clusters[2], color='g', marker='D', s=200)
plt.scatter(x_clusters[3], y_clusters[3], color='b', marker='^', s=200)
plt.grid()
plt.show()


################# Figure 06_05 #################
"""

"""
import matplotlib
#matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt

X = [
    [7, 5],
    [5, 7],
    [7, 7],
    [3, 3],
    [4, 6],
    [1, 4],
    [0, 0],
    [2, 2],
    [8, 7],
    [6, 8],
    [5, 5],
    [3, 7]
]

x, y = zip(*X)
plt.scatter(x, y, color='k')
plt.grid()
plt.show()

################# Figure 06_06 #################
"""
The result of the first iteration of K-Means
"""
import matplotlib
#matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
c1x = [5, 4, 1, 6, 3]
c1y = [7, 6, 4, 8, 7]
c2x = [7, 7, 3, 0, 2, 8, 5]
c2y = [5, 7, 3 ,0 ,2 ,7 ,5]
plt.scatter(c1x, c1y, color='r')
plt.scatter([4], [6], color='r', marker='x', s=256)
plt.scatter(c2x, c2y, color='g')
plt.scatter([5], [5], color='g', marker='x', s=256)
plt.grid()
plt.show()


################# Figure 06_07 #################
"""
The result of the second iteration of K-Means
"""
import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
c1x = [5, 7, 4, 8, 6, 3]
c1y = [7, 7, 6, 7, 8, 7]
c2x = [7, 3, 1, 0, 2, 5]
c2y = [5, 3, 4, 0, 2, 5]
plt.scatter(c1x, c1y, color='r')
plt.scatter([3.8], [6.4], color='r', marker='x', s=256)
plt.scatter(c2x, c2y, color='g')
plt.scatter([4.5714285714], [4.1428571429], color='g', marker='x', s=256)
plt.grid()
plt.show()


################# Figure 06_08 #################
"""

"""
import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
c1x = [7, 5, 7, 4, 8, 6, 5, 3]
c1y = [5, 7, 7, 6, 7, 8, 5, 7]
c2x = [3, 1, 0, 2]
c2y = [3, 4, 0, 2]
plt.scatter(c1x, c1y, color='r')
plt.scatter([5.625], [6.5], color='r', marker='x', s=256)
plt.scatter(c2x, c2y, color='g')
plt.scatter([1.5], [2.25], color='g', marker='x', s=256)
plt.grid()
plt.show()


################# Figure 06_09 - 06_10 #################
"""
Plot an unlucky initialization of K-Means
"""
import matplotlib.pyplot as plt

x = [5.749038874212223, 5.655149965177027, 4.438552312330491, 5.451867409428628, 4.861174993666921, 4.574139543873348, 4.7103149112188785, 6.361987372686885, 5.350496964296188, 7.334787828251171, 3.724960975524051, 4.516898332153453, 4.590820167742156, 4.888713715268829, 5.58706618580751, 5.499898334425577, 4.9304851639679645, 5.173367936859512]
y = [1.5600425447366681, 1.8521167472861984, -0.34664839470444786, 0.29180814519742326, -0.5062758938445506, 1.8157831493328997, 1.2612212011027966, 0.8821213955656363, 9.856207716729374, 7.252967807168886, 9.204583302534418, 7.735672187049999, 6.460797098218169, 7.4694452583870445, 7.005875123804591, 7.129196847187513, 8.477115009687902, 8.109716657032214]
c1x = [4.270832165561871]
c1y = [0.24783914312892807]
c2x = [4.741711876896134]
c2y = [0.3086121140743425]

plt.scatter(x, y, color='k', marker='o', s=200)
plt.scatter(c1x, c1y, color='r', marker='D', s=200)
plt.scatter(c2x, c2y, color='g', marker='^', s=200)
plt.xlim((0, 10))
plt.grid()
plt.show()

c2x = [4.270832165561871, 4.741711876896134, 5.749038874212223, 5.655149965177027, 5.451867409428628, 4.574139543873348, 4.7103149112188785, 6.361987372686885, 5.350496964296188, 7.334787828251171, 3.724960975524051, 4.516898332153453, 4.590820167742156, 4.888713715268829, 5.58706618580751, 5.499898334425577, 4.9304851639679645, 5.173367936859512]
c2y = [0.24783914312892807, 0.3086121140743425, 1.5600425447366681, 1.8521167472861984, 0.29180814519742326, 1.8157831493328997, 1.2612212011027966, 0.8821213955656363, 9.856207716729374, 7.252967807168886, 9.204583302534418, 7.735672187049999, 6.460797098218169, 7.4694452583870445, 7.005875123804591, 7.129196847187513, 8.477115009687902, 8.109716657032214]
c1x = [4.438552312330491, 4.861174993666921]
c1y = [-0.34664839470444786, -0.5062758938445506]

plt.scatter(c1x, c1y, color='r', marker='D', s=200)
plt.scatter(c2x, c2y, color='g', marker='o', s=200)
plt.xlim((0, 10))
plt.grid()
plt.show()



################# Sample 1 #################
"""
>>> import numpy as np
>>> from sklearn.cluster import KMeans
>>> from sklearn import metrics
>>> import matplotlib.pyplot as plt

>>> x1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
>>> x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
>>> X = zip(x1, x2)

>>> plt.xlim([0, 10])
>>> plt.ylim([0, 10])
>>> plt.scatter(x1, x2)
>>> plt.show()

>>> colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b']
>>> markers = ['o', 's', 'D', 'v', '^', 'p', '*', '+']
>>> tests = [2, 3, 4, 8]
>>> for t in tests:
>>>     kmeans_model = KMeans(n_clusters=t).fit(X)
>>>     for i, l in enumerate(kmeans_model.labels_):
>>>         plt.plot(x1[i], x2[i], color=colors[l], marker=markers[l], ls='None')
>>>     plt.xlim([0, 10])
>>>     plt.ylim([0, 10])
>>>     plt.title('K = %s, Silhouette Coefficient = %.03f' % (
>>>         t, metrics.silhouette_score(X, kmeans_model.labels_, metric='euclidean')))
>>>     plt.show()
"""
import matplotlib
matplotlib.use('Qt4Agg')
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt

x1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
X = zip(x1, x2)

plt.xlim([0, 10])
plt.ylim([0, 10])
plt.scatter(x1, x2)
plt.show()

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b']
markers = ['o', 's', 'D', 'v', '^', 'p', '*', '+']
tests = [2, 3, 4, 8]
for t in tests:
    kmeans_model = KMeans(n_clusters=t).fit(X)
    for i, l in enumerate(kmeans_model.labels_):
        plt.plot(x1[i], x2[i], color=colors[l], marker=markers[l], ls='None')
    plt.xlim([0, 10])
    plt.ylim([0, 10])
    plt.title('K = %s, Silhouette Coefficient = %.03f' % (
        t, metrics.silhouette_score(X, kmeans_model.labels_, metric='euclidean')))
    plt.show()


################# Sample 2 #################
"""
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> from sklearn.cluster import KMeans
>>> from sklearn.utils import shuffle
>>> import mahotas as mh

>>> original_img = np.array(mh.imread('img/tree.jpg'), dtype=np.float64) / 255
>>> original_dimensions = tuple(original_img.shape)
>>> width, height, depth = tuple(original_img.shape)

>>> image_flattened = np.reshape(original_img, (width * height, depth))
>>> image_array_sample = shuffle(image_flattened, random_state=0)[:1000]
>>> estimator = KMeans(n_clusters=64, random_state=0)
>>> estimator.fit(image_array_sample)
>>> cluster_assignments = estimator.predict(image_flattened)

>>> compressed_palette = estimator.cluster_centers_
>>> compressed_img = np.zeros((width, height, compressed_palette.shape[1]))
>>> label_idx = 0
>>> for i in range(width):
>>>     for j in range(height):
>>>         compressed_img[i][j] = compressed_palette[cluster_assignments[label_idx]]
>>>         label_idx += 1

>>> plt.subplot(122)
>>> plt.title('Original Image')
>>> plt.imshow(original_img)
>>> plt.axis('off')
>>> plt.subplot(121)
>>> plt.title('Compressed Image')
>>> plt.imshow(compressed_img)
>>> plt.axis('off')
>>> plt.show()

"""
import matplotlib
matplotlib.use('Qt4Agg')
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
import mahotas as mh

original_img = np.array(mh.imread('img/tree.jpg'), dtype=np.float64) / 255
original_dimensions = tuple(original_img.shape)
width, height, depth = tuple(original_img.shape)

image_flattened = np.reshape(original_img, (width * height, depth))
image_array_sample = shuffle(image_flattened, random_state=0)[:1000]
estimator = KMeans(n_clusters=64, random_state=0)
estimator.fit(image_array_sample)
cluster_assignments = estimator.predict(image_flattened)

compressed_palette = estimator.cluster_centers_
compressed_img = np.zeros((width, height, compressed_palette.shape[1]))
label_idx = 0
for i in range(width):
    for j in range(height):
        compressed_img[i][j] = compressed_palette[cluster_assignments[label_idx]]
        label_idx += 1

plt.subplot(122)
plt.title('Original Image')
plt.imshow(original_img)
plt.axis('off')
plt.subplot(121)
plt.title('Compressed Image')
plt.imshow(compressed_img)
plt.axis('off')
plt.show()


################# Sample 3 #################
# TODO try this with the points of interest from ch3
"""
>>> import numpy as np
>>> import mahotas as mh
>>> from mahotas.features import surf
>>> from sklearn.linear_model import LogisticRegression
>>> from sklearn.metrics import *
>>> from sklearn.cluster import MiniBatchKMeans
>>> import glob

>>> all_instance_filenames = []
>>> all_instance_targets = []
>>> for f in glob.glob('cats-and-dogs-img/*.jpg'):
>>>     target = 1 if 'cat' in f else 0
>>>     all_instance_filenames.append(f)
>>>     all_instance_targets.append(target)

>>> surf_features = []
>>> counter = 0
>>> for f in all_instance_filenames:
>>>     print 'Reading image:', f
>>>     image = mh.imread(f, as_grey=True)
>>>     surf_features.append(surf.surf(image)[:, 5:])

>>> train_len = int(len(all_instance_filenames) * .60)
>>> X_train_surf_features = np.concatenate(surf_features[:train_len])
>>> X_test_surf_feautres = np.concatenate(surf_features[train_len:])
>>> y_train = all_instance_targets[:train_len]
>>> y_test = all_instance_targets[train_len:]

>>> n_clusters = 300
>>> print 'Clustering', len(X_train_surf_features), 'features'
>>> estimator = MiniBatchKMeans(n_clusters=n_clusters)
>>> estimator.fit_transform(X_train_surf_features)

>>> X_train = []
>>> for instance in surf_features[:train_len]:
>>>     clusters = estimator.predict(instance)
>>>     features = np.bincount(clusters)
>>>     if len(features) < n_clusters:
>>>         features = np.append(features, np.zeros((1, n_clusters-len(features))))
>>>     X_train.append(features)

>>> X_test = []
>>> for instance in surf_features[train_len:]:
>>>     clusters = estimator.predict(instance)
>>>     features = np.bincount(clusters)
>>>     if len(features) < n_clusters:
>>>         features = np.append(features, np.zeros((1, n_clusters-len(features))))
>>>     X_test.append(features)

>>> clf = LogisticRegression(C=0.001, penalty='l2')
>>> clf.fit_transform(X_train, y_train)
>>> predictions = clf.predict(X_test)
>>> print classification_report(y_test, predictions)
>>> print 'Precision:', precision_score(y_test, predictions)
>>> print 'Recall:', recall_score(y_test, predictions)
>>> print 'Accuracy:', accuracy_score(y_test, predictions)
Reading image: dog.9344.jpg
...
Reading image: dog.8892.jpg
Clustering 756914 features
             precision    recall  f1-score   support

          0       0.71      0.76      0.73       392
          1       0.75      0.70      0.72       408

avg / total       0.73      0.73      0.73       800

Precision:  0.751322751323
Recall:  0.696078431373
Accuracy:  0.7275
"""
import numpy as np
import mahotas as mh
from mahotas.features import surf
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import *
from sklearn.cluster import MiniBatchKMeans
import glob

all_instance_filenames = []
all_instance_targets = []
for f in glob.glob('cats-and-dogs-img/*.jpg'):
    target = 1 if 'cat' in f else 0
    all_instance_filenames.append(f)
    all_instance_targets.append(target)

surf_features = []
counter = 0
for f in all_instance_filenames:
    print 'Reading image:', f
    image = mh.imread(f, as_grey=True)
    surf_features.append(surf.surf(image)[:, 5:])

train_len = int(len(all_instance_filenames) * .60)
X_train_surf_features = np.concatenate(surf_features[:train_len])
X_test_surf_feautres = np.concatenate(surf_features[train_len:])
y_train = all_instance_targets[:train_len]
y_test = all_instance_targets[train_len:]

n_clusters = 300
print 'Clustering', len(X_train_surf_features), 'features'
estimator = MiniBatchKMeans(n_clusters=n_clusters)
estimator.fit_transform(X_train_surf_features)

X_train = []
for instance in surf_features[:train_len]:
    clusters = estimator.predict(instance)
    features = np.bincount(clusters)
    if len(features) < n_clusters:
        features = np.append(features, np.zeros((1, n_clusters-len(features))))
    X_train.append(features)

X_test = []
for instance in surf_features[train_len:]:
    clusters = estimator.predict(instance)
    features = np.bincount(clusters)
    if len(features) < n_clusters:
        features = np.append(features, np.zeros((1, n_clusters-len(features))))
    X_test.append(features)

clf = LogisticRegression(C=0.001, penalty='l2')
clf.fit_transform(X_train, y_train)
predictions = clf.predict(X_test)
print classification_report(y_test, predictions)
print 'Precision:', precision_score(y_test, predictions)
print 'Recall:', recall_score(y_test, predictions)
print 'Accuracy:', accuracy_score(y_test, predictions)