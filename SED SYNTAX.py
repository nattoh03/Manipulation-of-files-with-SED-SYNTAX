######## SED  SYNTAX ##########

#### 1
#### find and replace a pattern, all matching patterns at the eginning of rows (chr) will be changed to (Chromosome), leaving similar patterns within the body
sed 's/pattern_to_find/pattern_to_replace/' in_put_file
sed 's/chr/Chromosome/' anopheles.gff
ouput printed on screen


#### 2 
#### To find and replace a pattern both at the beginnig of row and other parts of th documents, must include a global flag (g)
sed 's/pattern_to_find/pattern_to_replace/g' in_put_file
sed 's/chr/Chromosome/g' anopheles.gff

#### 3
#### print out specific lines/rows in a file
## print the first 3 lines of the  anopheles.gff file
sed -n '1, 3p' anopheles.gff
## print the first 10 lines of the  anopheles.gff file
sed -n '1, 10p' anopheles.gff
##print the first 3 lines, then line 5 and 9 of the  anopheles.gff file
sed -n '1, 3p; 5p; 9p' anopheles.gff
## print the first line, then lines 3 to 5, followed by lines 7 to 9 of the  anopheles.gff file
sed -n '1p; 3, 5p; 7, 9p' anopheles.gff

#### 4
#### format file from tab-delimited format to comma separated 
sed 's/\t/,/' anopheles.gff
but this substitutues only the first character, therefore 
sed 's/\t/,/g' anopheles.gff 
 
#### 5
#### To add a pattern at the beginning of every line
sed 's/^/Organism_/g' anopheles.gff 

#### 6
#### To add a pattern at the end of every line
sed 's/$/_Organism/g' anopheles.gff


#### 7
#### To change case only on the first latter of each line
sed 's/[a-z]/\U&/' anopheles.gff

#### 8
#### To change all sequences to upper case
sed 's/[a-z]/\U&/g' anopheles.gff

#### 9
#### To match only lines with beginning with chr/ (i.e. manipulation of specific matching)
sed 's/^chr*/Organism_/g' anopheles.gff

#### To add P_falciparum at the beginning of each line of a fasta header
sed 's/^>/>P_falciparum/g' anopheles.gff

#### 10
#### use pipe to combine various functions instead of doing them one after another, e.g.changing to upper case, adding a name to a afster header, 
sed 's/[a-z]/\U&/g' anopheles.gff | sed 's/^>/>P_falciparum/g' anopheles.gff > modified_anopheles.gff







