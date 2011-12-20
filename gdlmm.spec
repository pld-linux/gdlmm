Summary:	C++ bindings for gdl library
Summary(pl.UTF-8):	Wiązania C++ do biblioteko gdl
Name:		gdlmm
Version:	3.2.1
Release:	3
License:	LGPL v2.1
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gdlmm/3.2/%{name}-%{version}.tar.xz
# Source0-md5:	d07999618fcec79a2287bb23d01fc4d2
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	gdl-devel >= 3.0.0
BuildRequires:	glibmm-devel >= 2.16.0
BuildRequires:	gtkmm3-devel >= 3.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ bindings for gdl library.

%description -l pl.UTF-8
Wiązania C++ do biblioteki gdl..

%package devel
Summary:	Header files for gdlmm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gdlmm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gdl-devel >= 3.0.0
Requires:	glibmm-devel >= 2.12.8
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

%description apidocs
API and internal documentation for gdlmm library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gdlmm.

%prep
%setup -q

%build
%configure \
	--enable-static \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgdlmm-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdlmm-3.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdlmm-3.0.so
%{_libdir}/gdlmm-3.0
%{_libdir}/libgdlmm-3.0.la
%{_includedir}/gdlmm-3.0
%{_pkgconfigdir}/gdlmm-3.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdlmm-3.0.a

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/gdlmm-3.0
%{_datadir}/devhelp/books/gdlmm-3.0
