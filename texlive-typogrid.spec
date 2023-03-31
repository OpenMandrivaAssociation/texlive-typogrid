Name:		texlive-typogrid
Version:	24994
Release:	2
Summary:	Print a typographic grid
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/typogrid
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typogrid.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typogrid.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typogrid.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Draws a grid on every page of the document; the grid divides
the page into columns, and may be used for fixing measurements
of layout.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/typogrid/typogrid.sty
%doc %{_texmfdistdir}/doc/latex/typogrid/ChangeLog
%doc %{_texmfdistdir}/doc/latex/typogrid/Makefile
%doc %{_texmfdistdir}/doc/latex/typogrid/README
%doc %{_texmfdistdir}/doc/latex/typogrid/getversion.tex
%doc %{_texmfdistdir}/doc/latex/typogrid/testtypogrid.tex
%doc %{_texmfdistdir}/doc/latex/typogrid/typogrid.pdf
#- source
%doc %{_texmfdistdir}/source/latex/typogrid/typogrid.dtx
%doc %{_texmfdistdir}/source/latex/typogrid/typogrid.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
