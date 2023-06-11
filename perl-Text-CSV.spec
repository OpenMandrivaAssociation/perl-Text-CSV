%define modname	Text-CSV
%define modver 1.21

Summary:	Manipulate comma-separated value strings
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Text/MIYAGAWA/%{modname}-%{modver}.tar.gz
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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*


