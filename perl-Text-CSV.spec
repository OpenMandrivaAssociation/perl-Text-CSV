%define modname	Text-CSV

Summary:	Manipulate comma-separated value strings
Name:		perl-%{modname}
Version:	2.03
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Text/ISHIGAKI/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(Test::Harness)
BuildRequires:	perl(Test::More)

%description
Text::CSV provides facilities for the composition and decomposition of
comma-separated values using the Text::CSV_XS manpage or its pure Perl
version.

An instance of the Text::CSV class can combine fields into a CSV string and
parse a CSV string into fields.

The module accepts either strings or files as input and can utilize any
user-specified characters as delimiters, separators, and escapes so it is
perhaps better called ASV (anything separated values) rather than just CSV.

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
%make_build test

%install
%make_install

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*
