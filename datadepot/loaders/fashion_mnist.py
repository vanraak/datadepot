def load_fashion_mnist():
    try:
        from keras.datasets import fashion_mnist
    except ImportError as exc:
        raise ImportError("Loading Fashion-MNIST requires Keras.") from exc

    return fashion_mnist.load_data()
