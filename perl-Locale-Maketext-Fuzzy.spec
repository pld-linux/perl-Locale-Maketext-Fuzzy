#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Locale
%define	pnam	Maketext-Fuzzy
Summary:	Locale::Maketext::Fuzzy - Maketext from already interpolated strings
Summary(pl):	Locale::Maketext::Fuzzy - Maketext z ju¿ przybli¿onych ³añcuchów
Name:		perl-Locale-Maketext-Fuzzy
Version:	0.02
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0425610d448900a774ed253eb678c559
BuildRequires:	perl-devel >= 5.6
%if %{with tests}
BuildRequires:	perl-Locale-Maketext
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Locale/Maketext/*.pm
%{_mandir}/man3/*
