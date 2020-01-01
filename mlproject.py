from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

#데이터셋을 읽는다
iris = datasets.load_iris()

print("iris.keys() : {}\n".format(iris.keys()))
print("iris 데이터의 형태 : {}\n".format(iris.data.shape))
print("클래스별 샘플 개수 : {}\n".format({n: v for n, v in zip(iris.target_names, np.bincount(iris.target))}))
print("특성 이름 : {}\n".format(iris.feature_names))

#훈련 세트와 테스트 세트로 나눈다
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,stratify=iris.target, random_state=42)

#과적합을 막기 위해 결정트리의 깊이를 4로 제한한다.
tree = DecisionTreeClassifier(max_depth=4,random_state=0)
tree.fit(X_train, y_train)
print("Decision Tree Model 훈련세트 정확도: {:.3f}\n".format(tree.score(X_train, y_train)))
print("Decision Tree Model 테스트 세트 정확도: {:.3f}\n".format(tree.score(X_test, y_test)))
dtm_test_accuracy = tree.score(X_test, y_test)

#특성중요도 확인
def plot_feature_importances_iris(model):
    n_features = iris.data.shape[1]
    plt.barh(range(n_features),model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features),iris.feature_names)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")

plot_feature_importances_iris(tree)

NewDataSet = X_test
predicted_class = tree.predict(NewDataSet)
#0은 setosa, 1은 versicolor, 2는 virginica
print("\t<0 : setosa, 1 : versicolor, 2 : virginica>\n", predicted_class,"\n")

#knn
import mglearn
from sklearn.neighbors import KNeighborsClassifier

#데이터 셋을 만든다
X, y = mglearn.datasets.make_forge()
#데이터를 훈련 세트와 테스트 세트로 나눈다
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#이웃의 수를 3개로 지정
clf = KNeighborsClassifier(n_neighbors=3)
#분류 모델을 학습시킴
clf.fit(X_train, y_train)

print("KNN 테스트 세트 예측: {}\n".format(clf.predict(X_test)))
print("KNN 테스트 세트 정확도: {:.2f}\n".format(clf.score(X_test, y_test)))
knn_test_accuracy = clf.score(X_test, y_test)

if(dtm_test_accuracy>knn_test_accuracy):
    print("Decision Tree Model 테스트 세트 정확도({:.2f})가 KNN 테스트 세트 정확도({:.2f})보다 더 높다\n".format(dtm_test_accuracy, knn_test_accuracy))
elif(dtm_test_accuracy<knn_test_accuracy):
    print("KNN 테스트 세트 정확도({:.2f})가 Decision Tree Model 테스트 세트 정확도({:.2f})보다 더 높다\n".format(knn_test_accuracy, dtm_test_accuracy))
else:
    print("Decision Tree Model 테스트 세트 정확도({:.2f})와 KNN 테스트 세트 정확도({:.2f})가 동일하다.\n".format(dtm_test_accuracy, knn_test_accuracy))