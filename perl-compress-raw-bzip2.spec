#
# spec file for package: perl-compress-raw-bzip2
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%define real_version 2.019

Name:		perl-compress-raw-bzip2
Version:	2.0.19
Summary:	Low-Level Interface to bzip2 compression library
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~pmqs/Compress-Raw-Bzip2-%{real_version}/lib/Compress/Raw/Bzip2.pm
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/Compress-Raw-Bzip2-%{real_version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWperl584core
Requires:	SUNWperl584core

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Paul Marquees <pmqs@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~pmqs/Compress-Raw-Bzip2-%{real_version}/lib/Compress/Raw/Bzip2.pm
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Compress::Raw::Bzip2 provides an interface to the in-memory
compression/uncompression functions from the bzip2 compression library.

%prep
%setup -q -n Compress-Raw-Bzip2-%{real_version}

%build
perl Makefile.PL PREFIX=%{_prefix} INSTALLSITEMAN3DIR=%{_mandir}/man3 DESTDIR=$RPM_BUILD_ROOT LIB=/usr/perl5/vendor_perl/5.8.4
make

%install
rm -rf $RPM_BUILD_ROOT
make pure_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%{_prefix}/perl5
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}

%changelog
* Mon Jun 01 2009 - jlee@thestaticvoid.com
- Initial version
* Fri Jun 12 2009 - jlee@thestaticvoid.com
- Separate zeros with dots in version number for IPS compatibility.
