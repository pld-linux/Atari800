#
# Conditional build:
%bcond_with	license_agreement	# with unzipped ROM files instead of xf25.zip
%bcond_without	svga 			# without SVGA version
#
Summary:	Atari 800 Emulator
Summary(pl):	Emulator Atari 800
Name:		Atari800
Version:	1.3.2
Release:	1
License:	GPL (Atari800), distributable if unmodified (xf25 with ROMs)
Group:		Applications/Emulators
Source0:	http://dl.sourceforge.net/atari800/atari800-%{version}.tar.gz
# Source0-md5:	8fcd251a3757270c02519ad7b86b7caa
# NOTE: ROMs probably can be redistributed only in original XF25 archive
Source1:	http://joy.sophics.cz/www/xf25.zip
# Source1-md5:	4dc3b6b4313e9596c4d474785a37b94d
Source2:	%{name}-chooser
URL:		http://atari800.atari.org/
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
%{?with_svga:BuildRequires:	svgalib-devel}
%if %{with license_agreement}
BuildRequires:	unzip
%endif
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
This is Atari 800, 800XL, 130XE and 5200 emulator.

%description -l pl
To jest emulator Atari 800, 800XL, 130XE i 5200.

%package common
Summary:	Atari 800 Emulator - common files for svgalib and X11 versions
Summary(pl):	Emulator Atari 800 - pliki wspólne dla wersji svgalib oraz X11
Group:		Applications/Emulators
Obsoletes:	Atari800
%if %{without license_agreement}
Requires(post):	unzip
%endif

%description common
This is Atari 800, 800XL, 130XE and 5200 emulator.

This package contains common files for both svgalib and X11 versions
of Atari800.
%if %{without license_agreement}
Note: because of license problems we had to include whole X-Former
archive (xf25.zip). If you don't want it - rebuild Atari800 (--with
license_agreement)
%endif 

%description common -l pl
To jest emulator Atari 800, 800XL, 130XE i 5200.

Ten pakiet zawiera pliki wspólne dla wersji dzia³aj±cych pod svgalib
oraz X11.
%if %{without license_agreement}
Uwaga: z powodu problemów z licencj± musieli¶my za³±czyæ ca³± paczkê
z emulatorem X-Former (xf25.zip). Je¶li jej nie chcesz w pakiecie -
przebuduj pakiet z opcja --with license_agreement.
%endif

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

%build
cd src
cp -f /usr/share/automake/config.sub .


CFLAGS="%{rpmcflags}"

%if %{with svga}
%configure \
	--target=svgalib \
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

%{__make}

mv -f atari800 atari800-svga

%{__make} clean
%endif

%configure \
	--target=sdl \
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

%{__make}

mv -f atari800 atari800-SDL

%{__make} clean

%configure \
	--target=shm \
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

%{__make}

mv -f atari800 atari800-x11

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/atari800,%{_mandir}/man1}

%if %{with svga}
install src/atari800-svga $RPM_BUILD_ROOT%{_bindir}
%endif
install src/atari800-x11 $RPM_BUILD_ROOT%{_bindir}
install src/atari800-SDL $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/atari800
install src/atari800.man $RPM_BUILD_ROOT%{_mandir}/man1/atari800.1

%if %{with license_agreement}
unzip -q -L %{SOURCE1} -d $RPM_BUILD_ROOT%{_datadir}/atari800
rm -f $RPM_BUILD_ROOT%{_datadir}/atari800/xf25.*
%else
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/atari800
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{without license_agreement}
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

%if %{with svga}
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/atari800-svga
%endif
