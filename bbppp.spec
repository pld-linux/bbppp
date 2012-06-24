Summary:	A ppp monitor tool designed for blackbox
Summary(pl):	Narz�dzie monitoruj�ce po��czenia ppp zaprojektowane dla blackboksa
Name:		bbppp
Version:	0.2.3
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://bbtools.windsofstorm.net/sources/%{name}-%{version}.tar.gz
# Source0-md5:	c28c66ec68acc3fa32f3578b02b49b61
Patch0:		%{name}-sysconfdir.patch
Patch1:		%{name}-gcc33.patch
URL:		http://bbtools.windsofstorm.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
# whatever package it would belong to
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bbppp allows you to connect and disconnect (with user supplied
scripts) with dial-up. It monitors load, lights blinking leds and
counts time of connection. It is highly integrated with blackbox
window manager (can use it's theme settings), but can also work with
other WM.

%description -l pl
bbppp pozwala po��czy� i roz��czy� si� przez dial-up (u�ywaj�c
skrypt�w u�ytkownika). Mo�e monitorowa� przep�yw danych, zapala
mrugaj�ce "diodki" i liczy czas po��czenia.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO data/README.*
%attr(755,root,root) %{_bindir}/bb*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bbtools/%{name}.*
