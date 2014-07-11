# revision 24994
# category Package
# catalog-ctan /macros/latex/contrib/typogrid
# catalog-date 2012-01-01 15:10:03 +0100
# catalog-license lppl
# catalog-version 0.21
Name:		texlive-typogrid
Version:	0.21
Release:	7
Summary:	Print a typographic grid
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/typogrid
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typogrid.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typogrid.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typogrid.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.21-1
+ Revision: 759070
- Update to latest upstream release

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.10-2
+ Revision: 757168
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.10-1
+ Revision: 719827
- texlive-typogrid
- texlive-typogrid
- texlive-typogrid

