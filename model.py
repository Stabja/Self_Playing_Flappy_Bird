dataset = pd.read_csv('flappyData.csv')
X = dataset.iloc[:, 0:2].values
Y = dataset.iloc[:, 2].values

sc = StandardScaler()
X = sc.fit_transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=7)

classifier = Sequential()
classifier.add(Dense(6, init='uniform', activation='relu', input_dim = 2))
classifier.add(Dense(6, init='uniform', activation='relu'))
classifier.add(Dense(1, init='uniform', activation='sigmoid'))
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
classifier.summary()

classifier.fit(X, Y, batch_size = 1, epochs = 10)

Y_pred = classifier.predict(X_test)
Y_pred = (Y_pred > 0.1)
