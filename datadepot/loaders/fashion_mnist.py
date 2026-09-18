def load_fashion_mnist():
    try:
        from tensorflow.keras.datasets import fashion_mnist
    except ImportError as exc:
        raise ImportError("Loading Fashion-MNIST requires TensorFlow.") from exc

    return fashion_mnist.load_data()
