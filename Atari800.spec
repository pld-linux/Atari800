#
# Conditional build:
%bcond_with	license_agreement	# with unzipped ROM files instead of xf25.zip
#
Summary:	Atari 800 Emulator
Summary(pl.UTF-8):	Emulator Atari 800
Name:		Atari800
Version:	3.1.0
Release:	1
License:	GPL v2+ (Atari800), distributable if unmodified (xf25 with ROMs)
Group:		Applications/Emulators
Source0:	http://downloads.sourceforge.net/atari800/atari800-%{version}.tar.gz
# Source0-md5:	354f8756a7f33cf5b7a56377d1759e41
# NOTE: ROMs probably can be redistributed only in original XF25 archive
Source1:	http://joy.sophics.cz/www/xf25.zip
# Source1-md5:	4dc3b6b4313e9596c4d474785a37b94d
Source2:	%{name}-chooser
URL:		http://atari800.atari.org/
BuildRequires:	SDL-devel
BuildRequires:	automake
%if %{with license_agreement}
BuildRequires:	unzip
%endif
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
Obsoletes:	Atari800
%if !%{with license_agreement}
Requires(post):	unzip
%endif

%description common
This is Atari 800, 800XL, 130XE and 5200 emulator.

This package contains common files for both SDL and X11 versions
of Atari800.
%if !%{with license_agreement}
Note: because of license problems we had to include whole X-Former
archive (xf25.zip). If you don't want it - rebuild Atari800 (--with
license_agreement)
%endif 

%description common -l pl.UTF-8
To jest emulator Atari 800, 800XL, 130XE i 5200.

Ten pakiet zawiera pliki wspólne dla wersji działających pod SDL
oraz X11.
%if !%{with license_agreement}
Uwaga: z powodu problemów z licencją musieliśmy załączyć całą paczkę
z emulatorem X-Former (xf25.zip). Jeśli jej nie chcesz w pakiecie -
przebuduj pakiet z opcja --with license_agreement.
%endif

%package x11
Summary:	Atari 800 Emulator - X Window version
Summary(pl.UTF-8):	Emulator Atari 800 - wersja dla systemu X Window
License:	GPL
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
License:	GPL
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	Atari800-svga

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

%build
cd src
rm config.sub
cp -f /usr/share/automake/config.sub .

%configure \
	--target=x11-shm \
	--enable-crashmenu \
	--disable-stereosound \
	--with-sound=sdl \
	--with-video=sdl

%{__make}

%{__mv} atari800 atari800-SDL

%{__make} clean

%configure \
	--target=x11-shm \
	--enable-crashmenu \
	--disable-stereosound \
	--with-sound=oss \
	--with-video=no

%{__make}

%{__mv} atari800 atari800-x11

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/atari800,%{_mandir}/man1}

install src/atari800-x11 $RPM_BUILD_ROOT%{_bindir}
install src/atari800-SDL $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/atari800
install src/atari800.man $RPM_BUILD_ROOT%{_mandir}/man1/atari800.1

%if %{with license_agreement}
unzip -q -L %{SOURCE1} -d $RPM_BUILD_ROOT%{_datadir}/atari800
%{__rm} $RPM_BUILD_ROOT%{_datadir}/atari800/xf25.*
%else
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/atari800
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if !%{with license_agreement}
%post common
cd %{_datadir}/atari800
if [ "`echo *.rom`" = "*.rom" ]; then
	umask 022
	unzip -q -L xf25.zip
	rm -f xf25.doc xf25.exe
fi
%endif

%files common
%defattr(644,root,root,755)
%doc DOC/{BUGS,CREDITS,ChangeLog,FAQ,NEWS,README,TODO,USAGE,*.txt} README.1ST
%attr(755,root,root) %{_bindir}/atari800
%{_datadir}/atari800
%{_mandir}/man1/atari800.1*

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/atari800-x11

%files SDL
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/atari800-SDL
