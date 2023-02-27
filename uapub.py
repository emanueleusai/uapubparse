import argparse,bibtexparser


parser = argparse.ArgumentParser(
                    prog = 'uapub',
                    description = 'Format publications for UA Watermark system',
                    epilog = 'Goodbye.')

parser.add_argument('filename')           # positional argument
# parser.add_argument('-c', '--count')      # option that takes a value
# parser.add_argument('-v', '--verbose',
#                     action='store_true')  # on/off flag

args = parser.parse_args()

# print(args.filename)



bibparser = bibtexparser.bparser.BibTexParser()
bibparser.ignore_nonstandard_types = False

with open(args.filename) as bibtex_input_file:
    bib_db = bibtexparser.load(bibtex_input_file,bibparser)

# print(bib_db.entries)

for i,entry in enumerate(bib_db.entries):

	#remove double curly braces
	for key in entry:
		if entry[key][0]=='{' and entry[key][-1]=='}':
			bib_db.entries[i][key]=entry[key][1:-1]

	

with open(args.filename.replace('.bib','')+'_parsed.bib', 'w') as bibtex_output_file:
    bibtexparser.dump(bib_db, bibtex_output_file)
