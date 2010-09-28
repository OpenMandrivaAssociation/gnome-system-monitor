%define polkit_version 0.92

Summary: Simple process monitor
Name: gnome-system-monitor
Version: 2.28.2
Release: %mkrel 1
License: GPLv2+
Group: Graphical desktop/GNOME
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source1: procman48.png
Source2: procman32.png
Source3: procman16.png
# (fc) 2.21.5-3mdv add PolicyKit support (Fedora) (GNOME bug #491462)
Patch0:	gnome-system-monitor-2.28.2-polkit.patch
# (fc) 2.27.4-2mdv Polkit1 support (Fedora) (GNOME bug #491462)
Patch1: gnome-system-monitor-2.28.2-polkit1.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: gtk2-devel
BuildRequires: gnome-vfs2-devel
BuildRequires: libgnome2-devel
BuildRequires: libgtop2.0-devel >= 2.23.1
BuildRequires: librsvg-devel
BuildRequires: libwnck-devel >= 2.5
BuildRequires: gtkmm2.4-devel
BuildRequires: gnome-icon-theme >= 2.15.3
BuildRequires: scrollkeeper
BuildRequires: gnome-doc-utils
BuildRequires: polkit-1-devel >= %{polkit_version}
BuildRequires: intltool
Obsoletes: procman gtop
Provides: procman = %{version}
Provides: gtop
Requires(post): scrollkeeper >= 0.3
Requires(postun): scrollkeeper >= 0.3
%ifnarch %arm %mips
Requires: lsb-release
%endif
Requires: polkit-agent

%description
Gnome-system-monitor is a simple process and system monitor.

%prep
%setup -q
%patch0 -p1 -b .polkit
%patch1 -p1 -b .polkit1

#neeeded by patches 0 & 1
autoreconf -fi

%build

%configure2_5x \
    --enable-polkit

#needed by patch0
make -C src gnome-system-monitor-mechanism-glue.h gnome-system-monitor-mechanism-client-glue.h

%make

%install
rm -rf $RPM_BUILD_ROOT

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
rm -rf %buildroot/var
%find_lang %{name} --with-gnome
for omf in %buildroot%_datadir/omf/*/*[_-]??.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done

rm -f $RPM_BUILD_ROOT%{_var}

mkdir -p $RPM_BUILD_ROOT%{_miconsdir} $RPM_BUILD_ROOT%{_liconsdir}

cp %{SOURCE1} $RPM_BUILD_ROOT%{_liconsdir}/procman.png
cp %{SOURCE2} $RPM_BUILD_ROOT%{_iconsdir}/procman.png
cp %{SOURCE3} $RPM_BUILD_ROOT%{_miconsdir}/procman.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_scrollkeeper
%post_install_gconf_schemas gnome-system-monitor
%{update_menus}
%endif

%preun
%preun_uninstall_gconf_schemas gnome-system-monitor

%if %mdkversion < 200900
%postun
%clean_scrollkeeper
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-, root, root)
%doc README NEWS AUTHORS
%config(noreplace) %{_sysconfdir}/gconf/schemas/*
%{_bindir}/gnome-system-monitor
%{_datadir}/applications/*
%_datadir/pixmaps/%name
%dir %{_datadir}/omf/%name
%{_datadir}/omf/%name/%name-C.omf
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%{_sysconfdir}/dbus-1/system.d/org.gnome.SystemMonitor.Mechanism.conf
%{_libdir}/gnome-system-monitor-mechanism
%{_datadir}/polkit-1/actions/org.gnome.system-monitor.policy
%{_datadir}/dbus-1/system-services/org.gnome.SystemMonitor.Mechanism.service
