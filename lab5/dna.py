class DnaSeq:
    def __init__(self, accession: str, seq: str):

        if not accession or not seq:
            raise ValueError

        self.accession = accession
        self.seq = seq 
            
    def __len__(self):
        return len(self.seq)

    def __str__(self):
        return f"<DnaSeq accession='{self.accession}'>" 


def read_dna(filename: str) -> list[DnaSeq]:
    """Reads DNA sequences from a text file and returns a list of DnaSeq Objects

    Args:
        filename (str): filename in which to read the DNA sequences from.

    Returns:
        list[DnaSeq]: List with DnaSeq objects
    """
    dna_sequences = []

    try:
        with open(filename, "r") as dna_file:
            dna_file_iter = iter(dna_file)
            for line in dna_file_iter:
                if line[0] == ">":
                    accession = line.replace(">", "").strip()
                    sequence = next(dna_file_iter).strip()
                    dna_sequences.append(DnaSeq(accession, sequence))

    except Exception as e:
        print(f"Unexpected error opening file: {filename}")
        print("Error:", e)

    return dna_sequences


def check_exact_overlap(a: DnaSeq, b: DnaSeq, min_len: int =10):
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
        if a.seq[-len((b.seq[:i])):] == b.seq[:i]:
            overlap_string = b.seq[:i]

    if len(overlap_string) >= min_len:
        return len(overlap_string)
    
    return 0


def overlaps(dna_objects: list[DnaSeq], overlap_detection) -> dict[dict]:
    
    result_dict = {}

    for current_dna in dna_objects:
        current_dna_dict = {}
        for compared_dna in dna_objects:
            if compared_dna.seq is not current_dna.seq:
                if compared_dna not in result_dict:
                    overlap_detected = overlap_detection(current_dna, compared_dna)
                    if overlap_detected != 0:
                        current_dna_dict[compared_dna.accession] = overlap_detected
                        print(current_dna.accession, "x",compared_dna.accession)
        result_dict[current_dna.accession] = current_dna_dict
            
    print(result_dict)
    return result_dict


#
# Testing code. You should not change any code below here. To run the tests
# uncomment the last line in the file.
#
def test_class_DnaSeq():
    s1 = DnaSeq('s1', 'ACGT')
    s2 = DnaSeq('s2', 'ATGTTTGTTTTTCTTGTTTTATTGCCACTAGTCTCTAGTCAGTGTGTTAATCTTACAACCAGAACTCAAT')
    assert len(s1) == 4, 'Your length method (__len__) is not correct.'
    assert len(s2) == 70, 'Your length method (__len__) is not correct.'

    assert str(s1) == "<DnaSeq accession='s1'>", 'The __str__ method is not following the specification.'
    assert str(s2) == "<DnaSeq accession='s2'>", 'The __str__ method is not following the specification.'

    # The rest of this function is verifying that we are indeed raising an exception.
    status = 0
    try:
        s3 = DnaSeq('', 'ACGT')
    except ValueError:
        status += 1
    try:
        s3 = DnaSeq('s3', None)
    except ValueError:
        status += 1

    try:
        s3 = DnaSeq(None, '')
    except ValueError:
        status += 1
    if status != 3:
        raise Exception('class DnaSeq does not raise a ValueError '
                        'exception with initialised with empty '
                        'accession and sequence.')
    print('DnaSeq passed')


def test_reading():
    dna1 = read_dna('ex1.fa')
    assert len(dna1) == 6, 'The file "ex1.fa" has exactly 6 sequences, but your code does not return that.'
    assert list(map(lambda x: x.accession, dna1)) == [f's{i}' for i in range(6)], 'The accessions are not read correctly'

    dna2 = read_dna('ex2.fa')
    assert len(dna2) == 6, 'The file "ex2.fa" has exactly 6 sequences, but your code does not return that.'

    covid = read_dna('sars_cov_2.fa')
    assert len(covid[0].seq) == 29903, 'The length of the genome in "sars_cov_2.fa" is 29903, but your code does not return that.'

    print('read_dna passed')


def test_overlap():
   s0 = DnaSeq('s0', 'AAACCC')
   s1 = DnaSeq('s1', 'CCCGGG')
   s2 = DnaSeq('s2', 'TTATCC')
   s3 = DnaSeq('s3', 'CCAGGG')
   s4 = DnaSeq('s4', 'GGGGGGGGAAAGGGGG')
   s5 = DnaSeq('s5', 'AAATTTTTTTTTTTTTTTTTAT')

   data1 = [s0, s1, s2, s3]
   assert check_exact_overlap(s0, s1, 2) == 3
   assert check_exact_overlap(s0, s1) == 0
   assert check_exact_overlap(s0, s3, 2) == 2
   assert check_exact_overlap(s1, s2, 2) == 0
   assert check_exact_overlap(s2, s1, 2) == 2
   assert check_exact_overlap(s2, s3, 2) == 2
   assert check_exact_overlap(s4, s5, 1) == 0, 'Do not allow "internal" substrings to overlap. s4 and s5 does not have an overlap.'
   assert check_exact_overlap(s4, s5, 2) == 0
   assert check_exact_overlap(s4, s5, 3) == 0
   assert check_exact_overlap(s5, s2, 1) == 4

   res0 = overlaps(data1, lambda s1, s2: check_exact_overlap(s1, s2, 2))
   assert len(res0) == 2, 'You get the wrong number of overlaps'
   assert res0 == {'s0': {'s1': 3, 's3': 2}, 's2': {'s1': 2, 's3': 2}}

   dna_data = read_dna('ex1.fa')
   res1 = overlaps(dna_data, check_exact_overlap)
   assert len(res1) == 5
   for left, right in [('s0', 's1'), ('s1', 's2'), ('s2', 's3'), ('s3', 's4'),
                       ('s4', 's5')]:
       assert res1[left][right], f'Missing overlap of {left} and {right} (in that order)'
   print('overlap code passed')



def test_all():
    test_class_DnaSeq()
    test_reading()
    test_overlap()
    print('Yay, all good')

# Uncomment this to test everything:
# test_all()
    
if __name__ == '__main__':
    test_overlap()

