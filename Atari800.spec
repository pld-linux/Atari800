#
# Conditional build:
# _with_license_agreement - with unzipped ROM files instead of xf25.zip
# _without_svgalib	  - without SVGA version
#
Summary:	Atari 800 Emulator
Summary(pl):	Emulator Atari 800
Name:		Atari800
Version:	1.2.2
Release:	2
License:	GPL (Atari800), distributable if unmodified (xf25 with ROMs)
Group:		Applications/Emulators
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/atari800/atari800-%{version}.tar.gz
# NOTE: ROMs probably can be redistributed only in original XF25 archive
Source1:	http://joy.sophics.cz/www/xf25.zip
Source2:	%{name}-chooser
Patch0:		%{name}-shm_fix.patch
URL:		http://atari800.atari.org/
BuildRequires:	unzip
%ifarch %{ix86}
%{!?_without_svgalib:BuildRequires:	svgalib-devel}
%endif
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xbindir	%{_prefix}/X11R6/bin

%description
This is Atari 800, 800XL, 130XE and 5200 emulator.

%description -l pl
To jest emulator Atari 800, 800XL, 130XE i 5200.

%package common
Summary:	Atari 800 Emulator - common files for svgalib and X11 versions
Summary(pl):	Emulator Atari 800 - pliki wspólne dla wersji svgalib oraz X11
Group:		Applications/Emulators
Obsoletes:	Atari800
%{!?_with_license_agreement:Prereq:	unzip}

%description common
This is Atari 800, 800XL, 130XE and 5200 emulator.

This package contains common files for both svgalib and X11 versions
of Atari800.

%{!?_with_license_agreement:Note: because of license problems we had to include whole X-Former}
%{!?_with_license_agreement:archive (xf25.zip). If you don't want it - rebuild Atari800 by:}
%{!?_with_license_agreement:rpm --rebuild --with license_agreement ftp://ftp.pld.org.pl/PLD-1.0/SRPMS/SRPMS/%{name}-%{version}-%{release}.src.rpm}

%description common -l pl
To jest emulator Atari 800, 800XL, 130XE i 5200.

Ten pakiet zawiera pliki wspólne dla wersji dzia³aj±cych pod svgalib
oraz X11.

%{!?_with_license_agreement:Uwaga: z powodu problemów z licencj± musieli¶my za³±czyæ ca³± paczkê}
%{!?_with_license_agreement:z emulatorem X-Former (xf25.zip). Je¶li jej nie chcesz w pakiecie -}
%{!?_with_license_agreement:przebuduj pakiet poleceniem:}
%{!?_with_license_agreement:rpm --rebuild --with license_agreement ftp://ftp.pld.org.pl/PLD-1.0/SRPMS/SRPMS/%{name}-%{version}-%{release}.src.rpm}

%package svga
Summary:	Atari 800 Emulator - svgalib version
Summary(pl):	Emulator Atari 800 - wersja pod svgalib
License:	GPL
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description svga
This is Atari 800, 800XL, 130XE and 5200 emulator.

This package contains Atari800 executable file configured for svgalib
with sound and joystick support.

%description svga -l pl
To jest emulator Atari 800, 800XL, 130XE i 5200.

Ten pakiet zawiera wykonywalny plik emulatora skonfigurowany dla
svgalib z obs³ug± d¼wiêku i joysticka.

%package x11
Summary:	Atari 800 Emulator - X Window version
Summary(pl):	Emulator Atari 800 - wersja pod X Window
License:	GPL
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description x11
This is Atari 800, 800XL, 130XE and 5200 emulator.

This package contains Atari800 executable file configured for X11 with
sound and joystick support.

%description x11 -l pl
To jest emulator Atari 800, 800XL, 130XE i 5200.

Ten pakiet zawiera wykonywalny plik emulatora skonfigurowany dla X11 z
obs³ug± d¼wiêku i joysticka.

%package SDL
Summary:	Atari 800 Emulator - SDL version
Summary(pl):	Emulator Atari 800 - wersja pod SDL
License:	GPL
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description SDL
This is Atari 800, 800XL, 130XE and 5200 emulator.

This package contains Atari800 executable file configured for SDL with
sound and joystick support.

%description SDL -l pl
To jest emulator Atari 800, 800XL, 130XE i 5200.

Ten pakiet zawiera wykonywalny plik emulatora skonfigurowany dla SDL z
obs³ug± d¼wiêku i joysticka.

%prep
%setup -q -n atari800-%{version}
%patch0 -p1

%build
cd src

%if %{?_without_svgalib:0}%{!?_without_svgalib:1}
%ifarch %{ix86}

%configure2_13 --target=svgalib \
	--disable-VERY_SLOW \
	--enable-NO_CYCLE_EXACT \
	--enable-CRASH_MENU \
	--enable-MONITOR_BREAK \
	--enable-MONITOR_HINTS \
	--enable-MONITOR_ASSEMBLER \
	--enable-COMPILED_PALETTE \
	--enable-SNAILMETER \
	--disable-SVGA_SPEEDUP \
	--enable-USE_CURSORBLOCK \
	--disable-JOYMOUSE \
	--enable-LINUX_JOYSTICK \
	--enable-SOUND \
	--enable-NO_VOL_ONLY \
	--enable-NO_CONSOL_SOUND \
	--disable-SERIO_SOUND \
	--enable-NOSNDINTER \
	--disable-CLIP \
	--disable-STEREO \
	--disable-BUFFERED_LOG \
	--enable-SET_LED \
	--enable-NO_LED_ON_SCREEN

%{__make} \
	CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}" \
	LDFLAGS="%{rpmldflags}"
mv -f atari800 atari800-svga

%{__make} clean
%endif
%endif

%configure2_13 --target=sdl \
	--disable-VERY_SLOW \
	--enable-NO_CYCLE_EXACT \
	--enable-CRASH_MENU \
	--enable-MONITOR_BREAK \
	--enable-MONITOR_HINTS \
	--enable-MONITOR_ASSEMBLER \
	--enable-COMPILED_PALETTE \
	--enable-SNAILMETER \
	--enable-LINUX_JOYSTICK \
	--enable-SOUND \
	--enable-NO_VOL_ONLY \
	--enable-NO_CONSOL_SOUND \
	--disable-SERIO_SOUND \
	--enable-NOSNDINTER \
	--disable-CLIP \
	--disable-STEREO \
	--disable-BUFFERED_LOG \
	--enable-SET_LED \
	--enable-NO_LED_ON_SCREEN
	
%{__make} \
	CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer} -I/usr/X11R6/include/SDL" \
	LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib"
mv -f atari800 atari800-SDL

%{__make} clean

%configure2_13 --target=x11-shm \
	--disable-VERY_SLOW \
	--enable-NO_CYCLE_EXACT \
	--enable-CRASH_MENU \
	--enable-MONITOR_BREAK \
	--enable-MONITOR_HINTS \
	--enable-MONITOR_ASSEMBLER \
	--enable-COMPILED_PALETTE \
	--enable-SNAILMETER \
	--enable-LINUX_JOYSTICK \
	--enable-SOUND \
	--enable-NO_VOL_ONLY \
	--enable-NO_CONSOL_SOUND \
	--disable-SERIO_SOUND \
	--enable-NOSNDINTER \
	--disable-CLIP \
	--disable-STEREO

%{__make} \
	CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer} -I/usr/X11R6/include" \
	LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib"
mv -f atari800 atari800-x11

sed s@/usr/local/lib/atari@%{_datadir}/atari800@g atari800.man >atari800.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_xbindir}} \
	$RPM_BUILD_ROOT{%{_datadir}/atari800,%{_mandir}/man1}

%ifarch %{ix86}
%{!?_without_svgalib:install src/atari800-svga $RPM_BUILD_ROOT%{_bindir}}
%endif
install src/atari800-x11 $RPM_BUILD_ROOT%{_xbindir}
install src/atari800-SDL $RPM_BUILD_ROOT%{_xbindir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/atari800
install src/atari800.1 $RPM_BUILD_ROOT%{_mandir}/man1/atari800.1

%if %{?_with_license_agreement:1}%{!?_with_license_agreement:0}
unzip -q -L %{SOURCE1} -d $RPM_BUILD_ROOT%{_datadir}/atari800
rm -f $RPM_BUILD_ROOT%{_datadir}/atari800/xf25.*
%else
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/atari800
%endif

gzip -9nf DOC/{BUGS,CHANGES,CREDITS,FAQ,README,TODO,USAGE} README.1ST \
	DOC/{LPTjoy.txt,cart.txt,emuos.txt,pokeysnd.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{?_with_license_agreement:0}%{!?_with_license_agreement:1}
%post common
cd %{_datadir}/atari800
unzip -q -L xf25.zip
%endif

%files common
%defattr(644,root,root,755)
%doc  *.gz DOC/*.gz
%{_datadir}/atari800
%{_mandir}/man1/atari800.1*
%attr(755,root,root) %{_bindir}/atari800

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_xbindir}/atari800-x11

%files SDL
%defattr(644,root,root,755)
%attr(755,root,root) %{_xbindir}/atari800-SDL

%ifarch %{ix86}
%if %{?_without_svgalib:0}%{!?_without_svgalib:1}
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/atari800-svga
%endif
%endif
