Summary:	A ppp monitor tool designed for blackbox
Summary(pl):	Narzêdzie minotoruj±ce ppp zaprojektowane dla blackboksa
Name:		bbppp
Version:	0.2.2
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://bbtools.windsofstorm.net/sources/%{name}-%{version}.tar.gz
Patch0:		%{name}-sysconfdir.patch
URL:		http://bbtools.windsofstorm.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
bbppp allows you to connect and disconnect (with user supplied
scripts) with dial-up. It monitors load, ligths blinking leds and
counts time of connection. It is highly integrated with blackbox
window manager (can use it's theme settings), but can work also with
other WM.

%description -l pl
bbppp pozawala po³±czyæ i roz³±czyæ siê przez dial-up (u¿ywaj±c
skryptów u¿ytkownika). Mo¿e monitorowaæ przep³yw danych, zapala
mrygaj±ce "diodki" i liczy czas po³±czenia.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure
%{__make} CXX="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog README TODO data/README.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz data/*.gz
%attr(755,root,root) %{_bindir}/bb*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bbtools/%{name}.*
