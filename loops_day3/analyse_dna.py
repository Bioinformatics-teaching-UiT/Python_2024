"""
1. Do the following sequences of DNA contain the pieces given after them?
If so, how many times?

2. Then, count in total how many times A, T, C, G occur, using a dictionary and one loop only.

3. Transcribe this sequence to RNA.

Bonus:
    Complement this strand of DNA using a list comprehension. Then transcribe that complemented strain.
"""

### 1

sequence_1 = """AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGT
	GGATTAAAAAAAGAGTGTCTGATAGCAGCAGCTTTTCATTCTGACTGCAA
        CGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCACGATGTCGGATCGTAT
	GCTAGTCAGTGTGTTTTTTTTAAAAGCAGGCTGCATGCTGTGTGTGTGTACGTATATGAAAAAATCAGC"""

piece_1_1 = 'GCA'
piece_1_2 = 'ATT'
piece_1_3 = 'TCA'
piece_1_4 = 'GCAAATCC'
