import argparse

def run(args):
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', dest = 'model_path', default = "/model")
    args = parser.parse_args()
    run(args)
