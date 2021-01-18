#===DESCRIPTION=================================================================
# A script to extract mitogenome stats from the INSDSeq XML output of NCBI 
# written by C. Jonathan Schmitt 

import xml.etree.ElementTree as ET
import csv

# read in xml file, in this case saved in same directory where you call this script from
tree = ET.parse("mitogenomes_amphibia.xml")
root = tree.getroot()

# open a file for writing

mitogenome_data = open('/Users/schmitty/Documents/CJS/projects/bird_genome_review/mitogenomes_amphibia.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(mitogenome_data)
mitogenome_head = []

# create the column names
col_names = ['accession', 'submission_date', 'sequence_length', 'organism', ]
csvwriter.writerow(col_names)

count = 0
for member in root.findall('INSDSeq'):
	mitogenome = []
	if count == 0:
		accession = member.find('INSDSeq_primary-accession').tag
		mitogenome_head.append(accession)
		submission_date = member.find('INSDSeq_create-date').tag
		mitogenome_head.append(submission_date)
		sequence_length = member.find('INSDSeq_length').tag
		mitogenome_head.append(sequence_length)
		organism = member.find('INSDSeq_organism').tag
		mitogenome_head.append(organism)
		count = count + 1
		
	accession = member.find('INSDSeq_primary-accession').text
	mitogenome.append(accession)
	submission_date = member.find('INSDSeq_create-date').text
	mitogenome.append(submission_date)
	sequence_length = member.find('INSDSeq_length').text
	mitogenome.append(sequence_length)
	organism = member.find('INSDSeq_organism').text
	mitogenome.append(organism)
	csvwriter.writerow(mitogenome)
mitogenome_data.close()