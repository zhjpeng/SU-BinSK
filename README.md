# SU-BinSK
A Suit of Utilities for Bioinformatic Skills


1. Get the location of "N" in target genome
```
python3 LocateGenome-N.py toy.fasta > N_location.txt
```

chr1 3646  5086 <br>
chr1  6457  7082 <br>
chr1  9076  9956 <br>
chr1  14186 14187 <br>

You can affirm the result by `seqtk subseq toy.fasta N_location.txt`
