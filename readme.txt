Operating system:  Linux


To reproduce disease MOA prediction

cd thiswork
type 
./scan_all_ef.job 

wait for results at 
ef-fexactpval-gene-z1.65-q0.05-noX-filt1.0/*_ef.txt , 1,2,3,4 ... represent disease index (see data/drug_indication_comb_cls_indication.ind for mapping)
each file contains: 
column 1 : internal human protein ID
       2 : # of drugs NOT having the indication binding to the protein
       3 : column 2/total # of drugs NOT having the indication
       4 : # of drugs having the indication  binding to the protein
       5 : column 4/total # of drugs having the indication 
 (comment: column 2/column 3 + column 4/column 5 = total # of drugs = 2095 )
       6 :  relative risk defined on the association table (see eqs. 2a,2b)
       7 :  z-score of the association table (used the Normal approximation to the Hypergeometric distribution to calculate z-score)
       8 :  p-value of the association table (Fisher's exact test)
       9 :  q-value
       10 : gene ID
       11 : Uniprot-KB ID.

Check against our calculation at subdirectory   "thisworksresult"


To reproduce  disease-disease relations

type 
./scan_allpairoverlap_ef-fexactpval_q_noX_fexact_z1.65_filt1.0_py.job 

Wait for output at 
ov-fexactpval-gene-z1.65-q0.05-noX-filt1.0-py/*_ov.txt 
each file contains: (ranked by p-value)
column 1: DOID of self
       2: DOIDs of the other paireds
       3: # of proteins of self
       4: # of proteins of the other paired 
       5: # of overlapped proteins between self and the other paired
       6: z-score (assuming normal distribution of the # of overlapped proteins)
       7: p-value 
       8: J-score
       9: q-value
Check against our calculation at subdirectory   "thisworksresult"


To reproduce disease-disease relations after indication-drug relationship predicted by MEDICASCY been permuted  

run similar programs as above in directory "permutedrugdisease"

NOTICE, the only difference between "lemedisco" and "permutedrugdisease"
is that the former used "data/all_zscore.out"  while the latter used "data/all_zscore_permutedis.out"
Each row of the file has the z-scores of a drug to the 3608 indications (first 3608 columns). 
The contents of the two files are identical except  we randomly shuffled the last column of drug IDs:
it means the MEDICASCY predicted indications of each drug are randomly replaced by another drug's indications. 
You will notice that for the "permutedrugdisease" method, most of the output at 
ef-fexactpval-gene-z1.65-q0.05-noX-filt1.0/*_ef.txt  will be empty because very few diseases have proteins with 
q-value < 0.05. 


Similar to "permutedrugdisease", "permutedrugprotein" only changed "all_zscore.out" to  "all_zscore_permuteproteindrug.out"
The content of "all_zscore_permuteproteindrug.out" is similar to "all_zscore.out" but re-predicted indications by MEDICASCY 
due to permuted targets of drugs and a given drug's protein associations are replaced by those of a random drug's. 

