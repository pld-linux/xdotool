%define		rel 20091231
Summary:	fake keyboard/mouse input
Name:		xdotool
Version:	0
Release:	0.%{rel}.1
License:	BSD-like
Group:		X11/Window Managers/Tools
Source0:	http://semicomplete.googlecode.com/files/%{name}-%{rel}.02.tar.gz
# Source0-md5:	faa6f616d33bdd9ec7fbc0d9542a6cc0
URL:		http://www.semicomplete.com/projects/xdotool/
BuildRequires:	perl-tools-pod
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdotool lets you programatically (or manually) simulate keyboard input
and mouse activity, move and resize windows, etc. It does this using
X11's XTEST extension and other Xlib functions.

%prep
%setup -q -n %{name}-%{rel}.02

%build
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

%files
%defattr(644,root,root,755)
%doc COPYRIGHT CHANGELIST README examples
%attr(755,root,root) %{_bindir}/xdotool
%attr(755,root,root) %{_libdir}/libxdo*
%{_mandir}/man1/xdotool.1*
%{_includedir}/xdo.h
