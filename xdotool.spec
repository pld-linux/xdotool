Summary:	fake keyboard/mouse input
Name:		xdotool
Version:	3.20211022.1
Release:	1
License:	BSD-like
Group:		X11/Window Managers/Tools
Source0:	https://github.com/jordansissel/xdotool/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9fd993a251a7c38b32381503544b0dd7
URL:		http://www.semicomplete.com/projects/xdotool/
BuildRequires:	perl-tools-pod
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdotool lets you programatically (or manually) simulate keyboard input
and mouse activity, move and resize windows, etc. It does this using
X11's XTEST extension and other Xlib functions.

%package libs
Summary:	libxdo library
Group:		Libraries

%description libs
shared libxdo library.

%package devel
Summary:	Header files for libxdo library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxdo
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for libxdo library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libxdo.

%prep
%setup -q

sed -i -e 's#^libdir=.*#libdir=%{_libdir}#' \
	-e 's#^includedir=.*#includedir=%{_includedir}#' \
	libxdo.pc

%build
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir},%{_mandir}}

%{__make} install \
	PREFIX=%{_prefix} \
	INSTALLLIB=%{_libdir} \
	INSTALLMAN=%{_mandir} \
	LDCONFIG=/bin/true \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT CHANGELIST README.md examples
%attr(755,root,root) %{_bindir}/xdotool
%{_mandir}/man1/xdotool.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxdo.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxdo.so
%{_includedir}/xdo.h
%{_pkgconfigdir}/libxdo.pc
