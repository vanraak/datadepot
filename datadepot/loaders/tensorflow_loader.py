def load(meta: dict, canonical_name: str):
    if canonical_name == "mnist":
        return load_mnist()

    if canonical_name == "fashion_mnist":
        return load_fashion_mnist()

    raise ValueError(f"No tensorflow loader implemented for '{canonical_name}'")


def load_mnist():
    try:
        from tensorflow.keras.datasets import mnist
    except ImportError:
        raise ImportError(
            "Loading MNIST requires the optional dependency 'tensorflow'. "
            "Please install tensorflow before using this dataset."
        )

    return mnist.load_data()


def load_fashion_mnist():
    try:
        from tensorflow.keras.datasets import fashion_mnist
    except ImportError:
        raise ImportError(
            "Loading Fashion MNIST requires the optional dependency 'tensorflow'. "
            "Please install tensorflow before using this dataset."
        )

    return fashion_mnist.load_data()
