
%define realname   Text-CSV
%define version    1.11
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Manipulate comma-separated value strings
Source:     http://www.cpan.org/modules/by-module/Text/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(IO::Handle)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::More)

BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


