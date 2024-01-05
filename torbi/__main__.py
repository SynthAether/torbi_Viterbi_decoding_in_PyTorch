import yapecs
from pathlib import Path

import torbi


###############################################################################
# Entry point
###############################################################################


def parse_args():
    """Parse command-line arguments"""
    parser = yapecs.ArgumentParser(
        description='Synthesize speech from features')
    parser.add_argument(
        '--input_files',
        type=Path,
        nargs='+',
        required=True,
        help='Time-varying log-categorical distribution files')
    parser.add_argument(
        '--output_files',
        type=Path,
        nargs='+',
        required=True,
        help='Files to save decoded indices')
    parser.add_argument(
        '--transition_file',
        type=Path,
        help='Log-categorical transition matrix file; defaults to uniform')
    parser.add_argument(
        '--initial_file',
        type=Path,
        help='Log-categorical initial distribution file; defaults to uniform')
    parser.add_argument(
        '--log_probs',
        action='store_true',
        help='Whether inputs are in (natural) log space')
    parser.add_argument(
        '--gpu',
        type=int,
        help='GPU index to use for decoding. Defaults to CPU.')
    return parser.parse_known_args()[0]


torbi.from_files_to_files(**vars(parse_args()))