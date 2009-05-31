%include Solaris.inc

%define python_version 2.4

Name:		Genshi
Version:	0.5.1
Summary:	Python toolkit for generation of output for the web
License:	BSD
Group:		Development/Python
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://genshi.edgewall.org/
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright

Source0:	ftp://ftp.edgewall.org/pub/genshi/%{name}-%{version}.tar.bz2

%include default-depend.inc
BuildRequires:	SUNWpython-setuptools
Requires:	SUNWpython-setuptools

Meta(info.maintainer):          James Lee <jlee@thestaticvoid.com>
Meta(info.upstream):            Edgewall Software <trac-dev@googlegroups.com>
Meta(info.upstream_url):        http://trac.edgewall.org/

%description
Genshi is a Python library that provides an integrated set of components for
parsing, generating, and processing HTML, XML or other textual content for
output generation on the web. 

%prep
%setup -q

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
%dir %{_libdir}/python%{python_version}/vendor-packages
%{_libdir}/python%{python_version}/vendor-packages/genshi
%{_libdir}/python%{python_version}/vendor-packages/Genshi-0.5.1-py%{python_version}.egg-info

%changelog
* Fri May 30 2009 - jlee@thestaticvoid.com
- Initial version
