import argparse


def main():
    args = argparse.ArgumentParser()
    args.add_argument("--model-size", choices=["small", "medium", "large", "xl", "10B"], required=True)
    args.add_argument("--warm_up-step", type=int, required=True)
    args.add_argument("--execution-step", type=int, required=True)
    args.add_argument("--bench-type", required=True, choices=["forward", "backward", "all"])

    arg = args.parse_args()

    print(f"args{arg.model_size}")





if __name__ == "__main__":
    main()
