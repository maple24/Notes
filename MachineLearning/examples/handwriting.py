import sys
import tensorflow as tf


# use mnist handwriting dataset
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
y_train = tf.keras.utils.to_categorical(y_train)
y_test = tf.keras.utils.to_categorical(y_test)


# 1 in last part is to specify color depth of the pixel
x_train = x_train.reshape(
    x_train.shape[0], x_train.shape[1], x_train.shape[2], 1
)
x_test = x_test.reshape(
    x_test.shape[0], x_test.shape[1], x_test.shape[2], 1
)

model = tf.keras.models.Sequential([
    
    # Convolutional layer, learn 32 filters using a 3x3 kernel
    tf.keras.layers.Conv2D(
        32, (3, 3), activation="relu", input_shape=(28, 28, 1), 
    ),
    
    # Max-pooling layer, using 2x2 pool size
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    
    # Flatten units
    tf.keras.layers.Flatten(),
    
    # Add a hidden layer with dropout to avoid overfitting
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dropout(0.5),
    
    tf.keras.layers.Dense(10, activation="softmax")
])

model.compile(
    optimizer="adam", # one of gradient descent methods
    loss="categorical_crossentropy", # one of loss computing method for probability output, eg. mean square loss, empirical loss
    metrics=["accuracy"] # define metrics to monitor the training and testing steps, here we look at accuracy
)
model.fit(x_train, y_train, batch_size=10, epochs=10)
model.evaluate(x_test, y_test, verbose=2)

# save model to file
if len(sys.argv) == 2:
    filename = sys.argv[1]
    model.save(filename)
    print(f"Model saved to {filename}.")