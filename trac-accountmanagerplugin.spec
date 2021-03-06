#
# spec file for package: trac-accountmanagerplugin
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc

%define python_version 2.6

Name:		trac-accountmanagerplugin
Version:	0.11
Summary:	Account Managment for Trac
License:	Attribution
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://trac-hacks.org/wiki/AccountManagerPlugin
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

# hosted in my webspace since upstream doesn't generate tarballs
Source0:	http://thestaticvoid.com/packages/AccountManagerPlugin-%{version}.tar.gz

%include default-depend.inc
BuildRequires:	SUNWpython26-setuptools
Requires:	SUNWpython26-setuptools
Requires:	trac

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            pacopablo <pacopablo@pacopablo.com>
Meta(info.upstream_url):        http://trac-hacks.org/wiki/AccountManagerPlugin
Meta(info.classification):	org.opensolaris.category.2008:Development/Python

%prep
%setup -q -n AccountManagerPlugin-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

# move to vendor-packages
if [ -d $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/site-packages ] ; then
	mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/vendor-packages
	mv $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/site-packages/* \
		$RPM_BUILD_ROOT%{_libdir}/python%{python_version}/vendor-packages/
	rmdir $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/site-packages
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%dir %{_libdir}
%dir %{_libdir}/python%{python_version}
%{_libdir}/python%{python_version}/vendor-packages/

%changelog
* Wed Jan 12 2011 - jlee@thestaticvoid.com
- Move to Python 2.6
* Sun May 31 2009 - jlee@thestaticvoid.com
- Add header
* Sun May 31 2009 - jlee@thestaticvoid.com
- Initial version
