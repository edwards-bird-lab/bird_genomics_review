#===DESCRIPTION=================================================================
# A script to extract assembly stats from the XML output of NCBI #
# Note that for this script to work you'll probably need to create a new line at
# the beginning of the XML file and add <> to that line, as well as create a new 
# line at the end of the XML file and add </> to that line
# written by C. Jonathan Schmitt #

import xml.etree.ElementTree as ET
import csv

# read in xml file, in this case saved in same directory where you call this script from
tree = ET.parse("assembly_result_aves.xml")
root = tree.getroot()

# open a file for writing
Assembly_data = open('/n/home12/schmitt/AssemblyData_aves.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Assembly_data)
assembly_head = []

# create the column names
col_names = ['AssemblyAccession', 'Organism', 'SpeciesName', 'Coverage','SubmissionDate','SubmitterOrganization','ContigN50','ScaffoldN50', 'BioSample']
csvwriter.writerow(col_names)

count = 0
for member in root.findall('DocumentSummary'):
	assembly = []
	if count == 0:
		AssemblyAccession = member.find('AssemblyAccession').tag
		assembly_head.append(AssemblyAccession)
		Organism = member.find('Organism').tag
		assembly_head.append(Organism)
		SpeciesName = member.find('SpeciesName').tag
		assembly_head.append(SpeciesName)
		Coverage = member.find('Coverage').tag
		assembly_head.append(Coverage)
		SubmissionDate = member.find('SubmissionDate').tag
		assembly_head.append(SubmissionDate)
		SubmitterOrganization = member.find('SubmitterOrganization').tag
		assembly_head.append(SubmitterOrganization)
		ContigN50 = member.find('ContigN50').tag
		assembly_head.append(ContigN50)
		ScaffoldN50 = member.find('ScaffoldN50').tag
		assembly_head.append(ScaffoldN50)
		BioSampleAccn = member.find('BioSampleAccn').tag
		assembly_head.append(BioSampleAccn)
		count = count + 1

	AssemblyAccession = member.find('AssemblyAccession').text
	assembly.append(AssemblyAccession)
	Organism = member.find('Organism').text
	assembly.append(Organism)
	SpeciesName = member.find('SpeciesName').text
	assembly.append(SpeciesName)
	Coverage = member.find('Coverage').text
	assembly.append(Coverage)
	SubmissionDate = member.find('SubmissionDate').text
	assembly.append(SubmissionDate)
	SubmitterOrganization = member.find('SubmitterOrganization').text
	assembly.append(SubmitterOrganization)
	ContigN50 = member.find('ContigN50').text
	assembly.append(ContigN50)
	ScaffoldN50 = member.find('ScaffoldN50').text
	assembly.append(ScaffoldN50)
	BioSampleAccn = member.find('BioSampleAccn').text
	assembly.append(BioSampleAccn)
	csvwriter.writerow(assembly)
Assembly_data.close()