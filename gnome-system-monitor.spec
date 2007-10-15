Summary: Simple process monitor
Name: gnome-system-monitor
Version: 2.20.1
Release: %mkrel 1
License: GPL
Group: Graphical desktop/GNOME
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source1: procman48.png
Source2: procman32.png
Source3: procman16.png

BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: gtk2-devel
BuildRequires: gnome-vfs2-devel
BuildRequires: libgnome2-devel
BuildRequires: libgtop2.0-devel >= 2.19.3
BuildRequires: libwnck-devel >= 2.5
BuildRequires: gtkmm2.4-devel
BuildRequires: pcre-devel
BuildRequires: gnome-icon-theme >= 2.15.3
BuildRequires: scrollkeeper
BuildRequires: gnome-doc-utils
BuildRequires: perl-XML-Parser
BuildRequires: desktop-file-utils
Obsoletes: procman gtop
Provides: procman = %{version}
Provides: gtop
Requires(post): scrollkeeper >= 0.3
Requires(postun): scrollkeeper >= 0.3
Requires: lsb-release

%description
Gnome-system-monitor is a simple process and system monitor.

%prep
%setup -q

%build

%configure2_5x \
    --disable-selinux \
    --disable-libgksu

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

# Mandriva menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}

cat << EOF >  $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):\
 needs="x11"\
 section="System/Monitoring"\
 title="GNOME System monitor"\
 longtitle="View current processes and monitor system state"\
 command="%{_bindir}/gnome-system-monitor"\
 icon="procman.png" \
 startup_notify="true" xdg="true"
EOF
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Monitoring" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


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
%{_menudir}/*
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png
