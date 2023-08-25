Name:		python-chai
Version:	1.1.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/c/chai/chai-%{version}.tar.gz
Summary:	Easy to use mocking, stubbing and spying framework.
URL:		https://pypi.org/project/chai/
License:	LICENSE.txt
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Easy to use mocking, stubbing and spying framework.

%prep
%autosetup -p1 -n chai-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/chai
%{py_sitedir}/chai-*.*-info
