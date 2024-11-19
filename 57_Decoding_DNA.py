#57 Decoding DNA - ecoo12r1p2

def DNA_data() -> list:
    DNA_list = []

    while len(DNA_list) < 5:
        DNA_string = input()
        DNA_list.append(DNA_string)
    return DNA_list
    

# identify TATAAT promotr and return start of transcription index
def start_of_transcription(DNA_string: str) -> int:
    index = DNA_string.find("TATAAT")
    if index != -1:
        # find returns -1 if no such string found, so we can control for this case
        start_of_transcription = index + 10
        return start_of_transcription
    else:
        print("promoter not found in strand")
        return -1
            


def complementary_reversed(sequence):    
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    complement_sequence = "".join(complement[base] for base in sequence)
    return complement_sequence[::-1]


# identify base 6 terminator sequence
def end_of_transcription(dna_seq: str, transcription_start: int) -> int:
    length = 6 #length of terminatro sequence
    end_of_transcription = -1

    for i in range(transcription_start, len(dna_seq)):
        # extract candidate with base 6
        candidate = dna_seq[i:i + length]
        complementary_rev = complementary_reversed(candidate)

        #search for this complementary reversed sequence after the candidate sequence
        found_index = dna_seq.find(complementary_rev, i + length)

        if found_index != -1:
            end_of_transcription = i
            break
        
    #if no valid terminator found transcripton ends at end of strand
    if end_of_transcription == -1:
        print("no terminator sequences found")

    return end_of_transcription
  
#convert RNA              
def get_RNA(dna_seq, start_of_transcription, end_of_transcription):
        rna_code = {"A":"U","T":"A","C":"G","G":"C"}

        # get transcription unit segment
        dna_segment = dna_seq[start_of_transcription:end_of_transcription]

        # convert DNA to RNA
        rna_result = "".join(rna_code[base] for base in dna_segment)
        return rna_result
    

#Main program
dna_strings_lst = DNA_data()

for i in range(len(dna_strings_lst)):
    dna_seq = dna_strings_lst[i]
    transcription_start = start_of_transcription(dna_seq)
    if transcription_start == -1:
        continue
    transcription_end = end_of_transcription(dna_seq, transcription_start)
    if transcription_end == -1:
        continue
    rna_seq = get_RNA(dna_seq, transcription_start, transcription_end)
    print(f"{i+1}: {rna_seq}")






