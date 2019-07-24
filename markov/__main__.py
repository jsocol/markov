import argparse

from . import letters, words


def main(options):
    samples = []
    for fn in options.samples:
        with open(fn) as fp:
            samples.append(fp.read())

    if options.type == 'letters':
        print(letters.generate_from_samples(samples, options.ngram))
    else:
        print(words.generate_from_samples(samples, options.ngram))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='markov')
    parser.add_argument('-t', '--type', type=str, choices=['words', 'letters'],
                        default='letters')
    parser.add_argument('-n', '--ngram', type=int, default=3)
    parser.add_argument('samples', type=str, nargs='+', metavar='FILE',
                        help='A list of file names to use as samples')
    options = parser.parse_args()
    main(options)
