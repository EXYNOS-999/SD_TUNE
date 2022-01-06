import argparse

from . import guided  # , v, cfg


def argument_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    subparsers.add_parser(
        "guided", parents=[guided.argument_parser()], help="Generate images with guided diffusion", add_help=False
    ).set_defaults(func=guided.main)
    # subparsers.add_parser(
    #     "v", parents=[v.argument_parser()], help="Generate images with v diffusion", add_help=False
    # ).set_defaults(func=v.main)
    # subparsers.add_parser(
    #     "cfg",
    #     parents=[cfg.argument_parser()],
    #     help="Generate images with classifier-free guided diffusion",
    #     add_help=False,
    # ).set_defaults(func=cfg.main)
    return parser