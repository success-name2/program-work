#创建模型，训练模型，利用模型进行预测。
from idlelib.browser import transform_children
from scipy.linalg.interpolative import estimate_rank
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.model_selection import StratifiedShuffleSplit
from  sklearn.model_selection import ShuffleSplit
from collections import Counter
from  sklearn.model_selection import KFold
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sympy.physics.vector.printing import params

#加载数据
x,y=datasets.load_iris(return_X_y=True)
#训练集测试集划分
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

estimator=KNeighborsClassifier()
param_grid={'n_neighbors':[1,3,5,7]}
estimator=GridSearchCV(estimator,param_grid=param_grid,cv=5,verbose=0)
estimator.fit(x_train,y_train)

# y_predict=knn_estimator.predict(x_test)
# print('预测结果准确率为:',sum(y_predict==y_test)/y_test.shape[0])
print('最优参数组合:',estimator.best_params_,'最好得分:',estimator.best_score_)
#测试集评估模型
# accuracy_score(y_predict,y_test)
print('测试集准确率:',estimator.score(x_test,y_test))
