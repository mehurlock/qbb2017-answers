time velveth ~/qbb2017-answers/week_2/velvet_low/ 31 -fastq reads_low_1.fastq reads_low_2.fastq 
real	0m0.007s
user	0m0.001s
sys	0m0.002s

time velvetg ~/qbb2017-answers/week_2/velvet_low/ 
real	0m0.015s
user	0m0.002s
sys	0m0.004s

./contig_iterator.py contigs.fa 

Max: 998
Min: 61
Mean: 186.8
Number: 305
N50: 248

lastz reference.fasta contigs.fa --chain --format=general:zstart1,end1,name2 > unsorted_out.out

sort -k 1,1 -n unsorted.out > sorted.out

./file_converter sorted.out velvet_low

spades.py --12 reads_low_1.fastq --12 reads_low_2.fastq -o ~/qbb2017-answers/week_2/SPAdes_Low/
real	0m3.611s
user	0m4.085s
sys	0m1.217s

./contig_iterator.py contigs.fasta
Max: 1409
Min: 207
Mean: 379.8
Number: 123
N50: 372

lastz reference.fasta contigs.fasta --chain --format=general:zstart1,end1,name2 > unsorted.out

sort -k 1,1 -n unsorted.out > sorted.out

time spades.py --12 reads_low_1.fastq --12 reads_low_2.fastq --nanopore MAP006.subset.fa -o ~/qbb2017-answers/week_2/SPAdes_Low_nano/
real	0m17.655s
user	0m45.831s
sys	0m6.333s

./contig_iterator.py contigs.fasta
Max: 6731
Min: 207
Mean: 1096.33
Number: 64
N50: 2673

lastz reference.fasta contigs.fa --chain --format=general:zstart1,end1,name2 > unsorted_out.out

sort -k 1,1 -n unsorted.out > sorted.out

time velveth ~/qbb2017-answers/week_2/velvet_high/ 31 -fastq reads_1.fastq -fastq reads_2.fastq 
real	0m7.235s
user	0m6.902s
sys	0m0.314s

time velvetg ~/qbb2017-answers/week_2/velvet_high/
real	0m11.013s
user	0m10.781s
sys	0m0.208s

./contig_iterator.py contigs.fa
Max: 33235
Min: 61
Mean: 9096.45
Number: 11
N50: 19911

lastz reference.fasta contigs.fa --chain --format=general:zstart1,end1,name2 > unsorted.out

sort -k 1,1 -n unsorted.out > sorted.out

./file_converter.py sorted.out velvet_high

time spades.py --12 reads_1.fastq --12 reads_2.fastq -o ~/qbb2017-answers/week_2/SPAdes_high
real	2m13.930s
user	5m25.958s
sys	0m11.767s

./contig_iterator.py contigs.fasta 
Max: 99915
Min: 111
Mean: 50013.0
Number: 2
N50: 99915

lastz reference.fasta contigs.fasta --chain --format=general:zstart1,end1,name2 > unsorted.out

sort -k 1,1 -n unsorted.out > sorted.out

./file_converter.py sorted.out SPAdes_high