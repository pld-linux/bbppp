Summary:	A ppp monitor tool designed for blackbox
Summary(pl):	Narzêdzie monitoruj±ce po³±czenia ppp zaprojektowane dla blackboksa
Name:		bbppp
Version:	0.2.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://bbtools.windsofstorm.net/sources/%{name}-%{version}.tar.gz
Patch0:		%{name}-sysconfdir.patch
URL:		http://bbtools.windsofstorm.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bbppp allows you to connect and disconnect (with user supplied
scripts) with dial-up. It monitors load, lights blinking leds and
counts time of connection. It is highly integrated with blackbox
window manager (can use it's theme settings), but can also work with
other WM.

%description -l pl
bbppp pozwala po³±czyæ i roz³±czyæ siê przez dial-up (u¿ywaj±c
skryptów u¿ytkownika). Mo¿e monitorowaæ przep³yw danych, zapala
mrugaj±ce "diodki" i liczy czas po³±czenia.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO data/README.*
%attr(755,root,root) %{_bindir}/bb*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bbtools/%{name}.*
