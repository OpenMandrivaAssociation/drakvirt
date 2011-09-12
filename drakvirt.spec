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

