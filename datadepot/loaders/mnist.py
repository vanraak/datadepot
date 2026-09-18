def load_mnist():
    try:
        from tensorflow.keras.datasets import mnist
    except ImportError as exc:
        raise ImportError("Loading MNIST requires TensorFlow.") from exc

    return mnist.load_data()
