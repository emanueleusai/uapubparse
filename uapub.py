import argparse,bibtexparser,json
from urllib.request import urlopen
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
doi_ids=[]
pub_dates=[]
journals=[]

with open(args.filename+'.html') as f:
	lines = f.readlines()
	for line in lines:
		if 'inspirehep.net/literature' in line:
			inspire_id=line.split('/')[-1][:-3]
			inspire_ids.append(inspire_id)
		# if 'doi.org' in line: #####long term would be nice to match on doi
		# 	doi_id=line.split('/')[-2]+'/'+line.split('/')[-1]
		# 	doi_ids.append(doi_id)
# 
# print(len(inspire_ids))
# print(len(doi_ids))

journal_dict={
	'the European Physical Journal C':'Eur. Phys. J. C',
	'the Journal of High Energy Physics':'JHEP',
	'Physics Letters B':'Phys. Lett. B',
	'the Journal of Instrumentation':'JINST',
	'Physical Review D':'Phys. Rev. D',
	'Phys Rev. Letters':'Phys. Rev. Lett.',
	'Physical Review Letters':'Phys. Rev. Lett.',
}

not_published=[]
for i,iid in enumerate(inspire_ids):
	url='https://inspirehep.net/api/literature/'+iid
	print(url)
	response = urlopen(url)
	data_json = json.loads(response.read())
	if 'imprints' in data_json['metadata'].keys():
		date=data_json['metadata']['imprints'][0]["date"]
		pub_dates.append(date.split('-'))
	else:
		not_published.append(i)
		pub_dates.append('not published')

	if args.filename=='accepted':
		if 'public_notes' in data_json['metadata'].keys():
			journal_notes=data_json['metadata']['public_notes'][0]["value"]
			journal_raw=journal_notes.split('Submitted to ')[1].split('. All figures')[0]

			journals.append(journal_dict[journal_raw])
		else:
			if iid=="2088291":
				journals.append('JHEP')
			else:
				journals.append(url)
# print(journals)
# assert false


		# print("notin ",url)


print(pub_dates)

month_dict={
	'01':'jan',
	'02':'feb',
	'03':'mar',
	'04':'apr',
	'05':'may',
	'06':'jun',
	'07':'jul',
	'08':'aug',
	'09':'sep',
	'10':'oct',
	'11':'nov',
	'12':'dec',
}

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
'$\\mathrm{t\\bar{t}}\\gamma$':'ttgamma',
'$\\sqrt{s_{NN}}$':'sqrt(s_NN)',
'$\\sqrt {s_{NN}}$':'sqrt(s_NN)',
'$\\mu$':'mu',
'$\\mu\\tau$':'mutau',
'$\\mathcal{A}\\mathcal{A}$':' AA ',
'W$^+W^-$':'WW',
"$'$":"' ",
'$\\eta$':'eta',
"${\\sqrt{s}=13\\, \\text {TeV}}$":"sqrt(s) = 13 TeV",
"$ \\textrm{t}\\overline{\\textrm{t}} $":"ttbar ",
"$\\tau $":"tau ",
"$\\sqrt{s}=13$":"sqrt(s) = 13",
"$\\hbox {t}\\overline{\\hbox {t}}$":"",
"$^0_\\mathrm{S}$to$\\mu^+\\mu^-$":"0_S to mu+ mu-",
"$^0$to$\\mu^+\\mu^-$":"0 to mu+ mu-",
"$ \\sqrt{s_{\\textrm{NN}}} $":"sqrt(s_NN)",
"$\\text {pp}$":"pp",
"$\\sqrt{s}=13\\,\\textrm{TeV}$":"sqrt(s) = 13 TeV",
"$\\sqrt{s}=13\\,\\text {Te\\hspace{-.08em}V} $":"sqrt(s) = 13 TeV",
"$\\sqrt{s} = 13\\,\\text {Te}\\hspace{-.08em}\\text {V} $":"sqrt(s) = 13 TeV",
"$ \\textrm{t}\\overline{\\textrm{t}} $":"ttbar",
"J/\\ensuremath{\\psi}":"J/psi",
"$\\gamma\\gamma\\to WW$ and $\\gamma\\gamma\\to ZZ$":"gamma gamma to WW and gamma gamma to ZZ",
"$H \\to \\mathcal{A}\\mathcal{A} \\to  4\\gamma$":"H to AA to 4 gamma",
"$f_\\mathrm{s} / f_\\mathrm{u}$ and $f_\\mathrm{d} / f_ \\mathrm{u}$":"f_s / f_u and f_d / f_s",
"$\\sqrt{s}=13\\,\\text {Te}\\hspace{-.08em}\\text {V} $":"sqrt(s) = 13 TeV",
"sNN=8.16\\,\\,TeV":"sqrt(sNN) = 8.16 TeV",
"lepton~+~jets":"lepton+jets",
sNN=5.02TeV
$\sqrt{s} = 13\,\hbox {TeV}$
\ensuremath{\tau}
W$^{+}W^{−}$
\Upsilon{}(1S)
sNN = 8.16 TeV
sqrt(s)~=~13~TeV
$ {\Lambda}_{\textrm{c}}^{+} $
\ensuremath{\tau} \textrightarrow{} 3\ensuremath{\mu}
\ensuremath{\Lambda}(\ensuremath{\Lambda}‾)
 sNN=5.02TeV 
 s=13 TeV 
 \Upsilon{}(3S)
 \Upsilon{}
 $ \sqrt{\textrm{s}} $
 \ensuremath{\tau}
 J/psiJ/psi
 \ensuremath{\tau}
 H\textrightarrow{}bb\textasciimacron{}
 $ \textrm{t}\overline{\textrm{t}}\textrm{b}\overline{\textrm{b}} $
  sNN=5.02 TeV
  s=7 no tev
  8~TeV just the tilda)
$\sqrt{s} = 13~\text {TeV}$
\ensuremath{\tau}
\ensuremath{\alpha}S(mZ)
$ \sqrt{\textrm{s}} $
\ensuremath{\sqrt{}}$_{s}$
$\gamma\gamma\to\tau\tau$
\ensuremath{\Xi}b-\textrightarrow{}\ensuremath{\psi}(2S)\ensuremath{\Xi}-
\ensuremath{\Xi}b(5945)0
$ \textrm{b}\overline{\textrm{b}}{\textrm{W}}^{+}{\textrm{W}}^{-} $
B$^{\pm}$to K$^{\pm}\mu^+\mu^-$
B$^{\pm}$to K$^{\pm}$e$^+$e$^-$
${\text {Z}{}{}} {\text {Z}{}{}} $
${\text {Z}{}{}} {\text {H}{}{}} $
${\text {b}{}{}} {\bar{{\text {b}{}{}}}{}{}} {\text {b}{}{}} {\bar{{\text {b}{}{}}}{}{}} $
$\mu\mu$bb
J/psi\textrightarrow{}\ensuremath{\mu}+\ensuremath{\mu}-\ensuremath{\mu}+\ensuremath{\mu}-
$ \sqrt{\textrm{s}} $
# '':'',
# '':'',
# '':'',
# '':'',
}

# L799

# "(TOTEM Collaboration)\textdaggerdbl{}, (CMS Collaboration)\textdagger{}, TOTEM, CMS"

	to_remove=[]
	not_cms=[]
	accepted_year=[]

	for i,entry in enumerate(bib_db.entries):

		#remove double curly braces
		for key in entry:
			if entry[key][0]=='{' and entry[key][-1]=='}':
				bib_db.entries[i][key]=entry[key][1:-1]

		if 'author' in entry.keys():
			bib_db.entries[i]['author']=bib_db.entries[i]['author'].replace("\\'",'',100)

		for tsub in titlesub:
			bib_db.entries[i]['title']=bib_db.entries[i]['title'].replace(tsub,titlesub[tsub],100)

		if 'archiveprefix' in entry.keys():
			if entry['archiveprefix']=="arXiv":
				arxivid=entry['eprint']
				bib_db.entries[i]['url']="https://arxiv.org/pdf/"+arxivid+".pdf"
				# https://arxiv.org/pdf/2102.13080.pdf


		if 'collaboration' in entry.keys():
			if 'CMS' in entry['collaboration']:
				if "Tracker" in entry['collaboration']:
					not_cms.append(i)
				elif "ECAL" in entry['collaboration']:
					not_cms.append(i)
				elif "HCAL" in entry['collaboration']:
					not_cms.append(i)
				else:	
					bib_db.entries[i]['author']="CMS Collaboration, and Gleyzer, Sergei and Rumerio, Paolo and Usai, Emanuele"
				# author = "Collaboration, CMS and Usai, Emanuele and Gleyzer, Sergei",
			else:
				not_cms.append(i)
		else:
			not_cms.append(i)

		if "doi" in entry.keys():
			doi='https://doi.org/'+entry['doi']
			bib_db.entries[i]['doi']=doi

		if bib_db.entries[i]['year']!='2022' and bib_db.entries[i]['year']!='2023':
			accepted_year.append(i)

		if i not in not_published:
			bib_db.entries[i]['year']=pub_dates[i][0]
			if len(pub_dates[i])>2:
				bib_db.entries[i]['month']=month_dict[pub_dates[i][1]]
				bib_db.entries[i]['day']=pub_dates[i][2]
			else:
				bib_db.entries[i]['month']='unk'
				bib_db.entries[i]['day']='unk'
		else:
			bib_db.entries[i]['year']='2022'
			bib_db.entries[i]['month']='nov'
			bib_db.entries[i]['day']='01'


		# if pub_dates[i][0]!='2022' and pub_dates[i][0]!='2023':
		# 	to_remove.append(i) 

		# if pub_dates[i][0]!='2023':
		# 	to_remove.append(i) 


		#################################
		#################################
		#################################
		#SELECT ONLY ENTRIES AFTER SEPTEMBER
		# if pub_dates[i][0]!='2023':
		# 	to_remove.append(i) 
		# elif bib_db.entries[i]['month'] not in ['oct','nov','dec']:
		# 	to_remove.append(i) 
		#SELECT ONLY ENTRIES AFTER DEC
		if pub_dates[i][0]!='2024':
			to_remove.append(i) 


		if args.filename=='accepted':
			bib_db.entries[i]['journal']=journals[i] 


	# full_removal_list=list(set(not_published)|set(not_cms)|set(to_remove))
	# if args.filename=='accepted':
	# 	full_removal_list=list(set(not_cms)|set(accepted_year))
	# print(set(not_published))
	# print(set(not_cms))
	# print(set(to_remove))

	full_list=set(range(len(bib_db.entries)))
	# full_removal_list=set(not_published)|set(not_cms)|set(to_remove) ##do you want noncms?
	full_removal_list=set(not_published)|set(to_remove)

	if args.filename=='accepted':
		full_removal_list=set(not_cms)|set(accepted_year)
	# to save the removed ones only uncomment this
	if 'removed' in args.filename:
		full_removal_list=full_list - full_removal_list

	# if args.filename=='accepted':
	# 	full_removal_list=full_removal_list | set(accepted_year)
	# else:
	# 	full_removal_list=full_removal_list | set(to_remove)
	full_removal_list=list(full_removal_list)

	full_removal_list.sort(reverse=True)
	print(full_removal_list)

	# for i in not_cms:
	# 	not_cms_db.append(bib_db.entries[i])

	for i in full_removal_list:
		del bib_db.entries[i]

	# print(not_cms_db)
	print(bib_db.entries)


# https://doi.org/10.1103/PhysRevLett.126.252003
# "10.1103/PhysRevD.104.052001",
	

	# with open(args.filename.replace('.bib','')+'_parsed.bib', 'w') as bibtex_output_file:
	# 	bibtexparser.dump(bib_db, bibtex_output_file)
	with open(args.filename.replace('.bib','')+'_rtp24.bib', 'w') as bibtex_output_file:
		bibtexparser.dump(bib_db, bibtex_output_file)
