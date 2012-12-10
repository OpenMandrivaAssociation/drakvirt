%define name drakvirt
%define version 0.8.2
%define release %mkrel 3

Summary:	Virtualization configuration
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Patch:		xen.pm.patch
License:	GPL
Group:		System/Configuration/Other
Url:		https://svn.mandriva.com/svn/soft/drakvirt/trunk/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch
Requires:	drakxtools >= 10.4.222-1mdv2008.0

%description
This tool allows to configure virtualization using Xen.

%prep
%setup -q
%patch -p0

%build
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %name

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%_sbindir/%name
%dir %_datadir/%name
%_datadir/%name/*.pm
%dir %_datadir/%name/virtual
%_datadir/%name/virtual/*.pm
%_datadir/applications/%name.desktop
%_prefix/lib/libDrakX/icons/*.png
%{_iconsdir}/%{name}.png



%changelog
* Mon Sep 12 2011 Sergey Zhemoitel <serg@mandriva.org> 0.8.2-3mdv2012.0
+ Revision: 699571
- fix requires for xen

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-2mdv2011.0
+ Revision: 610275
- rebuild

* Wed May 26 2010 Christophe Fergeau <cfergeau@mandriva.com> 0.8.2-1mdv2010.1
+ Revision: 546249
- 0.8.2
- translation updates

* Sun May 02 2010 Funda Wang <fwang@mandriva.org> 0.8.1-2mdv2010.1
+ Revision: 541553
- fix perms of data files

* Wed Apr 15 2009 Thierry Vignaud <tv@mandriva.org> 0.8.1-1mdv2009.1
+ Revision: 367393
- translation updates

* Mon Sep 22 2008 Thierry Vignaud <tv@mandriva.org> 0.8-1mdv2009.0
+ Revision: 287076
- translation updates

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.7-3mdv2009.0
+ Revision: 244540
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Mar 25 2008 Thierry Vignaud <tv@mandriva.org> 0.7-1mdv2008.1
+ Revision: 190158
- translation updates
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Oct 04 2007 Thierry Vignaud <tv@mandriva.org> 0.6-1mdv2008.0
+ Revision: 95424
- hide menu entry since our tools are accessible through mcc

* Wed Oct 03 2007 Olivier Blin <blino@mandriva.org> 0.5-1mdv2008.0
+ Revision: 95249
- add icon in iconsdir
- 0.5
- use drakvirt icon in menu entry

* Fri Sep 28 2007 Olivier Blin <blino@mandriva.org> 0.4-2mdv2008.0
+ Revision: 93783
- fix drakxtools requires

* Fri Sep 28 2007 Olivier Blin <blino@mandriva.org> 0.4-1mdv2008.0
+ Revision: 93740
- require a new drakxtools version to allow asking for directory
- 0.4
- ask for a directory in the "Installer path" dialog (#30202, #34278)

* Sun Sep 23 2007 Olivier Blin <blino@mandriva.org> 0.3-1mdv2008.0
+ Revision: 92374
- 0.3: do not require lilo to be installed

* Mon Sep 17 2007 Olivier Blin <blino@mandriva.org> 0.2-1mdv2008.0
+ Revision: 89161
- 0.2
- adapt to kernel-xen naming and do not rebuild initrd (#30509)
- install mbootpack before xen (since xen pulls kernel-xen)
- install mbootpack only if lilo is used

