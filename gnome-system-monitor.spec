%global optflags %{optflags} -Wno-narrowing

%define _disable_rebuild_configure 1
%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Simple process monitor
Name:		gnome-system-monitor
Version:	47.rc
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		https://www.gnome.org/
Source0:	https://ftp.gnome.org/pub/GNOME/sources/gnome-system-monitor/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool >= 0.41.0
BuildRequires:	itstool
BuildRequires:	pkgconfig(giomm-2.68)
BuildRequires:	pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:	pkgconfig(glibmm-2.68)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(adwaita-icon-theme) >= 2.31
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(gtkmm-4.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(libgtop-2.0) >= 2.38.0
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.12
BuildRequires:	pkgconfig(libwnck-3.0) >= 2.91.0
BuildRequires:	pkgconfig(libxml-2.0) >= 2.0
BuildRequires:  pkgconfig(systemd)
BuildRequires:  appstream-util
BuildRequires:  cmake
BuildRequires:	meson
BuildRequires:  polkit-1-devel
BuildRequires:	gnome-common
BuildRequires:	yelp-tools

Requires:	polkit-agent
%ifnarch %arm %mips
Requires: lsb-release
%endif

%description
Gnome-system-monitor is a simple process and system monitor.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README.md NEWS AUTHORS
%{_bindir}/gnome-system-monitor
%{_datadir}/applications/*
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-monitor.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-monitor.gschema.xml
%{_libexecdir}/gnome-system-monitor/gsm-kill
%{_libexecdir}/gnome-system-monitor/gsm-renice
%{_libexecdir}/gnome-system-monitor/gsm-taskset
%{_datadir}/metainfo/org.gnome.SystemMonitor.appdata.xml
%{_datadir}/polkit-1/actions/org.gnome.gnome-system-monitor.policy
%{_datadir}/gnome-system-monitor/gsm.gresource
%{_iconsdir}/hicolor/*/apps/org.gnome.SystemMonitor*.svg
