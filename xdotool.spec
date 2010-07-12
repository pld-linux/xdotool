Summary:	fake keyboard/mouse input
Name:		xdotool
Version:	2.20100623.2949
Release:	1
License:	BSD-like
Group:		X11/Window Managers/Tools
Source0:	http://semicomplete.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	f717457e37e912642d422dacc4be7f83
URL:		http://www.semicomplete.com/projects/xdotool/
BuildRequires:	perl-tools-pod
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-proto-xextproto-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdotool lets you programatically (or manually) simulate keyboard input
and mouse activity, move and resize windows, etc. It does this using
X11's XTEST extension and other Xlib functions.

%package libs
Summary:	xdotool library
Summary(pl.UTF-8):	-
Group:		Libraries

%description libs
xdotool shared library.

%package devel
Summary:	Header files for xdotool library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki xdotool
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for xdotool library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki xdotool.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir},%{_mandir}}

%{__make} install \
	INSTALLBIN=$RPM_BUILD_ROOT%{_bindir} \
	INSTALLINCLUDE=$RPM_BUILD_ROOT%{_includedir} \
	INSTALLLIB=$RPM_BUILD_ROOT%{_libdir} \
	INSTALLMAN=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT CHANGELIST README examples
%attr(755,root,root) %{_bindir}/xdotool
%{_mandir}/man1/xdotool.1*

%files libs
%attr(755,root,root) %{_libdir}/libxdo.so.2

%files devel
%attr(755,root,root) %{_libdir}/libxdo.so
%{_includedir}/xdo.h
