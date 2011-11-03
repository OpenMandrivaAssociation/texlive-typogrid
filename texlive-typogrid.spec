# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/typogrid
# catalog-date 2007-01-18 23:55:07 +0100
# catalog-license lppl
# catalog-version 0.10
Name:		texlive-typogrid
Version:	0.10
Release:	1
Summary:	Print a typographic grid
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/typogrid
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typogrid.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typogrid.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typogrid.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Draws a grid on every page of the document; the grid divides
the page into columns, and may be used for fixing measurements
of layout.

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
%{_texmfdistdir}/tex/latex/typogrid/typogrid.sty
%doc %{_texmfdistdir}/doc/latex/typogrid/README
%doc %{_texmfdistdir}/doc/latex/typogrid/testtypogrid.tex
%doc %{_texmfdistdir}/doc/latex/typogrid/typogrid.pdf
#- source
%doc %{_texmfdistdir}/source/latex/typogrid/Makefile
%doc %{_texmfdistdir}/source/latex/typogrid/typogrid.dtx
%doc %{_texmfdistdir}/source/latex/typogrid/typogrid.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
