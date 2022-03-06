import argparse

def train(args):
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', dest = 'model_path', default = "/model")
    parser.add_argument('-d', dest = 'data_path', default = "/dataset")
    args = parser.parse_args()
    train(args)
