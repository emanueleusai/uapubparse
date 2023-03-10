import argparse,bibtexparser,urllib,json
# from urllib.request import urlopen
  
# import json

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


inspire_ids=[]
arxiv_ids=[]

with open(args.filename+'.html') as f:
	lines = f.readlines()
	for line in lines:
		if 'inspirehep.net/literature' in line:
			inspire_id=line.split['/'][-1][:-2]
			inspire_ids.append(inspire_id)
		if 'arxiv.org/abs' in line:
			arxiv_id=line.split['/'][-1][:-2]
			arxiv_ids.append(arxiv_id)
if len(inspire_ids)!=len(arxiv_ids):
	print('inspire ids and arxiv ids do not match')

for iid in inspire_ids:
	url='https://inspirehep.net/api/literature/'+iid
	response = urllib.request.urlopen(url)
	data_json = json.loads(response.read())
	data_json['metadata']['imprints'][0]["date"]



bibparser = bibtexparser.bparser.BibTexParser()
bibparser.ignore_nonstandard_types = False

with open(args.filename+'.bib') as bibtex_input_file:
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
'$\\sqrt{s} = 13\\,\\text {Te}\\text {V} $':'sqrt(s) = 13 TeV',
"Z($\\nu\\bar{\\nu}$)V(q$\\bar{q}$')":'Z(nu nu)V(qq)',
'Image 1':'sqrt(s_NN) = 5.02',
'$\\sqrt {s}$ = 13\\,\\,TeV':'sqrt(s) = 13 TeV',
'$t \\bar t$':'ttbar',
'137 fb$^{−1}$':'137/fb',
'$\\sqrt{s} = $':'sqrt(s) =',
'$\\sqrt s$ =13\\,\\,TeV':'sqrt(s) = 13 TeV',
't$ \\overline{t} $\\ensuremath{\\gamma}':'ttgamma',
'J$/\\psi$':'J/psi',
'$\\sqrt{s_\\mathrm{NN}} =$':'sqrt(s_NN) =',
'$\\gamma$':'gamma',
'$\\tau\\tau$':'tautau',
'$\\to$':'to',
'W$^\\pm\\gamma\\gamma$':'W gamma gamma',
'$\\gamma\\gamma$':'gamma gamma',
'$\\sqrt{s} = 13\\,\\text {TeV} $':'sqrt(s) = 13 TeV',
'$\\sqrt{s} = 13\\,{\\text {TeV}} $':'sqrt(s) = 13 TeV',
'$Z$':'Z',
'$\\sqrt {s_{NN}}$=5.02\\,\\,TeV':'sqrt(s_NN) = 5.02 TeV',
'${\\text {Z}}$':'Z',
'${\\text {p}}{\\text {p}}$':'pp',
'${\\mathrm{Z}}_{\\mathrm{}}^{\\mathrm{}}$':'',
'$\\Xi^-_\\mathrm{b} \\pi^+ \\pi^-$':'Xi_b- pi+ pi-',
'$\\sqrt {s}$=13\\,\\,TeV':'sqrt(s) = 13 TeV',
'$ \\sqrt{s_{\\mathrm{NN}}} $':'sqrt(s_NN)',
'$\\to$$\\mathcal{A}\\mathcal{A}$$\\to$':'to AA to',
'$\\mathrm{t\\bar{t}}$':'ttbar',
'$\\tau\\tau\\tau\\tau$':'tautautautau',
'$\\sqrt{s}= 7$':'sqrt(s) = 7',
'$ \\tau\\tau$':'tautau',
# '':'',
# '':'',
# '':'',
# '':'',
# '':'',
# '':'',
# '':'',
# '':'',
# '':'',
# '':'',
# '':'',
}

# L799

# "(TOTEM Collaboration)\textdaggerdbl{}, (CMS Collaboration)\textdagger{}, TOTEM, CMS"

	for i,entry in enumerate(bib_db.entries):

		#remove double curly braces
		for key in entry:
			if entry[key][0]=='{' and entry[key][-1]=='}':
				bib_db.entries[i][key]=entry[key][1:-1]

		if 'archivePrefix' in entry.keys():
			if entry['archivePrefix']=="arXiv":
				arxivid=entry['eprint']
				bib_db[i]['url']="https://arxiv.org/pdf/"+arxivid+".pdf"
				# https://arxiv.org/pdf/2102.13080.pdf

		if "collaboration" in entry.keys():
			if 'CMS' in entry['collaboration']:
				bib_db[i]['author']="Collaboration, CMS and Gleyzer, Sergei and Rumerio, Paolo and Usai, Emanuele"
				# author = "Collaboration, CMS and Usai, Emanuele and Gleyzer, Sergei",

		if "doi" in entry.keys():
			doi='https://doi.org/'+entry['doi']
			bib_db[i]['doi']=doi

	


# https://doi.org/10.1103/PhysRevLett.126.252003
# "10.1103/PhysRevD.104.052001",
	

	with open(args.filename.replace('.bib','')+'_parsed.bib', 'w') as bibtex_output_file:
		bibtexparser.dump(bib_db, bibtex_output_file)
