#
# spec file for package: spamassassin
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

Name:		spamassassin
Version:	3.2.5
Summary:	Spam Filter
License:	Apache-2.0
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://spamassassin.apache.org/
SUNW_Basedir:	/
SUNW_Copyright: %{name}.copyright

Source0:	http://download.filehat.com/apache/spamassassin/source/Mail-SpamAssassin-%{version}.tar.bz2
Source1:	spamd.xml

%include default-depend.inc
BuildRequires:	SUNWperl584core
BuildRequires:	SUNWperl584usr
BuildRequires:	SUNWopenssl-include
BuildRequires:	SUNWopenssl-libraries
BuildRequires:	perl-digest-sha1
BuildRequires:	perl-html-parser
BuildRequires:	perl-net-dns
BuildRequires:	perl-lwp
BuildRequires:	perl-io-zlib
BuildRequires:	perl-archive-tar
BuildRequires:	perl-dbfile
BuildRequires:	perl-mail-spf
BuildRequires:	perl-io-socket-ssl
Requires:	SUNWperl584core
Requires:	SUNWopenssl-libraries
Requires:	perl-digest-sha1
Requires:	perl-html-parser
Requires:	perl-net-dns
Requires:	perl-lwp
Requires:	perl-io-zlib
Requires:	perl-archive-tar
Requires:	perl-dbfile
Requires:	perl-mail-spf
Requires:	perl-io-socket-ssl

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Apache.org <users@spamassassin.apache.org>
Meta(info.upstream_url):        http://spamassassin.apache.org/
Meta(info.classification):	org.opensolaris.category.2008:System/Security

%description
SpamAssassin is a mail filter which attempts to identify spam using
a variety of mechanisms including text analysis, Bayesian filtering,
DNS blocklists, and collaborative filtering databases.

%prep
%setup -q -n Mail-SpamAssassin-%{version}

%build
PERL_MM_USE_DEFAULT=1 perl Makefile.PL PREFIX=%{_prefix} INSTALLSITEMAN1DIR=%{_mandir}/man1 INSTALLSITEMAN3DIR=%{_mandir}/man3 DESTDIR=$RPM_BUILD_ROOT LIB=/usr/perl5/vendor_perl/5.8.4 ENABLE_SSL="yes"
make

%install
rm -rf $RPM_BUILD_ROOT
make install
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/network
cp %{SOURCE1} $RPM_BUILD_ROOT%{_localstatedir}/svc/manifest/network/spamd.xml

%clean
rm -rf $RPM_BUILD_ROOT

%if %(test -f /usr/sadm/install/scripts/i.manifest && echo 0 || echo 1)
%iclass manifest -f i.manifest
%endif

%files
%defattr(-,root,bin)
%{_bindir}
%{_prefix}/perl5
%attr(755,root,sys) %dir %{_datadir}
%{_datadir}/spamassassin
%{_mandir}
%defattr(-,root,sys)
%{_sysconfdir}
%class(manifest) %attr(444,root,sys) %{_localstatedir}/svc/manifest/network/spamd.xml

%changelog
* Mon Jun 01 2009 - jlee@thestaticvoid.com
- Initial version
