%define 	module	WebError
Summary:	Web Error handling and exception catching
Summary(pl.UTF-8):	-
Name:		python-%{module}
Version:	0.10.3
Release:	0.1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/W/WebError/%{module}-%{version}.tar.gz
# Source0-md5:	84b9990b0baae6fd440b1e60cdd06f9a
URL:		-
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#Requires:		python-libs
Requires:	python-modules
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web Error handling and exception catching.

%description -l pl.UTF-8

%prep
%setup -q -n %{module}-%{version}

%build
# CFLAGS is only for arch packages - remove on noarch packages
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%dir %{py_sitescriptdir}/weberror
%{py_sitescriptdir}/weberror/*.py[co]
%{py_sitescriptdir}/weberror/eval_template.html
%{py_sitescriptdir}/weberror/eval-media
%dir %{py_sitescriptdir}/weberror/exceptions
%{py_sitescriptdir}/weberror/exceptions/*.py[co]
%dir %{py_sitescriptdir}/weberror/util
%{py_sitescriptdir}/weberror/util/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
