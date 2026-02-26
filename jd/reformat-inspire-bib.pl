#!/usr/bin/perl


# Usage:  perl reformat-inspire-bib.pl <year> <infile> <outfile>
# Example:  perl reformat-inspire-bib.pl 2024 INSPIRE-Summary-Jay-2024.bib Watermark-Input-2024.bib 

# Created by Jay R. Dittmann, Baylor University (updated Jan 2025)

$pryear = $ARGV[0];
$oldfile = $ARGV[1];
$newfile = $ARGV[2];

open(OF, $oldfile);
open(NF, ">$newfile");

$tab = "\t";

%mydata = ();
$article = "";
# read in each line of the file
while ($line = <OF>) {
  chop($line);
    if ($line =~ /^(@)article/) { $article = $1 if $line =~ /\{(.*),/; }
    if ($article && $line =~ /^\}$/) { $article = ""; $key = "";}
    if ($article && $line =~ /^ +([a-z]*) *= (.*)/i) { $key = $1; $mydata{$article.$key} = $2; $mydata{$article."NAME"} = $article; }
    #if ($article && $line =~ /^                       (.*)/) { $mydata{$article.$key} .= $1; }
    #print("$article\n");
}

while ( my ($key, $value) = each(%mydata) ) {


    $bkey = $value if $key =~ /NAME/;
    
    if ($key =~ /.*title/) {
        $title = $value;
	#$title =~ s/\{\\sqrt\{\}\}$_\{s\}$/blubber/g;
	$title =~ s/\{\\sqrt\{\}\}\$_/\$\\sqrt/g;
	#$title =~ s/H\\textrightarrow{}bb\\textasciimacron{/H \\to b\\bbar/g;
        $title =~ s/..08em//g;
        $title =~ s/\\hbox//g;
        $title =~ s/\\hspace//g;
        $title =~ s/\\textrm//g;
        $title =~ s/\\ensuremath//g;
        $title =~ s/Run~2/Run 2/g;
        $title =~ s/Bs0/B^0_s/g;
	$title =~ s/\{\\alpha\}S/αₛ/g;
	$title =~ s/B\+/B^\+/g;
        $title =~ s/"//g;
        $title =~ s/,$//;
        $title =~ s/\\,//g;
        $title =~ s/\\;//g;
        $title =~ s/â//g;
	$title =~ s/\\'e/é/g;
        $title =~ s/\\smash.*\]//g;
        $title =~ s/\\textendash\{\}/–/g;
        $title =~ s/\\textquotedblright\{\}/"/g;
	$title =~ s/\\textrightarrow/\\to/g;
        $title =~ s/t\\textasciimacron\{\}/\\bart/g;
	$title =~ s/b\\textasciimacron\{\}/\\barb/g;
        $title =~ s/\\text//g;
        $title =~ s/_\{\\mathrm\{\}\}//g;
        $title =~ s/\^\{\\mathrm\{\}\}//g;
        $title =~ s/to\$/to \$/g;
        $title =~ s/\\mathrm//g;
        $title =~ s/\\rm//g;
        $title =~ s/\\overline/\\bar/g;
        $title =~ s/\\pm/±/g;
        $title =~ s/\\rightarrow/\\to/g;
        $title =~ s/\\to/→/g;  #longarrow ⟶
        $title =~ s/\\gamma/γ/g;
        $title =~ s/\\alpha/α/g;
        $title =~ s/\\rho/ρ/g;
        $title =~ s/\\phi/ϕ/g; #𝜙
        $title =~ s/\\psi/ψ/g;
        $title =~ s/\\pi/π/g; #𝜋
        $title =~ s/\\tau/τ/g;
        $title =~ s/\\ell/ℓ/g;
        $title =~ s/\\chi/χ/g;
        $title =~ s/\\eta/η/g;
        $title =~ s/\\theta/𝜽/g;
        $title =~ s/\\mu/µ/g;
        $title =~ s/\\nu/ν/g;
        $title =~ s/\\Lambda/Λ/g;
        $title =~ s/\\Upsilon/ϒ/g;
        $title =~ s/\\Xi/Ξ/g;
        $title =~ s/\\mathcal//g;
        while ($title =~ /\$([^\$]*)\$/) {
            $math = $1;
            $math =~ s/ //g;
            $title =~ s/\$([^\$]*)\$/$math/;
        }
        $title =~ s/\$//g;
        $title =~ s/\{//;
        $title =~ s/\(s\)/s/g;
        while ($title =~ s/\{(.)\}/\1/) {};
        while ($title =~ s/\{(..)\}/\1/) {};
        while ($title =~ s/\{(...)\}/\1/) {};
        while ($title =~ s/\{(....)\}/\1/) {};
        while ($title =~ s/\{(.....)\}/\1/) {};
        while ($title =~ s/\{(......)\}/\1/) {};
        while ($title =~ s/\{(.......)\}/\1/) {};
        while ($title =~ s/\{(........)\}/\1/) {};
        while ($title =~ s/\{(.........)\}/\1/) {};
        while ($title =~ s/\{(..........)\}/\1/) {};
        while ($title =~ s/\{(...........)\}/\1/) {};
        while ($title =~ s/\{(............)\}/\1/) {};
        $title =~ s/ +/ /g;
        $title =~ s/s....NN/sɴɴ/g;
        $title =~ s/s...NN/sɴɴ/g;
        $title =~ s/s..NN/sɴɴ/g;
        $title =~ s/s.NN/sɴɴ/g;
        $title =~ s/\\sqrts/√s/g;
        $title =~ s/sqrts/√s/g;
        $title =~ s/\\s_NN/√sɴɴ/g;
        $title =~ s/\\bart/t̄/g;
        $title =~ s/ +t-bar/t̄/g;
        $title =~ s/t-tbar/tt̄/g;
        $title =~ s/\\barp/p̄/g;
        $title =~ s/\\barb/b̄/g;
        $title =~ s/\\barD/D̄/g;  # D̄D̅
        $title =~ s/\\barν/ν̄/g;  # ν̄ν̅
        $title =~ s/\^0/⁰/g;
        #$title =~ s/\^\*/*/g;  #   * ٭
	$title =~ s/KS0/K⁰ₛ/g;
        $title =~ s/_s/ₛ/g;
        $title =~ s/_S/ₛ/g;
        $title =~ s/=/ = /g;
        $title =~ s/→/ → /g;
        $title =~ s/ +/ /g;  #⁺
        $title =~ s/\^\+/⁺/g;
        $title =~ s/\^\-/⁻/g;
	$title =~ s/\{//g;
        $title =~ s/\}//g;
        $title =~ s/(.eV)/ \1/;
        $title =~ s/ +/ /g;
        $title =~ s/proton.proton/proton-proton/g;
        $title =~ s/Proton.Proton/Proton-Proton/g;
        $title =~ s/~//g;
        $title =~ s/at s =/at √s =/g;
        $title =~ s/at sNN =/at √sɴɴ =/g;
	$title =~ s/ +/ /g;
	$title =~ s/ +/ /g;
	$title =~ s/Ξb- → ψ\(2S\)Ξ-/Ξb⁻ → ψ\(2S\)Ξ⁻/g;
	$title =~ s/\(5945\)0/\(5945\)⁰/g;
        $mydata{$key} = "\"{$title}\"";
    }  #q̄ ν̅ q̅ ₁ ₂
    
    if ($key =~ /.*author/) {
        $author = $value;
        if ($author =~ /Asres/) { $author = "\"\{Asres, M.W. et al.\} and Dittmann, J.\""; }
        if ($author =~ /Lee, Kyeongpil/) { $author = "\"\{Tonon, N. et al. (CMS Collaboration)\} and Brinkerhoff, A. and Dittmann, J. and Hatakeyama, K.\""; }
        if ($author =~ /Khachatryan/) { $author = "\"\{Khachatryan, V. et al. (CMS Collaboration)\} and Brinkerhoff, A. and Dittmann, J. and Hatakeyama, K.\""; }
        if ($author =~ /Sirunyan/) { $author = "\"\{Sirunyan, A.M. et al. (CMS Collaboration)\} and Brinkerhoff, A. and Dittmann, J. and Hatakeyama, K.\""; }
        if ($author =~ /Tumasyan/) { $author = "\"\{Tumasyan, A. et al. (CMS Collaboration)\} and Brinkerhoff, A. and Dittmann, J. and Hatakeyama, K.\""; }
        if ($author =~ /Hayrapetyan/) { $author = "\"\{Hayrapetyan, A. et al. (CMS Collaboration)\} and Brinkerhoff, A. and Dittmann, J. and Hatakeyama, K.\""; }
        if ($author =~ /Chatrchyan/) { $author = "\"\{Chatrchyan, S. et al. (CMS HCAL Collaboration)\} and Dittmann, J. and Hatakeyama, K.\""; }
        if ($author =~ /Acar/) { $author = "\"\{Acar, B. et al. (CMS HGCAL Collaboration)\} and Dittmann, J. and Hatakeyama, K.\""; }
        if ($author =~ /Aad/) { $author = "\"\{Aad, G. et al. (ATLAS & CMS Collaborations)\} and Brinkerhoff, A. and Dittmann, J. and Hatakeyama, K.\""; } #use & instead of and for DigitalMeasures
        if ($author =~ /Aaltonen/) { $author = "\"\{Aaltonen, T. et al. (CDF Collaboration)\} and Dittmann, J.R. and Hatakeyama, K.\""; }
        
        if ($key =~ /TOTEM/ and $author =~ /CMS Collaboration/) {
            $author =~ s/CMS Collaboration/TOTEM & CMS Collaborations/g;
        }
        
        $mydata{$key} = $author;
    }
    #𝑒𝑡 𝑎𝑙.
    
    if ($mydata{$bkey."journal"} =~ /Phys. Rev. Lett./) {
        $mydata{$bkey."journal"} = "\"Physical Review Letters\",";
    }

    if ($mydata{$bkey."doi"} =~ /PhysRevLett/) {
        $mydata{$bkey."journal"} = "\"Physical Review Letters\",";
    }

    if ($mydata{$bkey."volume"} =~ /C/ && $mydata{$bkey."journal"} =~ /Phys/) {
        $vol = $mydata{$bkey."volume"};
        $mydata{$bkey."journal"} = "\"Physical Review C\",";
        $mydata{$bkey."volume"} =~ s/C//;
    }
    
    if ($mydata{$bkey."doi"} =~ /PhysRevC/) {
        $mydata{$bkey."journal"} = "\"Physical Review C\",";
        $mydata{$bkey."volume"} =~ s/C//;
        $vol = $mydata{$bkey."volume"};
    }

    if ($mydata{$bkey."volume"} =~ /D/ && $mydata{$bkey."journal"} =~ /Phys/) {
        $vol = $mydata{$bkey."volume"};
        $mydata{$bkey."journal"} = "\"Physical Review D\",";
        $mydata{$bkey."volume"} =~ s/D//;
    }

    if ($mydata{$bkey."doi"} =~ /PhysRevD/) {
        $mydata{$bkey."journal"} = "\"Physical Review D\",";
        $mydata{$bkey."volume"} =~ s/D//;
        $vol = $mydata{$bkey."volume"};
    }

    
    if ($mydata{$bkey."volume"} =~ /B/ && $mydata{$bkey."journal"} =~ /Phys/) {
        $vol = $mydata{$bkey."volume"};
        $mydata{$bkey."journal"} = "\"Physics Letters Section B: Nuclear, Elementary Particle and High-Energy Physics\",";
        $mydata{$bkey."volume"} =~ s/B//;
    }

    if ($mydata{$bkey."doi"} =~ /j.physletb/) {
        $mydata{$bkey."journal"} = "\"Physics Letters Section B: Nuclear, Elementary Particle and High-Energy Physics\",";
        $mydata{$bkey."volume"} =~ s/B//;
        $vol = $mydata{$bkey."volume"};
    }

    if ($mydata{$bkey."journal"} =~ /JHEP/) {
        $mydata{$bkey."journal"} = "\"Journal of High Energy Physics\",";
    }

    if ($mydata{$bkey."journal"} =~ /Eur/) {
        $mydata{$bkey."journal"} = "\"European Physical Journal C. Particles and Fields\",";
    }
    
    if ($mydata{$bkey."journal"} =~ /JINST/) {
        $mydata{$bkey."journal"} = "\"Journal of Instrumentation\",";
    }

    if ($mydata{$bkey."journal"} =~ /Mach. Learn/) {
        $mydata{$bkey."journal"} = "\"Machine Learning: Science and Technology\",";
    }

    if ($mydata{$bkey."journal"} =~ /Comput. Softw/) {
        $mydata{$bkey."journal"} = "\"Computing and Software for Big Science\",";
    }

    if ($mydata{$bkey."journal"} =~ /Nucl. Instrum. Meth. A/) {
        $mydata{$bkey."journal"} = "\"Nuclear Instruments and Methods in Physics Research, Section A: Accelerators, Spectrometers, Detectors and Associated Equipment\",";
    }


}

foreach $key (sort keys %mydata) {
    if ($key =~ /NAME/) {
        $bkey = $mydata{$key};
        #print($bkey);


        if ($mydata{$bkey."year"} =~ $pryear) {   #if ($mydata{$bkey."note"} !~ /Erratum/) {
            print(NF "\@article\{$bkey,\n");
            $pr = $mydata{$bkey."author"};
            print(NF "      author         = $pr\n");
            $pr = $mydata{$bkey."title"};
            print(NF "      title          = $pr\n");
            $title = $pr;
            $pr = $mydata{$bkey."journal"};
            print(NF "      journal        = $pr\n");
            $pr = $mydata{$bkey."volume"};
            print(NF "      volume         = $pr\n");
            $pr = $mydata{$bkey."year"};
            print(NF "      year           = $pr\n");
            $pr = $mydata{$bkey."pages"};
            print(NF "      pages          = $pr\n");
            $pr = $mydata{$bkey."doi"};
            print(NF "      doi            = $pr\n");
            $pr = $mydata{$bkey."eprint"};
            print(NF "      arXiv          = $pr\n");
            $pr = $mydata{$bkey."archivePrefix"};
            print(NF "      archivePrefix  = $pr\n");
            $pr = $mydata{$bkey."primaryClass"};
            print(NF "      primaryClass   = $pr\n");
            $pr = $mydata{$bkey."reportNumber"};
            print(NF "      reportNumber   = $pr\n") if ($pr =~ /\w/);
            print(NF "\}\n\n");

            print("$title\n");
        }
    }
}
    
    
    
close(OF);
close(NF);
    
