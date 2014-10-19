Summary:	Python bindings for NSS and NSPR
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek NSS i NSPR
Name:		python-nss
Version:	0.15.0
Release:	1
License:	MPL v1.1 or GPL v2+ or LGPL v2+
Group:		Development/Languages/Python
Source0:	http://ftp.mozilla.org/pub/mozilla.org/security/python-nss/releases/PYNSS_RELEASE_0_15_0/src/%{name}-%{version}.tar.bz2
# Source0-md5:	e0287a67ac99d490dd4bb6c87acdae28
URL:		http://www.mozilla.org/projects/security/pki/nss/
BuildRequires:	nspr-devel >= 4
BuildRequires:	nss-devel >= 3
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Network Security Services (NSS) and Netscape
Portable Runtime (NSPR).

%description -l pl.UTF-8
Wiązania Pythona do bibliotek NSS (Network Security Services) oraz
NSPR (Netscape Portable Runtime).

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitedir}/nss
%{py_sitedir}/nss/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/nss/error.so
%attr(755,root,root) %{py_sitedir}/nss/io.so
%attr(755,root,root) %{py_sitedir}/nss/nss.so
%attr(755,root,root) %{py_sitedir}/nss/ssl.so
%{py_sitedir}/python_nss-%{version}-py*.egg-info
