import argparse

def the_expression(args):
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', dest = 'model_path', default = "/model")
    args = parser.parse_args()
    the_expression(args)
