from mlxtend.data import iris_data
from mlxtend.preprocessing import standardize
from mlxtend.feature_extraction import LinearDiscriminantAnalysis

X,y = iris_data()
X= standardize(X)

lda = LinearDiscriminantAnalysis(n_discriminants=2)
lda.fit(X,y)
X_lda =lda.transform(X)
print(X_lda)