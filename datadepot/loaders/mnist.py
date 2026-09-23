def load_mnist():
    try:
        from keras.datasets import mnist
    except ImportError as exc:
        raise ImportError("Loading MNIST requires Keras.") from exc

    return mnist.load_data()
