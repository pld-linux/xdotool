%define		rel 20090612
Summary:	fake keyboard/mouse input
Name:		xdotool
Version:	0
Release:	0.%{rel}.1
License:	BSD-like
Group:		X11/Window Managers/Tools
Source0:	http://semicomplete.googlecode.com/files/%{name}-%{rel}.tar.gz
# Source0-md5:	78ff810202ed3ae74fd82ec741f889eb
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
%setup -q -n %{name}-%{rel}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}}

%{__make} install \
	INSTALLBIN=$RPM_BUILD_ROOT%{_bindir} \
	INSTALLMAN=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT CHANGELIST README examples
%attr(755,root,root) %{_bindir}/xdotool
%{_mandir}/man1/xdotool.1*
