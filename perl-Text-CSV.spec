%define upstream_name    Text-CSV
%define upstream_version 1.21

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Manipulate comma-separated value strings
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(Test::Harness)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.210.0-4mdv2012.0
+ Revision: 765755
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.210.0-3
+ Revision: 764260
- rebuilt for perl-5.14.x

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.210.0-2
+ Revision: 656974
- rebuild for updated spec-helper

* Wed Dec 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.210.0-1mdv2011.0
+ Revision: 625959
- update to new version 1.21

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.200.0-1mdv2011.0
+ Revision: 596041
- update to new version 1.20

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.180.0-1mdv2011.0
+ Revision: 552661
- update to 1.18

* Wed Mar 17 2010 Jérôme Quelin <jquelin@mandriva.org> 1.170.0-1mdv2010.1
+ Revision: 523441
- update to 1.17

* Wed Dec 09 2009 Jérôme Quelin <jquelin@mandriva.org> 1.160.0-1mdv2010.1
+ Revision: 475397
- update to 1.16

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.150.0-1mdv2010.1
+ Revision: 460774
- update to 1.15

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.130.0-2mdv2010.0
+ Revision: 408652
- force rebuild
- update to 1.13

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-1mdv2010.0
+ Revision: 401517
- rebuild using %%perl_convert_version
- fixed license field

* Sun May 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.12-1mdv2010.0
+ Revision: 376567
- update to new version 1.12

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.11-2mdv2010.0
+ Revision: 375891
- rebuild

* Sat Apr 11 2009 Olivier Thauvin <nanardon@mandriva.org> 1.11-1mdv2009.1
+ Revision: 366288
- import perl-Text-CSV


* Sat Apr 11 2009 cpan2dist 1.11-1mdv
- initial mdv release, generated with cpan2dist

