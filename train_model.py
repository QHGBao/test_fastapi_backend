from sklearn.linear_model import LinearRegression
import joblib

# dữ liệu giả (area, rooms)
X = [
    [50, 2],
    [70, 3],
    [100, 4],
    [120, 5]
]

# giá nhà (giả lập)
y = [60000, 90000, 150000, 200000]

# train model
model = LinearRegression()
model.fit(X, y)

# lưu model
joblib.dump(model, "model.pkl")

print("✅ Model saved as model.pkl")