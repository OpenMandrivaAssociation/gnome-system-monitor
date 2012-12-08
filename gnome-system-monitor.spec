Summary:	Simple process monitor
Name:		gnome-system-monitor
Version:	3.6.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/3.6/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	intltool >= 0.41.0 itstool
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
%{_datadir}/%{name}/*.ui
%{_datadir}/pixmaps/%{name}


%changelog
* Fri Oct  5 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Fri May 04 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.1-1
+ Revision: 796356
- new version 3.4.1
- removed old icons

* Fri Mar 09 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.1-1
+ Revision: 783679
- new version 3.2.1
- cleaned up spec

* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 2.28.2-3
+ Revision: 677079
- rebuild to add gconf2 as req

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.28.2-2
+ Revision: 664886
- mass rebuild

* Tue Sep 28 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.2-1mdv2011.0
+ Revision: 581762
- new version
- rediff patches

* Tue Mar 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.1-1mdv2010.1
+ Revision: 529948
- update to new version 2.28.1

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.28.0-3mdv2010.1
+ Revision: 521492
- rebuilt for 2010.1

* Fri Sep 25 2009 Olivier Blin <blino@mandriva.org> 2.28.0-2mdv2010.0
+ Revision: 448973
- do not require lsb-release for arm and mips, they are not lsb arches
  (from Arnaud Patard)

* Mon Sep 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446467
- update to new version 2.28.0

* Wed Aug 26 2009 Frederic Crozat <fcrozat@mandriva.com> 2.27.4-2mdv2010.0
+ Revision: 421512
- Update patch0
- Patch1 (Fedora): add polkit-1 support

* Mon Jul 13 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.4-1mdv2010.0
+ Revision: 395456
- new version
- drop patch 1

* Sat Jun 20 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.3-1mdv2010.0
+ Revision: 387476
- update to new version 2.27.3

* Fri May 22 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.2-1mdv2010.0
+ Revision: 378820
- update to new version 2.26.2

* Tue Apr 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 366955
- update to new version 2.26.1

* Tue Mar 31 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0.1-2mdv2009.1
+ Revision: 363036
- fix omf file list

* Mon Mar 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0.1-1mdv2009.1
+ Revision: 355980
- update to new version 2.26.0.1

* Mon Mar 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 347463
- update to new version 2.26.0

* Tue Feb 17 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 341295
- new version
- rediff patch 0
- fix autoreconf call

* Tue Jan 20 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.4-1mdv2009.1
+ Revision: 331571
- update to new version 2.24.4

* Mon Jan 12 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.3-1mdv2009.1
+ Revision: 328731
- new version
- fix format string
- remove old configure options

* Tue Oct 21 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 295947
- update to new version 2.24.1

* Tue Sep 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287354
- new version

* Mon Sep 01 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 278692
- new version

* Tue Aug 19 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 273560
- new version
- update patch 1

* Mon Aug 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.6-1mdv2009.0
+ Revision: 263568
- new version

* Tue Jul 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.5-1mdv2009.0
+ Revision: 240040
- new version

* Thu Jul 03 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.3-1mdv2009.0
+ Revision: 231412
- new version
- bump deps
- update the policykit patch from Fedora

* Tue Jul 01 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.3-1mdv2009.0
+ Revision: 230530
- new version
- update license

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue May 27 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.2-1mdv2009.0
+ Revision: 211622
- new version

* Mon Apr 14 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.1-1mdv2009.0
+ Revision: 192831
- new version

* Mon Mar 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183778
- new version

* Tue Feb 26 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 175276
- fix buildrequires
- new version
- fix buildrequires
- rediff the patch

  + Frederic Crozat <fcrozat@mandriva.com>
    - Patch0 (Fedora): add PolicyKit support (GNOME bug #491462)

* Mon Jan 14 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.5-2mdv2008.1
+ Revision: 151933
- fix buildrequires
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Dec 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.4-1mdv2008.1
+ Revision: 132654
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Funda Wang <fwang@mandriva.org>
    - drop old menu

* Tue Dec 04 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.3-1mdv2008.1
+ Revision: 115204
- new version

* Wed Nov 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.2-1mdv2008.1
+ Revision: 108578
- new version

* Mon Oct 15 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.1
+ Revision: 98607
- new version

* Mon Sep 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 89319
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - s/Mandrake/Mandriva/

* Wed Aug 29 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.91.1-1mdv2008.0
+ Revision: 74688
- new version
- no need to call intltoolize

* Sun Aug 26 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.91-1mdv2008.0
+ Revision: 71585
- new version
- fix build

* Mon Jul 30 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.6-1mdv2008.0
+ Revision: 56654
- new version

* Tue Jul 10 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.5-1mdv2008.0
+ Revision: 50854
- new version

* Mon Jun 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.4-1mdv2008.0
+ Revision: 41047
- new version

* Thu Jun 07 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.3-1mdv2008.0
+ Revision: 36605
- fix buildrequires
- new version
- update deps

* Mon May 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.2-1mdv2008.0
+ Revision: 32129
- new version

* Wed Apr 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.1.1-1mdv2008.0
+ Revision: 14383
- new version


* Mon Mar 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 142052
- new version

  + Thierry Vignaud <tvignaud@mandriva.com>
    - no need to package big ChangeLog when NEWS is already there

* Thu Mar 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.95-2mdv2007.1
+ Revision: 130283
- new version

* Wed Feb 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.94-1mdv2007.1
+ Revision: 126910
- fix buildrequires
- new version
- readd omf files

* Sun Feb 25 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.92-1mdv2007.1
+ Revision: 125669
- new version

* Mon Feb 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.91-1mdv2007.1
+ Revision: 118904
- fix buildrequires
- new version
- drop omf files

* Tue Jan 23 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.6-1mdv2007.1
+ Revision: 112235
- fix buildrequires
- new version
- fix buildrequires

  + Frederic Crozat <fcrozat@mandriva.com>
    - Add dependency on lsb-release for distribution detection

* Wed Dec 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.4.2-1mdv2007.1
+ Revision: 100370
- new version

* Tue Dec 19 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.4.1-1mdv2007.1
+ Revision: 99062
- new version

* Mon Dec 18 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.4-1mdv2007.1
+ Revision: 98393
- new version
- fix buildrequires

* Tue Dec 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.3-1mdv2007.1
+ Revision: 90714
- new version

* Tue Nov 28 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.2.1-3mdv2007.1
+ Revision: 87963
- fix buildrequires
- bot rebuild
- new version

* Fri Oct 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.1-2mdv2006.0
+ Revision: 63767
- rebuild
- Import gnome-system-monitor

* Thu Oct 12 2006 Götz Waschk <waschk@mandriva.org> 2.16.1-1mdv2007.1
- bump deps
- New version 2.16.1

* Wed Sep 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New version 2.16.0

* Wed Aug 23 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.92-1mdv2007.0
- New release 2.15.92

* Wed Aug 09 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.91-1mdv2007.0
- New release 2.15.91

* Fri Aug 04 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.90-2mdv2007.0
- Rebuild with latest dbus

* Thu Jul 27 2006 Götz Waschk <waschk@mandriva.org> 2.15.90-1mdv2007.0
- fix buildrequires
- New release 2.15.90

* Tue Jul 11 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.4-1
- New release 2.15.4

* Sat Jul 01 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.0-1
- New release 2.15.0

* Wed Jun 21 2006 Götz Waschk <waschk@mandriva.org> 2.14.4-1mdv2007.0
- use new macros
- xdg menu
- New release 2.14.4

* Thu May 18 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.3-1mdk
- New release 2.14.3

* Sun May 07 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-1mdk
- New release 2.14.2

* Wed Apr 19 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.1-1mdk
- Release 2.14.1
- Remove patch0 (merged upstream)

* Fri Feb 24 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.2-3mdk
- use mkrel
- fix prereq
- Patch0: remove debug output

* Fri Jan 06 2006 Oden Eriksson <oeriksson@mandriva.com> 2.12.2-2mdk
- dop selinux support

* Tue Nov 29 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.2-1mdk
- New release 2.12.2

* Thu Nov 03 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-2mdk
- Remove patch0 (no longer needed)

* Sat Oct 08 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-1mdk
- Release 2.12.1
- Regenerate patch0 (gotz)

* Sat Apr 23 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.10.1-2mdk
- remove BuildRequires: libgnomesu-devel

* Thu Apr 21 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-1mdk 
- Release 2.10.1 (based on Götz Waschk package)

* Mon Feb 14 2005 Götz Waschk <waschk@linux-mandrake.com> 2.8.3-1mdk
- drop patches 1,2
- New release 2.8.3

* Tue Feb 08 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.1-2mdk 
- Patch1 (CVS): show user memory
- Patch2 (CVS): fix crash at startup (Mdk bug #12639)

* Tue Dec 07 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.1-1mdk
- fix omf file listing
- New release 2.8.1

* Tue Nov 09 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.0-1mdk
- New release 2.8.0

* Thu Apr 22 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.0-2mdk
- Fix BuildRequires

* Wed Apr 07 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.0-1mdk
- Release 2.6.0 (with Götz help)
- requires new libwnck and libgtop
- requires new gtop

