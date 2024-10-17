Name:		texlive-xecyr
Version:	54308
Release:	2
Summary:	Using Cyrillic languages in XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/xecyr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xecyr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xecyr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Helper tools for using Cyrillic languages with XeLaTeX and
babel.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/xecyr
%doc %{_texmfdistdir}/doc/xelatex/xecyr

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc tex %{buildroot}%{_texmfdistdir}/
