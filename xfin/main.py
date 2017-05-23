import sys
import argparse

def kelly_formula(args):
    fraction = 0
    if args.bet == 0:
          fraction =0
    else:
        fraction = (args.bet*args.pro+args.pro-1)/args.bet

    print "fraction = {0}".format(fraction)
    return fraction

def main(args=None):
    """The main routine."""
    # if args is None:
    #    args = sys.argv[1:]
    # 1.The main framework
    parser = argparse.ArgumentParser(description='The most important financial function')

    subparser = parser.add_subparsers(title="Commands",
        description="Subcommands for different functions")

    # 2.Kelly formula
    kelly = subparser.add_parser("kelly", help="Kerry formula",
        description="Kerry calculation formula")
    kelly.add_argument("-b", "--bet", type=float,
        help="The odds of betting")
    kelly.add_argument("-p", "--pro", type=float,
        help="The probability of winning")
    kelly.set_defaults(func=kelly_formula)

    args = parser.parse_args()
    args.func(args)

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.

if __name__ == "__main__":
    main()

    
