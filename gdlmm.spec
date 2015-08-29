#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	C++ bindings for gdl library
Summary(pl.UTF-8):	Wiązania C++ do biblioteki gdl
Name:		gdlmm
Version:	3.7.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gdlmm/3.7/%{name}-%{version}.tar.xz
# Source0-md5:	518623e187d8bbe4c40c1d0dc3663e05
URL:		https://github.com/GNOME/gdlmm
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gdl-devel >= 3.7
BuildRequires:	glibmm-devel >= 2.16.0
BuildRequires:	gtkmm3-devel >= 3.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	mm-common >= 0.8
BuildRequires:	pkgconfig
Requires:	gdl >= 3.7
Requires:	glibmm >= 2.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ bindings for gdl library.

%description -l pl.UTF-8
Wiązania C++ do biblioteki gdl.

%package devel
Summary:	Header files for gdlmm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gdlmm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gdl-devel >= 3.7
Requires:	glibmm-devel >= 2.16.0
Requires:	gtkmm3-devel >= 3.0.0

%description devel
Header files for gdlmm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gdlmm.

%package static
Summary:	Static gdlmm library
Summary(pl.UTF-8):	Statyczna biblioteka gdlmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gdlmm library.

%description static -l pl.UTF-8
Statyczna biblioteka gdlmm.

%package apidocs
Summary:	gdlmm API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki gdlmm
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API and internal documentation for gdlmm library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gdlmm.

%prep
%setup -q

%build
%configure \
	%{?with_static_libs:--enable-static} \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgdlmm-3.0.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgdlmm-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdlmm-3.0.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdlmm-3.0.so
%{_libdir}/gdlmm-3.0
%{_includedir}/gdlmm-3.0
%{_pkgconfigdir}/gdlmm-3.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgdlmm-3.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/gdlmm-3.0
%{_datadir}/devhelp/books/gdlmm-3.0
