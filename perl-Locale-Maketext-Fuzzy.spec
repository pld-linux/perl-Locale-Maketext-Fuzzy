#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Locale
%define	pnam	Maketext-Fuzzy
Summary:	Locale::Maketext::Fuzzy - Maketext from already interpolated strings
Summary(pl):	Locale::Maketext::Fuzzy - Maketext z ju¿ przybli¿onych ³añcuchów
Name:		perl-Locale-Maketext-Fuzzy
Version:	0.02
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Locale-Maketext
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a subclass of Locale::Maketext, with additional support
for localizing messages that already contains interpolated variables.
This is most useful when the messages are returned by external modules
- for example, to match "dir: command not found" against "[_1]: command
not found".

%description -l pl
Ten modu³ jest podklas± Locale::Maketext, z dodatkow± obs³ug±
lokalizowanych komunikatów, które ju¿ zawieraj± przybli¿one warto¶ci.
Jest to najbardziej przydatne kiedy komunikaty s± zwracane przez
zewnêtrzne modu³y - na przyk³ad, aby dopasowaæ "dir: command not
found" do "[_1]: command not found".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Locale/Maketext/*.pm
%{_mandir}/man3/*
