import argparse, os, csv

def main():

	parser = argparse.ArgumentParser(description='Script to compare the gene presence and absence file with chewBBACA scheme.', epilog='by C I Mendes (cimendes@medicina.ulisboa.pt)')
	parser.add_argument('-s', '--scheme', help='Path to directory containing the scheme.')
	parser.add_argument('-g', '--genes', help='Gene presence and absence file.')

	args = parser.parse_args()

	schemaGenes=[]
	for item in os.listdir(args.scheme):
		schemaGenes.append(item.split('.')[0])
	#print len(schemaGenes) #5435
	#print schemaGenes

	geneGroupsIn=[]
	geneGroupsIn_core=[]
	geneGroupsOut=[]
	geneGroupsOut_core=[]

	geneGroups=0
	core=0

	with open(args.genes, 'r') as csvfile:
		reader = csv.reader(csvfile)
		#skip header
		reader.next()

		for row in reader:
			genes=row[14:]
			flag=False
			if '' not in genes:
				core+=1
			for item in genes:
				if item in schemaGenes:
					flag=True
			if flag:
				geneGroupsIn.append(row[0])
				if '' not in genes:
					geneGroupsIn_core.append(row[0])
			else:
				geneGroupsOut.append(row[0])
				if '' not in genes:
					geneGroupsOut_core.append(row[0])
			geneGroups+=1

	print 'Genes in chewBBACA: ' + str(len(set(geneGroupsIn)))
	print '... ' + str(len(set(geneGroupsIn_core))) + ' are core genes'
	print 'Genes not in chewBBACA: ' + str(len(set(geneGroupsOut)))
	print '... ' + str(len(set(geneGroupsOut_core))) + ' are core genes'

	print ('*** Total Genes in pan-genome: ***')
	print geneGroups

	print ('*** Total Genes in Scheme: ***')
	print len(schemaGenes)

	print "core genes: " + str(core)

if __name__ == "__main__":
    main()