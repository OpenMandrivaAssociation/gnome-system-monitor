%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Simple process monitor
Name:		gnome-system-monitor
Version:	 3.16.0
Release:	4
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-system-monitor/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool >= 0.41.0
BuildRequires:	itstool
BuildRequires:	pkgconfig(giomm-2.4) >= 2.27
BuildRequires:	pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:	pkgconfig(glibmm-2.4) >= 2.27
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(adwaita-icon-theme) >= 2.31
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
%configure2_5x

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
%{_libexecdir}/gnome-system-monitor/gsm-kill
%{_libexecdir}/gnome-system-monitor/gsm-renice
%{_datadir}/appdata/gnome-system-monitor.appdata.xml
%{_datadir}/polkit-1/actions/org.gnome.gnome-system-monitor.policy

