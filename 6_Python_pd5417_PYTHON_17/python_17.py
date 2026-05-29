from Bio import Entrez, SeqIO, pairwise2

Entrez.email = "zbigniew.lazar@gmail.com"

identyfikatory = ["JX669568", "JX669571"]

with Entrez.efetch(
    db="nucleotide",
    id=",".join(identyfikatory),
    rettype="fasta",
    retmode="text"
) as handle:
    rekordy = list(SeqIO.parse(handle, "fasta"))

SeqIO.write(rekordy, "sekwencje_genbank.fasta", "fasta")

print("Pobrano i zapisano sekwencje FASTA:")
for rekord in rekordy:
    print(rekord.id, len(rekord.seq))

rekordy_z_pliku = list(SeqIO.parse("sekwencje_genbank.fasta", "fasta"))

sekwencja_1 = str(rekordy_z_pliku[0].seq)
sekwencja_2 = str(rekordy_z_pliku[1].seq)

dopasowania = pairwise2.align.globalxx(sekwencja_1, sekwencja_2)

najlepsze = dopasowania[0]

print("\nNajlepsze dopasowanie:")
print(najlepsze.seqA[:200])
print(najlepsze.seqB[:200])

print("\nPunktacja dopasowania:", najlepsze.score)