import argparse, os

def main():
	parser = argparse.ArgumentParser(description='Script to retrieve the first allele of the loci given and concatenate them in a single fasta file.', epilog='by C I Mendes (cimendes@medicina.ulisboa.pt)')
	parser.add_argument('-l', '--loci', help='Path to directory containing the loci fasta files.')

	args = parser.parse_args()

	concatenate=''
	lociCount=0

	for item in os.listdir(args.loci):
		lociCount+=1
		with open (args.loci+item, 'r') as lociFile:
			for i, line in enumerate(lociFile):
				if i == 1: #second line - sequence for the first allele in the loci (files have the alleles ordered)
					concatenate+=line

	with open ('concatenatedLoci.fasta', 'w') as outFile:
		outFile.write('>' + str(args.loci) + '_concatenated_first_allele_in_' + str(lociCount) + '_loci\n')
		outFile.write(concatenate)
	
	print "concatenated sequence length: "
	print len(concatenate)


if __name__ == "__main__":
    main()