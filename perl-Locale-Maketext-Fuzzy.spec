#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Locale
%define		pnam	Maketext-Fuzzy
Summary:	Locale::Maketext::Fuzzy - Maketext from already interpolated strings
Summary(pl.UTF-8):	Locale::Maketext::Fuzzy - Maketext z już przybliżonych łańcuchów
Name:		perl-Locale-Maketext-Fuzzy
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Locale/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	623d791f1b57c076e18e5090d0cb2aca
URL:		http://search.cpan.org/dist/Locale-Maketext-Fuzzy/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Locale-Maketext
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a subclass of Locale::Maketext, with additional support
for localizing messages that already contains interpolated variables.
This is most useful when the messages are returned by external modules
- for example, to match "dir: command not found" against "[_1]: command
not found".

%description -l pl.UTF-8
Ten moduł jest podklasą Locale::Maketext, z dodatkową obsługą
lokalizowanych komunikatów, które już zawierają przybliżone wartości.
Jest to najbardziej przydatne kiedy komunikaty są zwracane przez
zewnętrzne moduły - na przykład, aby dopasować "dir: command not
found" do "[_1]: command not found".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Locale/Maketext/*.pm
%{_mandir}/man3/*
