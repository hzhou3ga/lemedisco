#!/usr/bin/env python 
import optparse
import sys
import os.path as op
import scipy.stats as ss

def hypergeom(m, n, n1, n2, p=False):
    if m <= 0: return 1.0
    mmin = m - 1
    mmax = min(n1, n2)
    return ss.hypergeom.cdf(mmax, n, n1, n2) - ss.hypergeom.cdf(mmin, n, n1, n2)

def with_genes(fftot, ffa, ffb):
    """
    given 3 genelists, calculate the p-value of the shared
    genes between fa and fb that are drawn from ftot.
    """

    ftot = frozenset(f.strip() for f in open(fftot) if f.strip())
    fa = frozenset(f.strip() for f in open(ffa) if f.strip())
    fb = frozenset(f.strip() for f in open(ffb) if f.strip())

    n1, n2 = len(fa), len(fb)
    m = len(fa.intersection(fb))
    n = len(ftot)

    print "A     : %-32s:%-5i" % (ffa, n1)
    print "B     : %-32s:%-5i" % (ffb, n2)
    print "total : %-32s:%-5i" % (fftot, n)
    print "shared: %-32s:%-5i" % (' ', m)
    return hypergeom(m, n, n1, n2)


def main():
    p = optparse.OptionParser(__doc__)
    opts, args = p.parse_args()
    if (len(args) not in (3, 4)):
        sys.exit(not p.print_help())
    if len(args) == 4 and not all(a.isdigit() for a in args):
        print >>sys.stderr, "four arguments must be integers"
        sys.exit(not p.print_help())
    elif len(args) == 3 and not all(op.exists(f) for f in args):
        sys.exit(not p.print_help())

    if len(args) == 4:
        args = map(long, args)
        m, n, n1, n2 = args
        print hypergeom(m, n, n1, n2)
    else:
        tot_genes, a_genes, b_genes = map(str.strip, args)
        print with_genes(tot_genes, a_genes, b_genes)

if __name__ == "__main__":
    import doctest
    if doctest.testmod(optionflags=doctest.ELLIPSIS).failed == 0:
        main()

