#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

Summary:	Python 2 bindings for NSS and NSPR
Summary(pl.UTF-8):	Wiązania Pythona 2 do bibliotek NSS i NSPR
Name:		python-nss
Version:	1.0.0
Release:	2
License:	MPL v2.0 or GPL v2+ or LGPL v2+
Group:		Development/Languages/Python
Source0:	http://ftp.mozilla.org/pub/security/python-nss/releases/PYNSS_RELEASE_1_0_0/src/%{name}-%{version}.tar.bz2
# Source0-md5:	2159793d207f8d1f15556fd7fcfddc48
URL:		http://www.mozilla.org/projects/security/pki/nss/
BuildRequires:	nspr-devel >= 4
BuildRequires:	nss-devel >= 3
%{?with_python2:BuildRequires:	python-devel >= 1:2.7}
%{?with_python3:BuildRequires:	python3-devel >= 1:3.2}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-libs >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 bindings for Network Security Services (NSS) and Netscape
Portable Runtime (NSPR).

%description -l pl.UTF-8
Wiązania Pythona 2 do bibliotek NSS (Network Security Services) oraz
NSPR (Netscape Portable Runtime).

%package -n python3-nss
Summary:	Python 3 bindings for NSS and NSPR
Summary(pl.UTF-8):	Wiązania Pythona 3 do bibliotek NSS i NSPR
Group:		Development/Languages/Python
Requires:	python3-libs >= 1:3.2

%description -n python3-nss
Python 3 bindings for Network Security Services (NSS) and Netscape
Portable Runtime (NSPR).

%description -n python3-nss -l pl.UTF-8
Wiązania Pythona 3 do bibliotek NSS (Network Security Services) oraz
NSPR (Netscape Portable Runtime).

%prep
%setup -q

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README doc/ChangeLog
%dir %{py_sitedir}/nss
%{py_sitedir}/nss/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/nss/error.so
%attr(755,root,root) %{py_sitedir}/nss/io.so
%attr(755,root,root) %{py_sitedir}/nss/nss.so
%attr(755,root,root) %{py_sitedir}/nss/ssl.so
%{py_sitedir}/python_nss-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-nss
%defattr(644,root,root,755)
%doc README doc/ChangeLog
%dir %{py3_sitedir}/nss
%{py3_sitedir}/nss/__init__.py
%{py3_sitedir}/nss/__pycache__
%attr(755,root,root) %{py3_sitedir}/nss/error.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/nss/io.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/nss/nss.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/nss/ssl.cpython-*.so
%{py3_sitedir}/python_nss-%{version}-py*.egg-info
%endif
