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

#title substitutions database
titlesub={
'$\\sqrt{s} =$':'sqrt(s)',
"\\'":"",
' s=13TeV':' sqrt(s) = 13 TeV',
'$ \\sqrt{\\mathrm{s}} $':'sqrt(s)',
'$\\sqrt{s}$':'sqrt(s)',
'$\\sqrt{s_\\mathrm{NN}}$':'sqrt(s_NN)',
'$\\Upsilon$':'Upsilon',
' s=13\\,\\,TeV':' sqrt(s) = 13 TeV',
'$\\sqrt s$=13\\,\\,TeV':'sqrt(s) = 13 TeV',
'B$^0$$\\to$$\\psi$(2S)K$^0_\\mathrm{S}\\pi^+\\pi^-$':'B0 to psi(2S) K0_S pi+ pi-',
'B$^0_\\mathrm{S}$$\\to$$\\psi$(2S)K$^0_\\mathrm{S}$':'B0_S to psi(2S) K0_S',
'$ \\sqrt{s} $':'sqrt(s)',
'$\\mathrm{t\bar{t}}\\gamma$':'ttgamma',
'$B_c^+$':'Bc+',
'5.02\\,\\,TeV':'5.02 TeV',
'$W$':'W',
'$\\sqrt s$':'sqrt(s)',
' 13\\,\\,TeV':'13 TeV',
'$ \\mathrm{t}\\overline{\\mathrm{t}} $':'ttbar',
'\\ensuremath{\\ell}\\ensuremath{\\nu}qq':'l nu q q',
'\\textendash{}':'-',
'$\\sqrt{s}=8\\,\\text {TeV} $':'sqrt(s) = 8 TeV',
'W$^\\pm\\gamma$':'Wgamma',
'$\\kappa_\\text{t}$':'kt',
'$\\text{t}\\bar{\\text{t}}$':'tt',
'$\\text{t}\\bar{\\text{t}}\\text{t}\\bar{\\text{t}}$':'tttt',
'Run~2':'Run 2',
'J/$\\psi$':'J/psi',
'$\\sqrt{s}=13\\text{ }\\text{ }\\mathrm{TeV}$':'sqrt(s) = 13 TeV',
'$\\sqrt{s}=13\\,\\text {TeV} $':'sqrt(s) = 13 TeV',
'$CP$':'CP',
'$\\tau$':'tau',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
'':'',
}

L799

"(TOTEM Collaboration)\textdaggerdbl{}, (CMS Collaboration)\textdagger{}, TOTEM, CMS"

for i,entry in enumerate(bib_db.entries):

	#remove double curly braces
	for key in entry:
		if entry[key][0]=='{' and entry[key][-1]=='}':
			bib_db.entries[i][key]=entry[key][1:-1]

	#

	

with open(args.filename.replace('.bib','')+'_parsed.bib', 'w') as bibtex_output_file:
    bibtexparser.dump(bib_db, bibtex_output_file)
