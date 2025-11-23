def to_rna(dna_strand):
    complement = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }

    return "".join(complement[n] for n in dna_strand)