Summary:	Free implementation of OpenAL's ALUT standard
Name:		freealut
Version:	1.1.0
Release:	13
License:	LGPL
Group:		Libraries
Source0:	http://connect.creativelabs.com/openal/Downloads/ALUT/%{name}-%{version}.tar.gz
# Source0-md5:	e089b28a0267faabdb6c079ee173664a
URL:		http://www.openal.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	openal-soft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free implementation of ALUT (OpenAL Utility Toolkit) standard.

%package devel
Summary:	Headers for freealut
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
freealut header files.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I admin/autotools/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libalut.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libalut.so.?

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/libalut.so
%{_libdir}/libalut.la
%{_includedir}/AL/*
%{_pkgconfigdir}/*

