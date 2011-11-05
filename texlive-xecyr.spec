# revision 20221
# category Package
# catalog-ctan /macros/xetex/latex/xecyr
# catalog-date 2010-10-26 13:00:58 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-xecyr
Version:	1.1
Release:	1
Summary:	Using Cyrillic languages in XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/xecyr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xecyr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xecyr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Helper tools for using Cyrillic languages with XeLaTeX and
babel.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/xecyr/xu-ruenhyph.tex
%{_texmfdistdir}/tex/xelatex/xecyr/xecyr.sty
%doc %{_texmfdistdir}/doc/xelatex/xecyr/1251.tex
%doc %{_texmfdistdir}/doc/xelatex/xecyr/866.tex
%doc %{_texmfdistdir}/doc/xelatex/xecyr/NEWS
%doc %{_texmfdistdir}/doc/xelatex/xecyr/README
%doc %{_texmfdistdir}/doc/xelatex/xecyr/iso.tex
%doc %{_texmfdistdir}/doc/xelatex/xecyr/koi8-r.tex
%doc %{_texmfdistdir}/doc/xelatex/xecyr/language.dat.add
%doc %{_texmfdistdir}/doc/xelatex/xecyr/listings-utf8-ex.pdf
%doc %{_texmfdistdir}/doc/xelatex/xecyr/listings-utf8-ex.tex
%doc %{_texmfdistdir}/doc/xelatex/xecyr/pict2e-ex.pdf
%doc %{_texmfdistdir}/doc/xelatex/xecyr/pict2e-ex.tex
%doc %{_texmfdistdir}/doc/xelatex/xecyr/rubibtex-ex-x.pdf
%doc %{_texmfdistdir}/doc/xelatex/xecyr/rubibtex-ex-x.tex
%doc %{_texmfdistdir}/doc/xelatex/xecyr/rubibtex-ex.bib
%doc %{_texmfdistdir}/doc/xelatex/xecyr/rumakeindex-ex-x.pdf
%doc %{_texmfdistdir}/doc/xelatex/xecyr/rumakeindex-ex-x.tex
%doc %{_texmfdistdir}/doc/xelatex/xecyr/xecyr-doc-ru.pdf
%doc %{_texmfdistdir}/doc/xelatex/xecyr/xecyr-doc-ru.tex
%doc %{_texmfdistdir}/doc/xelatex/xecyr/xecyr-ex1-ru-x.pdf
%doc %{_texmfdistdir}/doc/xelatex/xecyr/xecyr-ex1-ru-x.tex
%doc %{_texmfdistdir}/doc/xelatex/xecyr/xecyr-ex2-ru-x.pdf
%doc %{_texmfdistdir}/doc/xelatex/xecyr/xecyr-ex2-ru-x.tex
%doc %{_texmfdistdir}/doc/xelatex/xecyr/xecyr-ex3-ru-x.pdf
%doc %{_texmfdistdir}/doc/xelatex/xecyr/xecyr-ex3-ru-x.tex
%doc %{_texmfdistdir}/doc/xelatex/xecyr/xecyr-ex4-ru-x.pdf
%doc %{_texmfdistdir}/doc/xelatex/xecyr/xecyr-ex4-ru-x.tex
%doc %{_texmfdistdir}/doc/xelatex/xecyr/xecyr-ex5-ru-x.pdf
%doc %{_texmfdistdir}/doc/xelatex/xecyr/xecyr-ex5-ru-x.tex
%doc %{_texmfdistdir}/doc/xelatex/xecyr/xecyr-ex6-ru-x.pdf
%doc %{_texmfdistdir}/doc/xelatex/xecyr/xecyr-ex6-ru-x.tex
%doc %{_texmfdistdir}/doc/xelatex/xecyr/xecyr-ex7-ru-x.pdf
%doc %{_texmfdistdir}/doc/xelatex/xecyr/xecyr-ex7-ru-x.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
