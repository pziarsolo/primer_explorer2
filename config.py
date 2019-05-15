from pathlib import Path

BLACKLISTED_SEQS = [b'N', b'AAAA', b'TTTT', b'CCCC', b'GGGG']
KMERS_GENERATOR_FASTA = Path(
    "/home/jope/devel3/primer_experience/test_kmers.fa")
CACHE_DIR = Path("/home/jope/devel3/primer_experience/cache")
KMER_LENGTH = 8
G_CHAR = ord(b'G')
C_CHAR = ord(b'C')

import re
from collections import Counter

LOW_GC = 0.5
HIGH_GC = 0.75
KEEP_BEST = 100
LOW_GC = 0.50
HIGH_GC = 0.75
DUST_WINDOWSIZE = 64
DUST_WINDOWSTEP = 32
DEFAULT_DUST_THRESHOLD = 7
MAX_PCR_LENGTH = 1000
MIN_PCR_VIABLE_LENGTH = 300

PRIMER3_CONFIG_FPATH = "/home/jope/soft/primer3-2.3.7/src/primer3_config/"
PRIMER3_CORE_FPATH = "/home/jope/soft/primer3-2.3.7/src/primer3_core"

COMPLEMENTARY_BASES = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', '-': '-'}
MELTING_TEMPERATURE_THRESHOLD = 0
MAX_COMP_END = 3
MAX_COMP_ANY = 5
MAX_COMP_ANY_FACTOR = 0.44
EXPLANATION_LEFT_PRIMER = re.compile("PRIMER_LEFT_EXPLAIN=.+\n")
EXPLANATION_RIGHT_PRIMER = re.compile("PRIMER_RIGHT_EXPLAIN=.+\n")
PRIMER_SEQUENCE = re.compile("SEQUENCE_PRIMER=.+\n")
REV_PRIMER_SEQUENCE = re.compile("SEQUENCE_PRIMER_REVCOMP=.+\n")
PAIR_MSG = re.compile("PRIMER_PAIR_EXPLAIN=.+\n")
LEFT_MSG = re.compile("PRIMER_LEFT_0_PROBLEMS=.+\n")
RIGHT_MSG = re.compile("PRIMER_RIGHT_0_PROBLEMS=.+\n")
THERMO_MSG = re.compile("PRIMER_THERMODYNAMIC_OLIGO_ALIGNMENT=.+\n")
OK_PRIMER3_MSG = "considered 1, ok 1"


KMER_PRIMER3_FILTERING_CRITERIA = {"primer3_config_fpath": PRIMER3_CONFIG_FPATH,
                                   "primer3_core_fpath": PRIMER3_CORE_FPATH,
                                   "tm_threshold": MELTING_TEMPERATURE_THRESHOLD,
                                   "max_complementary_end": MAX_COMP_END,
                                   "max_complementary_any": MAX_COMP_ANY,
                                   "max_complementary_factor": MAX_COMP_ANY_FACTOR,
                                   "max_diff_temp": 40}
PAIR_PRIMER3_FILTERING_CRITERIA = {"primer3_config_fpath": PRIMER3_CONFIG_FPATH,
                                   "primer3_core_fpath": PRIMER3_CORE_FPATH,
                                   "tm_threshold": MELTING_TEMPERATURE_THRESHOLD,
                                   "max_complementary_end": MAX_COMP_END,
                                   "max_complementary_any": MAX_COMP_ANY,
                                   "max_complementary_factor": MAX_COMP_ANY_FACTOR,
                                   "max_diff_temp": 40}
MAX_PCR_PRODUCT_LENGTH = 1000

PCR_PRODUCTS_PICKLE = "pcr_products_results.pickle"
PCR_ANNOTATION = "pcr_annotation.pickle"
