from Bio import GenBank
from Bio.Seq import Seq

# pvc13_WT
with open('G:/dp/AlphaFold/PVC_FZhang/Supplementary_Data_1_Annotated_Plasmid_Maps/pAWP78-PVCpnf1-16.gb','r') as f1:
    for record in GenBank.parse(f1):
        pvc13_dna = Seq(record.sequence[17350:18877])
        pvc13_ptn = pvc13_dna.translate()
        pvc13_tip = pvc13_ptn[316:]

with open('G:/dp/AlphaFold/PVC_FZhang/ForPred/pvc13_WT0.fasta','w') as f2:
    f2.write('>pvc13_WT\n')
    f2.write(str(pvc13_tip))
    f2.write('\n')

# pAWP78-PVCpnf_pvc13-Ad5Knob
with open('G:/dp/AlphaFold/PVC_FZhang/Supplementary_Data_1_Annotated_Plasmid_Maps/pAWP78-PVCpnf_pvc13-Ad5Knob.gb','r') as f3:
    for record in GenBank.parse(f3):
        pvc13_dna1 = Seq(record.sequence[16867:18073])
        pvc13_dna2 = Seq(record.sequence[18073:18103])
        pvc13_dna3 = Seq(record.sequence[18103:18661])
        pvc13_dna4 = Seq(record.sequence[18661:18691])
        pvc13_dna5 = Seq(record.sequence[18691:18790])
        pvc13_dna = pvc13_dna1+pvc13_dna2+pvc13_dna3+pvc13_dna4+pvc13_dna5
        pvc13_ptn = pvc13_dna.translate()
        pvc13_tip = pvc13_ptn[316:]

with open('G:/dp/AlphaFold/PVC_FZhang/ForPred/pvc13_Ad5Knob.fasta','w') as f4:
    f4.write('>pvc13_Ad5Knob\n')
    f4.write(str(pvc13_tip))
    f4.write('\n')

