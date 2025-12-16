Name:		python-chai
Version:	1.1.2
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/c/chai/chai-%{version}.tar.gz
Summary:	Easy to use mocking, stubbing and spying framework.
URL:		https://pypi.org/project/chai/
License:	LICENSE.txt
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Easy to use mocking, stubbing and spying framework.

%files
%{py_sitedir}/chai
%{py_sitedir}/chai-*.*-info
