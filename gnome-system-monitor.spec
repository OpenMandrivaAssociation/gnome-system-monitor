Summary: Simple process monitor
Name: gnome-system-monitor
Version: 3.4.1
Release: 1
License: GPLv2+
Group: Graphical desktop/GNOME
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	gnome-doc-utils
BuildRequires:	intltool >= 0.41.0
BuildRequires:	pkgconfig(giomm-2.4) >= 2.27
BuildRequires:	pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:	pkgconfig(glibmm-2.4) >= 2.27
BuildRequires:	pkgconfig(gnome-icon-theme) >= 2.31
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:	pkgconfig(gtkmm-3.0) >= 2.99
BuildRequires:	pkgconfig(libgtop-2.0) >= 2.28.2
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.12
BuildRequires:	pkgconfig(libwnck-3.0) >= 2.91.0
BuildRequires:	pkgconfig(libxml-2.0) >= 2.0
Requires:	polkit-agent
%ifnarch %arm %mips
Requires: lsb-release
%endif

%description
Gnome-system-monitor is a simple process and system monitor.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-scrollkeeper

%make LIBS='-lgmodule-2.0'

%install
%makeinstall_std
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README NEWS AUTHORS
%{_bindir}/gnome-system-monitor
%{_datadir}/applications/*
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-monitor.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-monitor.gschema.xml
%{_datadir}/%{name}/preferences.ui
%{_datadir}/pixmaps/%{name}

