%define		fversion	%(echo %{version} |tr r -)
%define		modulename	withr
%undefine	_debugsource_packages
Summary:	Run code with temporarily modified global state
Name:		R-cran-%{modulename}
Version:	3.0.2
Release:	2
License:	MIT
Group:		Applications/Math
Source0:	https://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	f2e3780a71f6258d6f9055f138d474f2
URL:		https://cran.r-project.org/package=%{modulename}
BuildRequires:	R

Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Run code with temporarily modified global state.

%prep
%setup -q -c

%build
R CMD build --no-build-vignettes %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
