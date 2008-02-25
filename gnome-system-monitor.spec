%define polkit_version 0.7
%define polkit_gnome_version 0.7

Summary: Simple process monitor
Name: gnome-system-monitor
Version: 2.21.92
Release: %mkrel 1
License: GPL
Group: Graphical desktop/GNOME
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source1: procman48.png
Source2: procman32.png
Source3: procman16.png
# (fc) 2.21.5-3mdv add PolicyKit support (Fedora) (GNOME bug #491462)
Patch0:	gnome-system-monitor-2.21.92-polkit.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: gtk2-devel
BuildRequires: gnome-vfs2-devel
BuildRequires: libgnome2-devel
BuildRequires: libgtop2.0-devel >= 2.19.3
BuildRequires: librsvg-devel
BuildRequires: libwnck-devel >= 2.5
BuildRequires: gtkmm2.4-devel
BuildRequires: gnome-icon-theme >= 2.15.3
BuildRequires: scrollkeeper
BuildRequires: gnome-doc-utils
BuildRequires: perl-XML-Parser
BuildRequires: libpolkit-devel >= %{polkit_version}
BuildRequires: libpolkit-gnome-devel >= %{polkit_gnome_version}

Obsoletes: procman gtop
Provides: procman = %{version}
Provides: gtop
Requires(post): scrollkeeper >= 0.3
Requires(postun): scrollkeeper >= 0.3
Requires: lsb-release
Requires: policykit-gnome >= %{polkit_gnome_version}

%description
Gnome-system-monitor is a simple process and system monitor.

%prep
%setup -q
%patch0 -p1 -b .polkit

#neeeded by patch0 
autoreconf

%build

%configure2_5x \
    --disable-selinux \
    --disable-libgksu \
    --enable-polkit

#needed by patch0
make -C src gnome-system-monitor-mechanism-glue.h gnome-system-monitor-mechanism-client-glue.h

%make

%install
rm -rf $RPM_BUILD_ROOT

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
rm -rf %buildroot/var
%find_lang %{name} --with-gnome
for omf in %buildroot%_datadir/omf/*/*-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done

rm -f $RPM_BUILD_ROOT%{_var}

mkdir -p $RPM_BUILD_ROOT%{_miconsdir} $RPM_BUILD_ROOT%{_liconsdir}

cp %{SOURCE1} $RPM_BUILD_ROOT%{_liconsdir}/procman.png
cp %{SOURCE2} $RPM_BUILD_ROOT%{_iconsdir}/procman.png
cp %{SOURCE3} $RPM_BUILD_ROOT%{_miconsdir}/procman.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_scrollkeeper
%post_install_gconf_schemas gnome-system-monitor
%{update_menus}

%preun
%preun_uninstall_gconf_schemas gnome-system-monitor

%postun
%clean_scrollkeeper
%{clean_menus}

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
%{_datadir}/PolicyKit/policy/org.gnome.system-monitor.policy
%{_datadir}/dbus-1/system-services/org.gnome.SystemMonitor.Mechanism.service
