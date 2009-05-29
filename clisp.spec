%include Solaris.inc
%define gcc_picflags
%define _cc %(echo $CC)
%ifarch amd64 sparcv9
%include arch64.inc
%define cc %{_cc} -m64
%define confargs --disable-mmap
%use clisp_64 = clisp-base.spec
%endif
%include base.inc
%define cc %{_cc}
%define confargs
%use clisp = clisp-base.spec

Name:		clisp
Version:	%{clisp.version}
Release:	1
Summary:	A Common Lisp Implementation
License:	GPL
Group:		Development/Other Languages
Packager:       James Lee <jlee@thestaticvoid.org>
Vendor:		http://ftp.gnu.org/pub/gnu/%{name}/release/%{version}/%{name}-%{version}.tar.bz2
Url:		http://www.gnu.org/software/clisp/
SUNW_Hotline:   %{url}
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright:	%{name}.copyright
SUNW_Category:	application

%include default-depend.inc
BuildRequires:	libsigsegv-devel
BuildRequires:	libffcall-devel
BuildRequires:	readline-devel
Requires:	libsigsegv
Requires:	libffcall
Requires:	readline

%description
ANSI Common Lisp is a high-level, general-purpose programming language. GNU
CLISP is a Common Lisp implementation by Bruno Haible of Karlsruhe University
and Michael Stoll of Munich University, both in Germany. It mostly supports the
Lisp described in the ANSI Common Lisp standard. It runs on most Unix
workstations (GNU/Linux, FreeBSD, NetBSD, OpenBSD, Solaris, Tru64, HP-UX, BeOS,
NeXTstep, IRIX, AIX and others) and on other systems (Windows NT/2000/XP,
Windows 95/98/ME) and needs only 4 MB of RAM. 

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
%ifarch amd64 sparcv9
mkdir %{name}-%{version}/%{_arch64}
%clisp_64.prep -d %{name}-%{version}/%{_arch64}
%endif
mkdir %{name}-%{version}/%{base_arch}
%clisp.prep -d %{name}-%{version}/%{base_arch}

%build
%ifarch amd64 sparcv9
%clisp_64.build -d %{name}-%{version}/%{_arch64}
%endif
%clisp.build -d %{name}-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%clisp_64.install -d %{name}-%{version}/%{_arch64}
%endif
%clisp.install -d %{name}-%{version}/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/clisp $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir}
ln -s ../lib/isaexec clisp
%endif

mv $RPM_BUILD_ROOT%{_datadir}/doc $RPM_BUILD_ROOT%{_datadir}/foo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc
mv $RPM_BUILD_ROOT%{_datadir}/foo $RPM_BUILD_ROOT%{_datadir}/doc/clisp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/clisp
%{_libdir}/%{_arch64}/clisp-%{version}/full/gettext.o
%{_libdir}/%{_arch64}/clisp-%{version}/full/calls.o
%{_libdir}/%{_arch64}/clisp-%{version}/full/lisp.run
%{_libdir}/%{_arch64}/clisp-%{version}/full/regexp.dvi
%{_libdir}/%{_arch64}/clisp-%{version}/full/localcharset.o
%{_libdir}/%{_arch64}/clisp-%{version}/full/libnoreadline.a
%{_libdir}/%{_arch64}/clisp-%{version}/full/width.o
%{_libdir}/%{_arch64}/clisp-%{version}/full/lispinit.mem
%{_libdir}/%{_arch64}/clisp-%{version}/full/uniname.o
%{_libdir}/%{_arch64}/clisp-%{version}/full/readline.o
%{_libdir}/%{_arch64}/clisp-%{version}/full/regexi.o
%{_libdir}/%{_arch64}/clisp-%{version}/full/regex.o
%{_libdir}/%{_arch64}/clisp-%{version}/full/modules.h
%{_libdir}/%{_arch64}/clisp-%{version}/full/lisp.a
%{_libdir}/%{_arch64}/clisp-%{version}/full/makevars
%{_libdir}/%{_arch64}/clisp-%{version}/full/modules.o
%{_libdir}/%{_arch64}/clisp-%{version}/linkkit/modprep.lisp
%{_libdir}/%{_arch64}/clisp-%{version}/linkkit/clisp.h
%{_libdir}/%{_arch64}/clisp-%{version}/linkkit/modules.c
%{_libdir}/%{_arch64}/clisp-%{version}/data/Symbol-Table.text
%{_libdir}/%{_arch64}/clisp-%{version}/data/UnicodeDataFull.txt
%{_libdir}/%{_arch64}/clisp-%{version}/base/regexp.dvi
%{_libdir}/%{_arch64}/clisp-%{version}/base/calls.o
%{_libdir}/%{_arch64}/clisp-%{version}/base/localcharset.o
%{_libdir}/%{_arch64}/clisp-%{version}/base/gettext.o
%{_libdir}/%{_arch64}/clisp-%{version}/base/width.o
%{_libdir}/%{_arch64}/clisp-%{version}/base/lisp.run
%{_libdir}/%{_arch64}/clisp-%{version}/base/lispinit.mem
%{_libdir}/%{_arch64}/clisp-%{version}/base/regexi.o
%{_libdir}/%{_arch64}/clisp-%{version}/base/uniname.o
%{_libdir}/%{_arch64}/clisp-%{version}/base/libnoreadline.a
%{_libdir}/%{_arch64}/clisp-%{version}/base/modules.h
%{_libdir}/%{_arch64}/clisp-%{version}/base/readline.o
%{_libdir}/%{_arch64}/clisp-%{version}/base/regex.o
%{_libdir}/%{_arch64}/clisp-%{version}/base/makevars
%{_libdir}/%{_arch64}/clisp-%{version}/base/lisp.a
%{_libdir}/%{_arch64}/clisp-%{version}/base/modules.o
%{_libdir}/%{_arch64}/clisp-%{version}/clisp-link
%endif
%if %can_isaexec
%{_bindir}/%{base_isa}/clisp
%hard %{_bindir}/clisp
%else
%{_bindir}/clisp
%endif
%{_libdir}/clisp-%{version}/linkkit/clisp.h
%{_libdir}/clisp-%{version}/linkkit/modules.c
%{_libdir}/clisp-%{version}/linkkit/modprep.lisp
%{_libdir}/clisp-%{version}/clisp-link
%{_libdir}/clisp-%{version}/full/lisp.run
%{_libdir}/clisp-%{version}/full/calls.o
%{_libdir}/clisp-%{version}/full/localcharset.o
%{_libdir}/clisp-%{version}/full/regexp.dvi
%{_libdir}/clisp-%{version}/full/gettext.o
%{_libdir}/clisp-%{version}/full/width.o
%{_libdir}/clisp-%{version}/full/readline.o
%{_libdir}/clisp-%{version}/full/regex.o
%{_libdir}/clisp-%{version}/full/regexi.o
%{_libdir}/clisp-%{version}/full/modules.o
%{_libdir}/clisp-%{version}/full/modules.h
%{_libdir}/clisp-%{version}/full/libnoreadline.a
%{_libdir}/clisp-%{version}/full/lispinit.mem
%{_libdir}/clisp-%{version}/full/uniname.o
%{_libdir}/clisp-%{version}/full/makevars
%{_libdir}/clisp-%{version}/full/lisp.a
%{_libdir}/clisp-%{version}/base/gettext.o
%{_libdir}/clisp-%{version}/base/libnoreadline.a
%{_libdir}/clisp-%{version}/base/lispinit.mem
%{_libdir}/clisp-%{version}/base/lisp.run
%{_libdir}/clisp-%{version}/base/readline.o
%{_libdir}/clisp-%{version}/base/regex.o
%{_libdir}/clisp-%{version}/base/makevars
%{_libdir}/clisp-%{version}/base/width.o
%{_libdir}/clisp-%{version}/base/uniname.o
%{_libdir}/clisp-%{version}/base/lisp.a
%{_libdir}/clisp-%{version}/base/calls.o
%{_libdir}/clisp-%{version}/base/regexp.dvi
%{_libdir}/clisp-%{version}/base/localcharset.o
%{_libdir}/clisp-%{version}/base/modules.o
%{_libdir}/clisp-%{version}/base/modules.h
%{_libdir}/clisp-%{version}/base/regexi.o
%{_libdir}/clisp-%{version}/data/UnicodeDataFull.txt
%{_libdir}/clisp-%{version}/data/Symbol-Table.text
%attr(755,root,sys) %dir %{_datadir}
%attr(755,root,other) %dir %{_datadir}/locale
%attr(755,root,other) %dir %{_datadir}/locale/de
%attr(755,root,other) %dir %{_datadir}/locale/de/LC_MESSAGES
%attr(755,root,other) %dir %{_datadir}/locale/ru
%attr(755,root,other) %dir %{_datadir}/locale/ru/LC_MESSAGES
%attr(755,root,other) %dir %{_datadir}/locale/da
%attr(755,root,other) %dir %{_datadir}/locale/da/LC_MESSAGES
%attr(755,root,other) %dir %{_datadir}/locale/es
%attr(755,root,other) %dir %{_datadir}/locale/es/LC_MESSAGES
%attr(755,root,other) %dir %{_datadir}/locale/en
%attr(755,root,other) %dir %{_datadir}/locale/en/LC_MESSAGES
%attr(755,root,other) %dir %{_datadir}/locale/fr
%attr(755,root,other) %dir %{_datadir}/locale/fr/LC_MESSAGES
%attr(755,root,other) %dir %{_datadir}/locale/nl
%attr(755,root,other) %dir %{_datadir}/locale/nl/LC_MESSAGES
%{_datadir}/locale/de/LC_MESSAGES/clisp.mo
%{_datadir}/locale/de/LC_MESSAGES/clisplow.mo
%{_datadir}/locale/ru/LC_MESSAGES/clisplow.mo
%{_datadir}/locale/ru/LC_MESSAGES/clisp.mo
%{_datadir}/locale/da/LC_MESSAGES/clisplow.mo
%{_datadir}/locale/da/LC_MESSAGES/clisp.mo
%{_datadir}/locale/es/LC_MESSAGES/clisplow.mo
%{_datadir}/locale/es/LC_MESSAGES/clisp.mo
%{_datadir}/locale/en/LC_MESSAGES/clisplow.mo
%{_datadir}/locale/en/LC_MESSAGES/clisp.mo
%{_datadir}/locale/fr/LC_MESSAGES/clisp.mo
%{_datadir}/locale/fr/LC_MESSAGES/clisplow.mo
%{_datadir}/locale/nl/LC_MESSAGES/clisplow.mo
%{_datadir}/locale/nl/LC_MESSAGES/clisp.mo
%{_datadir}/emacs/site-lisp/clisp-indent.lisp
%{_datadir}/emacs/site-lisp/clisp-ffi.el
%{_datadir}/emacs/site-lisp/clhs.el
%{_datadir}/emacs/site-lisp/clisp-indent.el
%{_datadir}/emacs/site-lisp/clisp-coding.el
%{_datadir}/vim/vimfiles/after/syntax/lisp.vim
%attr(755,root,other) %dir %{_datadir}/doc
%{_datadir}/doc/clisp/GNU-GPL
%{_datadir}/doc/clisp/README.de
%{_datadir}/doc/clisp/clisp.html
%{_datadir}/doc/clisp/NEWS
%{_datadir}/doc/clisp/COPYRIGHT
%{_datadir}/doc/clisp/SUMMARY
%{_datadir}/doc/clisp/README.es
%{_datadir}/doc/clisp/MAGIC.add
%{_datadir}/doc/clisp/README
%{_datadir}/doc/clisp/ANNOUNCE
%{_datadir}/doc/clisp/doc/editors.txt
%{_datadir}/doc/clisp/doc/CLOS-guide.txt
%{_datadir}/doc/clisp/doc/clisp.png
%{_datadir}/doc/clisp/doc/clisp.html
%{_datadir}/doc/clisp/doc/clisp.1
%{_datadir}/doc/clisp/doc/LISP-tutorial.txt
%{_datadir}/doc/clisp/doc/impnotes.html
%{_datadir}/doc/clisp/doc/impnotes.css
%{_mandir}/man1/clisp.1