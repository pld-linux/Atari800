Summary:	Atari 800 Emulator
Summary(pl.UTF-8):	Emulator Atari 800
Name:		Atari800
Version:	5.2.0
Release:	1
License:	GPL v2+
Group:		Applications/Emulators
#Source0Download: https://github.com/atari800/atari800/releases
Source0:	https://github.com/atari800/atari800/releases/download/ATARI800_5_2_0/atari800-%{version}-src.tgz
# Source0-md5:	bed6188abbe73c2ac109dc954050fd46
Source1:	%{name}-chooser
Patch0:		%{name}-romdir.patch
Patch1:		%{name}-nodisk.patch
URL:		https://atari800.github.io/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	readline-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
This is Atari 800, 800XL, 130XE and 5200 emulator.

%description -l pl.UTF-8
To jest emulator Atari 800, 800XL, 130XE i 5200.

%package common
Summary:	Atari 800 Emulator - common files for SDL and X11 versions
Summary(pl.UTF-8):	Emulator Atari 800 - pliki wspólne dla wersji SDL oraz X11
Group:		Applications/Emulators
Suggests:	Atari800-rom
Obsoletes:	Atari800 < 1.0.7

%description common
This is Atari 800, 800XL, 130XE and 5200 emulator.

This package contains common files for both SDL and X11 versions
of Atari800.

%description common -l pl.UTF-8
To jest emulator Atari 800, 800XL, 130XE i 5200.

Ten pakiet zawiera pliki wspólne dla wersji działających pod SDL
oraz X11.

%package x11
Summary:	Atari 800 Emulator - X Window version
Summary(pl.UTF-8):	Emulator Atari 800 - wersja dla systemu X Window
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}

%description x11
This is Atari 800, 800XL, 130XE and 5200 emulator.

This package contains Atari800 executable file configured for X11 with
OSS sound and joystick support.

%description x11 -l pl.UTF-8
To jest emulator Atari 800, 800XL, 130XE i 5200.

Ten pakiet zawiera wykonywalny plik emulatora skonfigurowany dla X11 z
obsługą dźwięku OSS i joysticka.

%package SDL
Summary:	Atari 800 Emulator - SDL version
Summary(pl.UTF-8):	Emulator Atari 800 - wersja SDL
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	Atari800-svga < 2.1.0

%description SDL
This is Atari 800, 800XL, 130XE and 5200 emulator.

This package contains Atari800 executable file configured for SDL with
sound and joystick support.

%description SDL -l pl.UTF-8
To jest emulator Atari 800, 800XL, 130XE i 5200.

Ten pakiet zawiera wykonywalny plik emulatora skonfigurowany dla SDL z
obsługą dźwięku i joysticka.

%prep
%setup -q -n atari800-%{version}
#%%patch0 -p1
%patch -P1 -p1

%build
cp -f /usr/share/automake/config.sub .

%configure \
	--target=default \
	--enable-crashmenu \
	--disable-silent-rules \
	--disable-stereosound \
	--with-sound=sdl \
	--with-video=sdl

%{__make}

%{__mv} src/atari800 atari800-SDL

%{__make} clean

%configure \
	--target=x11-shm \
	--enable-crashmenu \
	--disable-silent-rules \
	--disable-stereosound \
	--with-sound=oss \
	--with-video=yes

%{__make}

%{__mv} src/atari800 atari800-x11

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/atari800,%{_mandir}/man1}

install atari800-x11 $RPM_BUILD_ROOT%{_bindir}
install atari800-SDL $RPM_BUILD_ROOT%{_bindir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/atari800
cp -p src/atari800.man $RPM_BUILD_ROOT%{_mandir}/man1/atari800.1

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc DOC/{BUGS,CREDITS,ChangeLog,FAQ,NEWS,README,TODO,USAGE,*.txt} README.TXT
%attr(755,root,root) %{_bindir}/atari800
%dir %{_datadir}/atari800
%{_mandir}/man1/atari800.1*

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/atari800-x11

%files SDL
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/atari800-SDL
