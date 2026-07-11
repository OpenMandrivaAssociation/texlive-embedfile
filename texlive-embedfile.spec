%global tl_name embedfile
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.13
Release:	%{tl_revision}.1
Summary:	Embed files into PDF
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/embedfile
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/embedfile.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/embedfile.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/embedfile.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package embeds files in a PDF document, using the PDF format's
embedding operation (note the contrast with the attach operation used by
the attachfile and attachfile2 packages). Currently only pdfTeX >=1.30,
in PDF mode, is supported.

