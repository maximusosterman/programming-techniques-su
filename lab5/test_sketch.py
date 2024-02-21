import dna as DNA

s4 = DNA.DnaSeq('s4', 'BGGGGGGGGAAAGGGGGE')
s5 = DNA.DnaSeq('s5', 'AAATTTTTTTTTTTTTTTTTAT')

def check_exact_overlap(a: DNA.DnaSeq, b: DNA.DnaSeq, min_len: int =10):
    """Cheks the overlap between two DNA sequences. Goes through the back to the beginning of sequence A. Front to back for sequence B.

    Args:
        a (DnaSeq): DnaObject to check overlap
        b (DnaSeq): DnaObject to check for overlap
        min_len (int, optional): The shortest in which the overlap has to be to be counted. Defaults to 10. 

    Returns:
        _type_: Returns a string of the overlap. If none is found then 0 will be returned.
    """

    overlap_string = ""
    for i in range(len(a.seq)):
        if b.seq[:i] in a.seq:
            print(a.seq[-len((b.seq[:i])):])
            overlap_string = b.seq[:i]

    if len(overlap_string) >= min_len:
        return len(overlap_string)
    
    return 0

def comb():
    data = ["s0", "s1", "s2", "s3", "s4"]
    result_dict = {}
    for current_dna in data:
        current_dna_dict = {}
        for compared_dna in data:
            if compared_dna is not current_dna:
                if compared_dna not in result_dict:
                    print(f"{current_dna} x {compared_dna}")
                    current_dna_dict[compared_dna] = 1
        result_dict[current_dna] = current_dna_dict

    return result_dict


if __name__ == "__main__":
    print(comb())