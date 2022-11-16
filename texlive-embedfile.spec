Name:		texlive-embedfile
Version:	54865
Release:	1
Summary:	Embed files into PDF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/embedfile
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/embedfile.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/embedfile.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/embedfile.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package embeds files in a PDF document, using the PDF
format's embedding operation (note the contrast with the attach
operation used by the attachfile and attachfile2 packages).
Currently only pdfTeX >=1.30, in PDF mode, is supported.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/embedfile
%{_texmfdistdir}/tex/latex/embedfile
%{_texmfdistdir}/tex/generic/embedfile
%doc %{_texmfdistdir}/doc/latex/embedfile

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
